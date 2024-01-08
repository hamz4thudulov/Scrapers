import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

url = 'https://tr.wikipedia.org/wiki/Ana_Sayfa'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
target_td = soup.find('td', {'id': 'mp-bm'})

if target_td:
    content = str(target_td)
    img_folder = 'img'
    os.makedirs(img_folder, exist_ok=True)
    today = datetime.today().strftime('%d-%m-%Y')
    img_path = os.path.join(img_folder, f'{today}.png')
    
    # Tüm bağlantıların başına "https://www.wikipedia.org/" eklemek
    content = content.replace('href="/wiki/', 'href="https://www.wikipedia.org/wiki/')
    
    photo_url = target_td.find('img')['src']
    photo_response = requests.get(urljoin(url, photo_url))
    
    with open(img_path, 'wb') as photo_file:
        photo_file.write(photo_response.content)
    
    html_path = f'{today}.html'
    
    with open(html_path, 'w', encoding='utf-8') as file:
        updated_content = content.replace(photo_url, img_path)
        updated_content = f"""
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>
            <h1>Günlük Bilgi</h1>
            <body>
                {updated_content}
                <br><br><br><br><br><br><br><br><br><br><br><br><br><p>Made by Hudul0v</p>
            </body>
        </html>
        """       
        file.write(updated_content)
    
    print(f"İçerik ve fotoğraf {html_path} ve {img_path} dosyalarına kaydedildi.")
else:
    print("Belirtilen <td> etiketi bulunamadı.")
