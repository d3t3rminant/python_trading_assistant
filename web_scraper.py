import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/symbols/AUDJPY/technicals/?exchange=FX")
trends = ["strong-buy", "strong-sell", "buy", "sell", "neutral"]

try:
    button_4h = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "1h")))


    container = driver.find_element(By.CLASS_NAME, "summary-kg4MJrFB")
    summary = container.find_element(By.CLASS_NAME, "container-zq7XRf30")
    #class_names = summary.get_attribute("class").split(" ")
    class_names = summary.get_attribute("class")
    print(class_names)
    for trend in trends:
        if trend in class_names:
            print("1D summary", trend)
            break

    button_4h.click()
    time.sleep(1) # Necessary in order to wait for the right class assignment. No work around found yet
    container = driver.find_element(By.CLASS_NAME, "summary-kg4MJrFB")
    summary = container.find_element(By.CLASS_NAME, "container-zq7XRf30")
    class_names = summary.get_attribute("class")
    for trend in trends:
        if trend in class_names:
            print("1H summary", trend)
            break

except TimeoutError:
    print("Element not found")
    driver.quit()






"""    #button_4h = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "4h")))
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "summary-kg4MJrFB")))
    summary = WebDriverWait(container, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "container-zq7XRf30")))"""

