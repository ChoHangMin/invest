from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 셀레니움 옵션
option = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=option)

# 페이지 이동
driver.get(url='http://hoood.tistory.com')
