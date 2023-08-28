import requests
from bs4 import BeautifulSoup

def getLabels():
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    checkboxes = soup.find_all('input', {'type': 'checkbox', 'name': 'fieldIds'})

    options = {} 

    for checkbox in checkboxes:
        label = checkbox.find_next('label') 
        text = label.get_text(strip=True)  
        option_value = label.get('for')
        
        options[text] = option_value 
    
    return options

options = getLabels()
print(options)
