# unittest 框架

# 测试固件   setUp() 初始化测试环境的工作  tearDown() 清理环境的操作

# 测试套件   把不同测试脚本，不同类中的测试用例组织起来，放到一个测试套中执行

from selenium import webdriver
import unittest
import time
import os

# 用例的执行顺序  0~9  A~Z  a~z
# 忽略测试用例的执行 @unittest.skip("skipping")

# 通过继承 unittest.TestCase 来使用 unittest 框架
class Baidu(unittest.TestCase):
    # 测试固件
    def setUp(self):
        print("------setUp------")
        self.driver = webdriver.Chrome()
        self.url = "https://baidu.com/"
        time.sleep(3)

    def tearDown(self):
        print("-----tearDown-----")
        self.driver.quit()


    # 测试用例
    def test_hao(self):
        driver = self.driver
        url = self.url
        driver.get(url)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)

    def test_hbaidu(self):
        driver = self.driver
        url = self.url
        driver.get(url)
        # self.assertTrue("百度一下，你就知道" == driver.title, msg="不一致！！")
        driver.find_element_by_id("kw").send_keys("突如其来的疫情")
        driver.find_element_by_id("su").submit()
        time.sleep(5)

        # 断言，结果不符的时候，就会异常输出
        # assertEqual  预期结果，实际结果，异常输出
        # assertNotEqual  预期结果，实际结果，异常输出
        # assertTrue  预期结果==实际结果，异常信息
        # assertTrue  预期结果==实际结果，异常信息
        # self.assertEquals("啦啦啦", driver.title, msg="实际结果与预期不一致") # 前面是预期结果，后面是实际结果

        print(driver.title)
        try:
            self.assertNotEqual(driver.title,"突如其来的疫情_百度搜索", msg="实际结果和预期不符！！")
        except:
            self.saveScreenAsPhoto(driver, 'haohao.png')
        time.sleep(6)

    def saveScreenAsPhoto(self, driver, file_name):
        if not os.path.exists("./image"):
            os.makedirs("./image")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./image/" + now + "-" + file_name)
        time.sleep(3)


