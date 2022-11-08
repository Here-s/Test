import csv
import sys

from ddt import data, ddt, unpack
from selenium import webdriver
import unittest
import time
import os


def getTxt(file_name):
    rows = []
    path = sys.path[0]
    with open(path+'/data/'+file_name, 'rt') as f:
        readers = csv.reader(f, delimiter='', quotechar='')
        next(readers, None)
        for row in readers:
            temprows=[]
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        print(rows)
        return rows

@ddt
class Baidu1(unittest.TestCase):

    def setUp(self):
        print("------setUp------")
        self.driver = webdriver.Chrome()
        self.url = "https://baidu.com/"
        time.sleep(3)

    def tearDown(self):
        print("-----tearDown-----")
        self.driver.quit()

    # @data("王凯", "Lisa", "马斯克", "英国王室")
    @data(['Lisa', u"Lisa_百度搜索"], [u"马斯克", u"马1斯克_百度搜索"],
          [u"英国王室", u"英国2王室_百度搜索"], [u"Lockey", u"Lockey_百度搜索"])

    # 也可以通过读文件来进行内容的测试
    # @data(*getTxt('test_baidu_data_txt))
    @unpack
    def test_baidu(self, value, expected_value):
        driver = self.driver
        driver.get(self.url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)
        try:
            self.assertEquals(expected_value, driver.title, msg="搜索结果和期望不一样")
        except:
            self.save_errorImage(driver, "error.png")
        time.sleep(6)

    def save_errorImage(self, driver, file_name):
        if not os.path.exists("./image"):
            os.makedirs("./image")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./image/" + now + "-" + file_name)
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
