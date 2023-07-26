from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from time import sleep



with webdriver.Chrome() as browser:
    browser.get('https://connect.garmin.com/')
    # browser.find_element().send_keys()
    WebDriverWait(browser, 5).until(EX.element_to_be_clickable((By.ID, "truste-consent-button"))).click()
    WebDriverWait(browser, 5).until(EX.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/header'
                                                                          '/nav/ul/li[4]/a/button'))).click()
    el = WebDriverWait(browser, 5).until(EX.presence_of_element_located((By.ID, 'email'))).send_keys('genchez@rambler.ru')
    # el.send_keys('genchez@rambler.ru')
    # browser.find_element(By.ID, 'email').send_keys('genchez@rambler.ru')

    sleep(3)
