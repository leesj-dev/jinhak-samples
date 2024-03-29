from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from pwinput import pwinput
import time
import sys
import re
import convert  # 반드시 convert.py를 동일 디렉토리에 둬야 함


## 초기설정
login_id = input("진학사 ID: ")  # 진학사 ID
login_pw = pwinput(prompt="진학사 비밀번호: ", mask="*")  # 진학사 비밀번호
link = "https://hijinhak.jinhak.com/SAT/J1Apply/J1MyApplyList.aspx?LeftTab=1"

while True:
    until_self = input("전체 등수 크롤링은 1, 본인 앞의 등수까지 크롤링은 2를 입력하세요: ")
    if until_self in ["1", "2"]:
        until_self = bool(int(until_self) - 1)
        break
    else:
        print("1 또는 2를 입력하세요: ")

while True:
    all_applicant = input("실제지원자 통계 크롤링은 1, 전체지원자 통계 크롤링은 2를 입력하세요: ")
    if all_applicant in ["1", "2"]:
        all_applicant = bool(int(all_applicant) - 1)
        break
    else:
        print("1 또는 2를 입력하세요: ")

chrome_options = Options()
# headless mode. 향후 개발이 모두 완료된 후 아래 주석 제거할 예정
"""
chrome_options.add_argument("headless")
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument("--start-maximized")
"""

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

## 링크 접속
driver.get(link)
driver.find_element(By.XPATH, '//*[@id="txtMemID"]').send_keys(login_id)
driver.find_element(By.XPATH, '//*[@id="txtMemPass"]').send_keys(login_pw)
driver.find_element(By.XPATH, '//*[@id="panel_1"]/div/div[1]/div[3]/button').click()
driver.implicitly_wait(5)

## 군별로 실행해야 하는 js 정리
driver.switch_to.frame(driver.find_element(By.ID, "ifrmJ1MyApplyListBtm"))  # iframe 내에 있으므로
group_dict = {}
for i in range(3):
    group_name = driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div/table/tbody/tr[' + str(i + 1) + ']/td[3]').get_attribute("innerHTML")[:-1]  # '군' 제거
    group_js = driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div/table/tbody/tr[' + str(i + 1) + ']/td[10]/a').get_attribute("href")[11:]  # 앞의 'javascript:' 제거
    group_dict[group_name] = group_js

## list의 문자들을 int로 변환하는 함수
def digit_to_int(classes: list, type_of_class: str) -> float:
    length: int = len(classes) // convert.digital_dict[type_of_class][2]
    convert_dict_2: dict = convert.digital_dict[type_of_class][1]
    num = ""
    for item in zip(*[classes[i : i + length] for i in range(0, len(classes), length)]):
        num += convert_dict_2[item]
    return float(num)

## 군별 크롤링
def scrape_group(group_id_js: str, all_applicant: bool, until_self: bool):
    driver.switch_to.window(driver.window_handles[0])  # 메인창으로 이동
    driver.execute_script(group_id_js)
    driver.switch_to.window(driver.window_handles[1])  # 팝업창으로 이동
    driver.execute_script("fn_Href(1)")
    if all_applicant == True:
        driver.execute_script("GoTab(2);return false;") # 전체지원자 통계 전환
    applicant_num = driver.find_element(By.XPATH, "//*[@id='rUnivInfo']/div/div[3]/ul/li[7]/dl/dd").get_attribute("innerHTML")
    applicant_num = applicant_num.replace(" ", "")
    driver.execute_script("window.scrollTo(0,1500)")  # iframe 로딩을 위해 스크롤 내리기
    time.sleep(5)  # 내부 iframe 로딩
    driver.switch_to.frame(driver.find_element(By.ID, "ifrmGraph"))
    highest = driver.find_element(By.XPATH, "/html/body/form[1]/div[3]/div[1]/ul/li[1]").get_attribute("id") #지원자 분포 최고점수 범위
    lowest = driver.find_element(By.XPATH, "//*[@id='graph_1']/div[1]/ul/li[last()]").get_attribute("id")
    driver.execute_script("ViewDetailRank(" + str(lowest) + ", " + str(highest) + ", 0," + str(applicant_num) + ")")
    driver.switch_to.frame(driver.find_element(By.ID, "ifrmRank"))  #점수분포 iframe으로 전환

    # css 정보 스크레이핑
    digital_css: str = driver.find_element(By.XPATH, "/html/body/style").get_attribute("innerHTML")

    # digital / digitalT / digitalM 중 어느 것인지 판별
    for item in convert.digital_dict.keys():
        if item in digital_css:
            digital_info = item

    # 아래부터 계속 전처리
    css_info = [re.split("\s|:", item[2:], 1) for item in digital_css.split("." + digital_info) if item != " "]

    # 마지막 문자 공백 시 제거
    for item in css_info:
        if item[1][-1] == " ":
            item[1] = item[1][:-1]

    key, val = map(list, zip(*css_info))
    css_dict = {}
    for i in range(len(key) - 1):
        if key[i] != key[i + 1]:
            css_dict[key[i]] = ()
    css_dict[key[len(key) - 1]] = ()
    for i in range(len(key)):
        css_dict[key[i]] += (val[i],)
    # print({y: x for x, y in css_dict.items()}) -- convert.py의 dictionary들을 만들기 위한 용도 (사용 금지)

    scores, subjects = [], []
    i = 1
    while True:
        try:
            scores.append(driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div/div/div[' + str(i) +']/div[2]/p[1]/span/b/span').get_attribute("innerHTML"))
            subjects.append(driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div/div/div[' + str(i) +']/div[2]/p[1]/span/span').get_attribute("innerHTML").split(","))
            i += 1
        except:
            break
        else:
            if until_self is True and "me" in driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div/div/div[' + str(i) + ']').get_attribute("class"):
                break

    # HTML 파싱
    for i in range(len(scores)):
        soup = BeautifulSoup(scores[i], "html.parser")
        classes = [value for item in soup.find_all(class_=True) for value in item["class"]]
        convert_dict_1: dict = convert.digital_dict[digital_info][0]
        classes_std = []

        # classes 내의 각 class_name에 대하여 -> css 정보로 변환 -> 다시 표준형으로 변환 -> 해당되는 숫자로 변환
        for class_name in classes:
            try:
                classes_std.append(convert_dict_1[css_dict[class_name]])
            except:  # 아무것도 없는 거는 애초에 CSS 정의가 안 되어있으므로 * 처리
                classes_std.append("*")
        try:
            print("{:.2f}".format(digit_to_int(classes_std, digital_info)), end=" ")  # 소숫점 둘째 자리까지 출력
        except:
            print("Error", end=" ")
        finally:
            print(' '.join(subjects[i]))

    print("")  # 가독성을 위해 빈 줄 추가

for group in ["가", "나", "다"]:
    if all_applicant:
        sys.stdout = open('all_applicant.csv', 'w')
        print("〈" + group + "군 〉")
        scrape_group(group_dict[group], all_applicant, until_self)
    else:
        sys.stdout = open('real_applicant.csv', 'w')
        print("〈" + group + "군 〉")
        scrape_group(group_dict[group], all_applicant, until_self)

# 코드 실행 후 창 안 닫기게 하려고
time.sleep(10000)