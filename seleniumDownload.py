'''
import os, time
from selenium import webdriver
import chromedriver_autoinstaller

def chrome_driver():
    options = webdriver.ChromeOptions()
    chrome_ver = chromedriver_autoinstaller.get_chrome_version()
    print(f'current chrome ver : {chrome_ver}')
    chrome_driver = f'./{chrome_ver.split(".")[0]}/chromedriver.exe'
    if not os.path.exists(chrome_driver):
        os.makedirs(os.path.dirname(chrome_driver), exist_ok=True)
        res = chromedriver_autoinstaller.install(True)

        if res:
            print(f'chrome driver install finished!({chrome_ver.split(".")[0]} version)')
        else:
            print(f'chrome driver install error!({chrome_ver.split(".")[0]} version)')
    driver = webdriver.Chrome(chrome_driver, options)
    return driver

driver = chrome_driver()
time.sleep(3)

driver.quit()
'''

'''
import os, time
from selenium import webdriver
import chromedriver_autoinstaller

def chrome_driver():
    chrome_ver = chromedriver_autoinstaller.get_chrome_version()
    print(f'current chrome ver: {chrome_ver}')
    chrome_driver = f'./{chrome_ver.split(".")[0]}/chromedriver.exe'
    if not os.path.exists(chrome_driver):
        os.makedirs(os.path.dirname(chrome_driver), exist_ok=True)
        res = chromedriver_autoinstaller.install(True)

        if res:
            print(f'chrome driver install finished! ({chrome_ver.split(".")[0]} version)')
        else:
            print(f'chrome driver install error! ({chrome_ver.split(".")[0]} version)')
    
    # ChromeOptions 객체를 생성하고 원하는 설정을 추가할 수 있습니다.
    options = webdriver.ChromeOptions()
    
    # executable_path를 설정하여 chromedriver의 경로를 지정합니다.
    options.executable_path = chrome_driver
    
    # 다른 옵션을 추가할 수 있습니다.
    # options.add_argument("--headless")  # Headless 모드로 실행 등
    
    driver = webdriver.Chrome(options=options)
    return driver

driver = chrome_driver()
driver.get('https://naver.com')
driver.implicitly_wait(5)
driver.quit()
'''

