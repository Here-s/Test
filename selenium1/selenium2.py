# alert 提示框
import os.path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "file:///" + os.path.abspath("D:\Users\\18178\Desktop\JavaEE\HTML\src\\test.html")
driver.get(url)
time.sleep(3)

# 定位元素，点击，使得弹出框出现
driver.find_element_by_tag_name("input").click()
time.sleep(3)
alert = driver.switch_to.alert # 获得弹出框的操作句柄
alert.send_keys("Lockey")
time.sleep(3)
alert.accept()
time.sleep(3)

# 点击 click 出现弹框
driver.find_element_by_link_text("Click").click()
# 点击 div 框框里面的 click me 让弹出框内容发生变化
div1 = driver.find_element_by_class_name("model-body")
div1.find_element_by_link_text("click me").click()
time.sleep(3)

# 点击 div 再定位具体的 button
div2 = driver.find_element_by_class_name("modal-footer")
buttons = div2.find_element_by_tag_name("button")
buttons[0].click()
time.sleep(4)
driver.quit()