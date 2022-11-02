from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# 获得浏览器驱动
driver = webdriver.Chrome()

# 打开需要访问的 web 页面
driver.get("https://www.baidu.com")

# set_windows_size 设置浏览器的宽和高
driver.set_window_size(900, 800)

# maximize_window() 浏览器最大化
# driver.maximize_window()

# 用 id 定位，send_keys 给操作对象输入文本信息
# driver.find_element_by_id("kw").send_keys("辛德勒的名单")

# 用 name 定位
# driver.find_element_by_name("wd").send_keys("生命之书")

# 用 class 定位
# driver.find_element_by_class_name("s_ipt").send_keys("卢旺达饭店")

# link text 适用于可点击的链接
# driver.find_element_by_link_text("新闻").click()

# partial_link_text 适用于链接的部分内容
# driver.find_element_by_partial_link_text("新").click()

# tag name 组成元素的 tag
# driver.find_element_by_tag_name("input").send_keys("测试")
# driver.find_element_by_tag_name("input").click()

# by_xpath 定位 复制前端的 xpath 位置就好了，每个元素的 xpath 都是唯一的
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("雪中")
# driver.find_element_by_xpath("//*[@id='kw']").click()

# css_selector 来定位元素，也是复制 selector 就行了
driver.find_element_by_css_selector("#kw").send_keys("测试")
driver.find_element_by_css_selector("#kw").click()

# click 表示点击的意思
# driver.find_element_by_id("su").click()

# text 表示输出文本
# text = driver.find_element_by_id("bottom_layer").text
# print("--------------------------------")
# print(text)
# print("---------------------------------")

# title 就是输出标题
# title = driver.title
# print(title)

# current_url 输出 url
# url = driver.current_url
# print(url)

# submit 表示提交的意思，提交表单
driver.find_element_by_id("su").submit()
time.sleep(3)

# back 就是浏览器后退
driver.back()

# forward 就是浏览器前进
driver.forward()

# time.sleep 表示固定等待
time.sleep(5)

# 浏览器滚动条的控制
# js1 = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js1)
# time.sleep(3)

# js2 = "var q=document.documentElement.scrollTop=0"
# driver.execute_script(js2)
# time.sleep(3)

# 键盘事件
# send_keys(Keys.TAB) # TAB
# send_keys(Keys.ENTER) # 回车
# send_keys(Keys.SPACE) # 空格
# send_keys(Keys.ESCAPE) # 回退键 esc

# 清除已有账号的登录信息
driver.find_element_by_id("account").clear()
driver.find_element_by_id("password").clear()

# 使用 tab 键把焦点定位到用户名
driver.find_element_by_id("account").send_keys(Keys.TAB)

# 就是 Ctrl + a 全选
driver.find_element_by_id("account").send_keys(Keys.CONTROL, 'a')

# 就是 Ctrl + x 剪贴
driver.find_element_by_id("account").send_keys(Keys.CONTROL, 'x')

b = driver.find_element_by_id("su")
# 双击
ActionChains(driver).double_click(b).perform()

# 右击
ActionChains(driver).context_click(b).perform()

# driver.implicitly_wait() 表示只能等待，等待的元素出现了，就不等了
# driver.implicitly_wait(5)

# clear 清除文本对象输入的文本内容
driver.find_element_by_css_selector("#kw").clear()

time.sleep(3)
driver.quit()

