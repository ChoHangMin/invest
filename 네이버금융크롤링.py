from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
import time
import datetime

오늘날짜 = datetime.datetime.now().strftime('%Y.%m.%d')
option = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=option)

pd.set_option('display.float_format', '{:.2f}'.format) # 항상 float 형식

def setting():
    driver.find_element_by_id("option1").click()
    driver.find_element_by_id("option15").click()
    driver.find_element_by_id("option21").click()
    driver.find_element_by_id("option4").click()
    driver.find_element_by_id("option6").click()
    driver.find_element_by_id("option12").click()


거래량=1
시가=7
고가=13
저가=19
매수호가=2
매도호가=8
매수총잔량=14
매도총잔량=20
거래대금_백만=3
전일거래량=9
외국인비율=15
상장주식수_천주=21
시가총액_억=4
자산총계_억=10
부채총계_억=16
매출액_억=22
매출액증가율=25
영업이익_억=5
엽엉이익증가율=11
당기순이익_억=17
주당순이익_원=23
보통주배당금_억=26
PER_배=6
ROE=12
ROA=18
PBR=24
유보율=27



옵션=[거래량,시가,고가,저가,매수호가,매도호가,매수총잔량,매도총잔량,거래대금_백만,전일거래량,외국인비율,상장주식수_천주,시가총액_억,자산총계_억,부채총계_억,
   매출액_억,매출액증가율,영업이익_억,엽엉이익증가율,당기순이익_억,주당순이익_원,보통주배당금_억,PER_배,ROE,ROA,PBR,유보율]

driver.get('https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1')

코스피=[]
cnt=0
for a in range(1,6):
    
    초기화=driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/form/div/div/div/a[2]/img").click()
    time.sleep(2)
    setting()
    for i in 옵션[0+cnt:6+cnt]:
        driver.find_element_by_id(f"option{i}").click()

    적용하기=driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/form/div/div/div/a[1]/img").click()

    #코스피
    temp_df = pd.DataFrame()
    for page in range(1,33):
        driver.get(f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={page}')
        html = driver.page_source #지금 현 상태의 page source불러오기
        soup = BeautifulSoup(html,'html.parser')
        table = soup.find('table',{'class':"type_2"})#재무제표 영역 불러오기
        p=parser.make2d(table)
        df=pd.DataFrame(p[2:],columns=p[0])
        df.drop_duplicates( keep=False, inplace=True)
        df.set_index("N",inplace=True)
        temp_df=temp_df.append(df)


    
    if cnt==24:
        cnt+=3
    else:
        cnt+=6
    코스피.append(temp_df)

코스피2=pd.concat([코스피[0],코스피[1],코스피[2],코스피[3],코스피[4]],axis=1)
코스피3=코스피2.loc[:,~코스피2.columns.duplicated()]


코스닥 =[]
cnt=0
for a in range(1,6):
    
    초기화=driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/form/div/div/div/a[2]/img").click()
    time.sleep(2)
    setting()
    for i in 옵션[0+cnt:6+cnt]:
        driver.find_element_by_id(f"option{i}").click()

    적용하기=driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/form/div/div/div/a[1]/img").click()

    #코스닥
    temp_df = pd.DataFrame()
    for page in range(1,29):
        driver.get(f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page={page}')
        html = driver.page_source #지금 현 상태의 page source불러오기
        soup = BeautifulSoup(html,'html.parser')
        table = soup.find('table',{'class':"type_2"})#재무제표 영역 불러오기
        p=parser.make2d(table)
        df=pd.DataFrame(p[2:],columns=p[0])
        df.drop_duplicates( keep=False, inplace=True)
        df.set_index("N",inplace=True)
        temp_df=temp_df.append(df)
    

    
    if cnt==24:
        cnt+=3
    else:
        cnt+=6
    
    코스닥.append(temp_df)
    
코스닥2=pd.concat([코스닥[0],코스닥[1],코스닥[2],코스닥[3],코스닥[4]],axis=1)
코스닥3=코스닥2.loc[:,~코스닥2.columns.duplicated()]
#코스닥3.to_excel("./분석/네이버금융/국내증시_코스닥.xlsx")

국내증시=pd.concat([코스피3,코스닥3])
국내증시.to_excel(f"{[오늘날짜]}국내증시.xlsx")