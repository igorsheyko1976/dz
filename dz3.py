from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome()

driver.get('https://www.divan.ru')

time.sleep(5)

prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])

    for price in prices:
        writer.writerow([price.text])

driver.quit()

def clean_price(price):
    price = price.replace('руб.', '').replace(' ', '')
    if price:
        return int(price)
    else:
        return None

input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")

file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

prices = data['Цена']

plt.hist(prices, bins=10, edgecolor='black')

plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()
