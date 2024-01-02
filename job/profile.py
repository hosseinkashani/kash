from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# from selenium.webdriver.common.keys import Keys
# import os
# from pathlib import Path
# from selenium.webdriver.chrome.options import Options

# c_option = Options()
# c_option.add_argument("--incognito")
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)


def finder(type_operate, find_by, find_value):
    if type_operate == 'click':
        driver.find_element(find_by, find_value).click()
    elif type_operate == 'text':
        return driver.find_element(find_by, find_value).text
    else:
        driver.find_element(find_by, find_value).send_keys(type_operate)


base_url = str(input("url vared konid: "))
sleep(3)
driver.get(base_url)
driver.set_window_size(400, 1000)
driver.set_window_position(2200, 30)

sleep(2)

# finder('click', 'xpath', '//*[@id="__next"]/div[1]/header[2]/div/div/a[3]')
# sleep(1)
# finder('click', 'xpath', '//*[@id="__next"]/div[1]/main/div/div[2]/button')
# finder("09351407172", 'tag name', 'input')
# sleep(3)
# finder('click', 'xpath', '//*[@id=":r1:"]')
# sleep(3)
# finder("123456", 'xpath', "//input[@id=':rh:']")
# sleep(1)
# finder('click', 'xpath', '//*[@id=":r3:"]')
# sleep(1)
# favorite_menu = finder('text', 'xpath', '//*[@id="__next"]/div[1]/main/div/nav/div[1]/div[1]/div[2]/span/div/p')
# sleep(1)
# finder('click', 'xpath', '//*[@id="__next"]/div[1]/main/div/nav/div[1]/div[1]')
# sleep(1)
# favorite_txt = finder('text', 'xpath', '//*[@id="__next"]/div[1]/main/div/div/div/div/a/p')
# sleep(1)
# print(favorite_menu)
# print(favorite_txt)
#
# assert favorite_menu == favorite_txt
#
# driver.quit()
