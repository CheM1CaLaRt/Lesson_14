from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Путь к драйверу ChromeDriver
driver_path = 'путь_к_драйверу/chromedriver.exe'

# Создание экземпляра драйвера
driver = webdriver.Chrome(service=Service(driver_path))

# URL страницы для парсинга
url = "https://www.divan.ru/category/svet"

# Открытие страницы
driver.get(url)

# Подождать, пока страница полностью загрузится
time.sleep(5)

# Нахождение всех элементов с информацией о светильниках
lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

# Создание списка для хранения данных
data = []

# Парсинг информации о каждом светильнике
for light in lights:
    name = light.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
    price = light.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
    url = light.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    data.append({'name': name, 'price': price, 'url': url})

# Закрытие браузера
driver.quit()

# Создание DataFrame из данных
df = pd.DataFrame(data)

# Сохранение DataFrame в CSV файл
df.to_csv('светильники.csv', index=False, encoding='utf-8-sig')

print("Данные успешно сохранены в CSV файл.")