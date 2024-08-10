import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://svetilnik-online.ru/svetilniki-podvesnye'
driver.get(url)
time.sleep(3)

luminaries = driver.find_elements(By.CLASS_NAME, 'item')
print(luminaries)

parsed_data = []

for lumina in luminaries:
    try:
        name = lumina.find_element(By.XPATH, './/div[@class="item-content"]//p[@class="product-name"]/a').get_attribute('title')
        price = lumina.find_element(By.XPATH, './/div[@class="price-box"]//span[@class="pprice"]').text
        url = lumina.find_element(By.XPATH, './/div[@class="item-content"]//p[@class="product-name"]/a').get_attribute('href')
    except:
        print('Произощла ошибка при парсинге')
        continue
    parsed_data.append([name, price, url])

print(parsed_data)
driver.quit()

with open('selenium_pars.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование светильника', 'Цена', 'Ссылка на описание'])
    writer.writerows(parsed_data)