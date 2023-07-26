from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from time import sleep
from config import LOGIN, PASSWORD

with webdriver.Chrome() as browser:
    browser.get('https://connect.garmin.com/')
    WDW = WebDriverWait(browser, 5)
    WDW.until(EX.element_to_be_clickable((By.ID, "truste-consent-button"))).click()
    WDW.until(EX.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/header'
                                                    '/nav/ul/li[4]/a/button'))).click()
    WDW.until(EX.presence_of_element_located((By.ID, 'email'))).send_keys(LOGIN)
    WDW.until(EX.presence_of_element_located((By.ID, 'password'))).send_keys(PASSWORD)
    WDW.until(EX.element_to_be_clickable((By.XPATH, '//*[@id="portal"]/div[2]/div/div/div/div/form/section['
                                                    '2]/g-button/button'))).click()

    sleep(10)
