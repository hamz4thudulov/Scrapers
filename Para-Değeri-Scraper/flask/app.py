from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_exchange_rate(currency):
    url = f'https://wise.com/gb/currency-converter/{currency}-to-try-rate?amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    exchange_rate_element = soup.find('span', class_='text-success')
    exchange_rate = exchange_rate_element.text.strip() if exchange_rate_element else 'Bilgi Bulunamadı'
    return exchange_rate

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usdt')
def usdt():
    exchange_rate = get_exchange_rate('usd')
    return render_template('currency.html', currency='USDT', exchange_rate=exchange_rate)

@app.route('/azn')
def azn():
    exchange_rate = get_exchange_rate('azn')
    return render_template('currency.html', currency='AZN', exchange_rate=exchange_rate)

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    if request.method == 'POST':
        custom_currency = request.form['custom_currency']
        exchange_rate = get_exchange_rate(custom_currency.lower())
        return render_template('currency.html', currency=custom_currency.upper(), exchange_rate=exchange_rate)
    return render_template('custom.html')

if __name__ == '__main__':
    app.run(debug=True)
