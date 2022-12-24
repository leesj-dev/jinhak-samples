from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time
import re
import convert


## 초기설정
load_dotenv()
login_id = os.getenv("id")  # 진학사 ID
login_pw = os.getenv("pw")  # 진학사 비밀번호
link_main = "https://hijinhak.jinhak.com/SAT/J1Apply/J1MyApplyList.aspx?LeftTab=1"

chrome_options = Options()
# headless mode. 향후 개발이 모두 완료된 후 아래 주석 제거할 예정
"""
chrome_options.add_argument("headless")
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument("--start-maximized")
"""
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

## 링크 접속
driver.get("https://hijinhak.jinhak.com/SAT/J1Apply/J1MyApplyList.aspx?LeftTab=1")
driver.find_element(By.XPATH, '//*[@id="txtMemID"]').send_keys(login_id)
driver.find_element(By.XPATH, '//*[@id="txtMemPass"]').send_keys(login_pw)
driver.find_element(By.XPATH, '//*[@id="panel_1"]/div/div[1]/div[3]/button').click()
driver.implicitly_wait(5)

## list의 문자들을 int로 변환하는 함수
def digit_to_int(classes: list, type_of_class: str) -> float:
    length = len(classes) // convert.digital_dict[type_of_class][2]
    convert_dict_2 = convert.digital_dict[type_of_class][1]
    num = ""
    for item in zip(*[classes[i : i + length] for i in range(0, len(classes), length)]):
        num += convert_dict_2[item]

    return float(num)


def scrape_group(group_id):
    driver.switch_to.window(driver.window_handles[0])  # 메인창으로 이동
    driver.execute_script("parent.ReportOpenLast('3', '" + group_id + "', 'TOT');")
    driver.switch_to.window(driver.window_handles[1])  # 팝업창으로 이동
    driver.execute_script("window.scrollTo(0,1500)")  # 스크롤 내리기
    time.sleep(5)  # 내부 iframe 로딩
    driver.switch_to.frame(driver.find_element(By.ID, "ifrmGraph"))  # iframe 내에 있으므로

    # css 정보 스크레이핑
    digital_css = driver.find_element(By.XPATH, "/html/body/style").get_attribute(
        "innerHTML"
    )

    for item in convert.digital_dict.keys():
        if item in digital_css:
            digital_info = item

    # 전처리
    css_info = [
        re.split("\s|:", item[2:], 1)
        for item in digital_css.split("." + digital_info)
        if item != " "
    ]

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
    # print({y: x for x, y in css_dict.items()})  # -- 변환 용도 (사용 금지)

    ## 과목 스크레이핑 (좀 있다가 할 것)
    # subjects = driver.find_elements(By.XPATH, '//*[@id="DivA"]/div/*/div[2]/p[1]/span/span')
    # print(subjects)

    # [1::2]는 중복방지를 위해 그 중 짝수 번째(bottom)만 출력
    scores = driver.find_elements(By.CLASS_NAME, digital_info)[1::2]

    ## HTML 파싱
    for item in scores:
        soup = BeautifulSoup(item.get_attribute("innerHTML"), "html.parser")
        classes = [
            value for item in soup.find_all(class_=True) for value in item["class"]
        ]
        convert_dict_1 = convert.digital_dict[digital_info][0]
        classes_std = []

        # classes 내의 각 class_name에 대하여 -> css 정보로 변환 -> 다시 Tx 표준형으로 변환 -> 해당되는 숫자로 변환
        for class_name in classes:
            try:
                classes_std.append(convert_dict_1[css_dict[class_name]])
            except:  # 아무것도 없는 거는 애초에 CSS 정의가 안 되어있으므로 * 처리
                classes_std.append("*")
        try:
            print("{:.2f}".format(digit_to_int(classes_std, digital_info)))  # 소숫점 둘째 자리
        except:
            print("Error")

    time.sleep(3)


group_ids = ["2C31461515AD59D5E40", "2C31461515AD59D5E40", "2C313705174A9FE40AA"]
scrape_group(group_ids[2])

# 디버깅 용도
time.sleep(10000)
