# 上传文件
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "file:///" + os.path.abspath("D:\Users\\18178\Desktop\JavaEE\HTML\src\\test.html")
driver.get(url)
time.sleep(3)

# send_keys 当中是绝对路径
driver.find_element_by_name("file").send_keys("D:\下载\《乔治湖，自由习作》.jpg")

time.sleep(3)
driver.quit()