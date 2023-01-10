from selenium import webdriver
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook,load_workbook

# 계절학기에는 수업과목들이 없어 2학기 웹페이지로 이동함

word = input("검색태그를 입력하시오.: ")
url = 'https://www.instagram.com'
driver = webdriver.Chrome(executable_path=r'C:\Users\wnsdu\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(url)
time.sleep(3)



# 아이디 입력
user_id = input('인스타 아이디를 입력해주세요.: ')
et_login = driver.find_element_by_name("username")
et_login.clear()
et_login.send_keys(user_id)


# 비밀번호 입력
user_pw = input('에브리타임 비밀번호를 입력해주세요.: ')
et_login = driver.find_element_by_name("password")
et_login.clear()
et_login.send_keys(user_pw) #자신의 비번을 넣으세요

driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[3]""").click()  # 로그인 버튼 클릭
time.sleep(2)

word = input('검색어 입력: ')
word = str(word)



