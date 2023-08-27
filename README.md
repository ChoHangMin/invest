chrome ver : 116.0.5845.111

## Setting
chrome version이 116이 넘어가면서 chromedriver error 다수 발생. 직접 다운로드하는 방식 사용
```bash
pip install selenium
```
만약 undetected_chromedriver가 있다면
```
pip uninstall undetected_chromedriver 
```
이후,
```bash
pip install -e git+https://github.com/jdholtz/undetected-chromedriver.git@f91b7d86bc257d4cb9bfc848266e82509868e2c6#egg=undetected_chromedriver
``` 

.gitignore에서
```gitignore
/src/undetected-chromedriver/
```
설정 후 저장


기본 사용 코드

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 셀레니움 옵션
option = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=option)

# 페이지 이동
driver.get(url='http://naver.com')
```

## 예상되는 문제점 
```python
driver.find_element_by_xpath()
```
없어짐. 대신,
```python
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="hello world"]')
```
으로 사용 가능.

## docs
https://selenium-python.readthedocs.io/index.html