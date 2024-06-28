import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service('D:/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get('https://oxylabs.io/blog')

results = []
more_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs='oxy-4x8s2x e1c11dfq0'):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='oxy-1hhb85i e1b0cevj0'):
    date = b.find('p')
    if date not in more_results:
        more_results.append(date.text)

df = pd.DataFrame({'Name': results, 'Dates': more_results})
a = df.to_csv('names.csv', index=False, encoding='utf-8')
