from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

## 초기 실정
load_dotenv()
login_id = os.getenv("id")  # 진학사 ID
login_pw = os.getenv("pw")  # 진학사 비밀번호
link_main = os.getenv("link_main")  # 가군 실지원 링크

chrome_options = Options()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("window-size=1920x1080")
# chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
## 링크 접속
driver.get("https://hijinhak.jinhak.com/SAT/J1Apply/J1MyApplyList.aspx?LeftTab=1")
driver.find_element(By.XPATH, '//*[@id="txtMemID"]').send_keys(login_id)
driver.find_element(By.XPATH, '//*[@id="txtMemPass"]').send_keys(login_pw)
driver.find_element(By.XPATH, '//*[@id="panel_1"]/div/div[1]/div[3]/button').click()
driver.implicitly_wait(5)
driver.execute_script("parent.ReportOpenLast('3', '23R146151E91AB6B118', 'TOT');")
# driver.execute_script("parent.ReportOpenLast('3', '23R141591F09D90464D', 'TOT');")
# driver.execute_script("parent.ReportOpenLast('3', '23R13705168452A594F', 'TOT');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(1000)
