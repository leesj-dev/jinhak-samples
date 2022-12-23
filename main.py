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

## 초기설정
load_dotenv()
login_id = os.getenv("id")  # 진학사 ID
login_pw = os.getenv("pw")  # 진학사 비밀번호
link_main = "https://hijinhak.jinhak.com/SAT/J1Apply/J1MyApplyList.aspx?LeftTab=1"

chrome_options = Options()
## 향후 개발이 모두 완료된 후 주석 제거할 예정
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


digitalT_std = {
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T1",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T2",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
    ): "T3",
    (
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T4",
    ("after { right: 2px; bottom: 0; width: 2px; height: 2px; } ",): "T5",
    ("em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",): "T6",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; } ",): "T7",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T8",
    (
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
    ): "T9",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T10",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
    ): "T11",
}

digits_digitalT = {
    ("T1", "T1"): "1",
    ("T7", "T4"): "2",
    ("T7", "T3"): "3",
    ("T6", "T7"): "4",
    ("T9", "T3"): "5",
    ("T5", "T8"): "6",
    ("T7", "T1"): "7",
    ("T10", "T8"): "8",
    ("T10", "T7"): "9",
    ("T10", "T11"): "0",
    ("*", "T2"): ".",
}


def digit_to_int(classes: list, type_of_class: str) -> float:
    length = len(classes) // 2
    num = ""
    if type_of_class == "digitalT":
        dictionary = digits_digitalT
    else:
        print("Error")

    # 아래 split문은 패턴이 2가지일 때만 성립하며, 3일 때도 있으므로 추후 다른 방법을 강구해보겠음
    for item in zip(classes[:length], classes[length:]):
        num += dictionary[item]
    return float(num)


## 가군
driver.execute_script("parent.ReportOpenLast('3', '23R146151E91AB6B118', 'TOT');")  # 가군
driver.switch_to.window(driver.window_handles[1])  # 팝업창으로 이동
driver.execute_script("window.scrollTo(0,1400)")  # 스크롤 내리기
time.sleep(5)
digitalT_scrape = driver.find_element(By.XPATH, "/html/body/style").get_attribute(
    "innerHTML"
)

# 전처리
css_info = [
    re.split("\s|:", item[2:], 1)
    for item in digitalT_scrape.split(".digitalT")
    if item != ""
]
key, val = map(list, zip(*css_info))
css_dict = {}
for i in range(0, len(key) - 1):
    if key[i] != key[i + 1]:
        css_dict[key[i]] = ()
css_dict[key[len(key) - 1]] = ()
for i in range(0, len(key)):
    css_dict[key[i]] += (val[i],)
# css_dict = {y: x for x, y in css_dict.items()} -- 변환 용도 (사용 금지)

# subjects = driver.find_elements(By.XPATH, '//*[@id="DivA"]/div/*/div[2]/p[1]/span/span')
# print(subjects)
scores = driver.find_elements(By.CLASS_NAME, "digitalT")
print(scores)  # 임시

for item in scores:
    soup = BeautifulSoup(item.get_attribute("innerHTML"), "html.parser")
    classes = [value for item in soup.find_all(class_=True) for value in item["class"]]
    classes_std = []

    # classes 내의 각 class_name에 대하여 -> css 정보로 변환 -> 다시 Tx 표준형으로 변환 -> 해당되는 것으로 변환
    for class_name in classes:
        try:
            classes_std.append(digitalT_std[css_dict[class_name]])
        except:  # 아무것도 없는 거는 애초에 CSS 정의가 안 되어있음
            classes_std.append("*")

    try:
        print(digit_to_int(classes_std, "digitalT"))
    except:
        print("Error")

time.sleep(10000)

"""
## 나군
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("parent.ReportOpenLast('3', '23R141591F09D90464D', 'TOT');")  # 나군
driver.switch_to.window(driver.window_handles[1])
time.sleep(10)

## 다군
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("parent.ReportOpenLast('3', '23R13705168452A594F', 'TOT');")  # 다군
driver.switch_to.window(driver.window_handles[1])
time.sleep(10000)
"""
