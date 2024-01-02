from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options


driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

el1 = driver.find_element('id', 'id1')

el2 = driver.find_element('xpath', "/html/body/h1[1]")
el3 = driver.find_element('xpath', '//tag[@type  = "value"]')
el4 = driver.find_element('xpath', '//tag[text()  = "value"]')

el5 = driver.find_element('tag name', "value")

el5 = driver.find_element('link text', 'download felan text')



