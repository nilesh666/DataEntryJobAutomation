from main import all_address,all_links,all_price
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

d = webdriver.Chrome(options=chrome_options)

for i in range(len(all_links)):
    d.get(
        "Form Link Here")
    time.sleep(2)
    top = d.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    middle = d.find_element(By.XPATH,
                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bottom = d.find_element(By.XPATH,
                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = d.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    top.send_keys(all_address[i])
    middle.send_keys(all_price[i])
    bottom.send_keys(all_links[i])
    submit.click()

