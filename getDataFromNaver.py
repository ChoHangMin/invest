from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def setting():
    option = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=option)
    driver.maximize_window()

    # naver 증권홈 > 국내증시 > 시가총액
    driver.get('https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1')
    #checkbox_elements = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    #print(checkbox_elements)
    
    return driver  # WebDriver 객체를 반환

driver = setting()

time.sleep(5)
driver.quit()
