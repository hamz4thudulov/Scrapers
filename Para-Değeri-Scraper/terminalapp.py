import requests
from bs4 import BeautifulSoup

def usdt():
    url = 'https://wise.com/gb/currency-converter/usd-to-try-rate?amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try_amount_element = soup.find('span', class_='text-input')
    if try_amount_element:
        try_amount = try_amount_element.find('input')['value']
    else:
        try_amount = 'Bilgi Bulunamadı'
    exchange_rate_element = soup.find('span', class_='text-success')
    exchange_rate = exchange_rate_element.text.strip() if exchange_rate_element else 'Bilgi Bulunamadı'

    print(f"1.00 USDT = {exchange_rate} TRY")

def azn():
    url = 'https://wise.com/gb/currency-converter/azn-to-try-rate?amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try_amount_element = soup.find('span', class_='text-input')
    if try_amount_element:
        try_amount = try_amount_element.find('input')['value']
    else:
        try_amount = 'Bilgi Bulunamadı'
    exchange_rate_element = soup.find('span', class_='text-success')
    exchange_rate = exchange_rate_element.text.strip() if exchange_rate_element else 'Not Found'

    print(f"1.00 AZN = {exchange_rate} TRY")

def custom():
    custom=str(input("Enter international name of amount (For example Dollar->USDT)\n>>> "))
    url = f'https://wise.com/gb/currency-converter/{custom}-to-try-rate?amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try_amount_element = soup.find('span', class_='text-input')
    if try_amount_element:
        try_amount = try_amount_element.find('input')['value']
    else:
        try_amount = 'Bilgi Bulunamadı'
    exchange_rate_element = soup.find('span', class_='text-success')
    exchange_rate = exchange_rate_element.text.strip() if exchange_rate_element else 'Bilgi Bulunamadı'

    print(f"1.00 {custom} = {exchange_rate} TRY")


print("""
1-> USDT to TRY
2-> AZN to TRY
3-> CUSTOM
""")
currency=str(input(">>> "))

if currency=="1":
    usdt()
elif currency=="2":
    azn()
elif currency=="3":
    custom()
else:
    print("404")
