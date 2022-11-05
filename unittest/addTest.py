import HTMLTestRunner
import sys

from selenium import webdriver
import unittest
import time
import os

import main

# 用例的执行顺序  0~9  A~Z  a~z
# 忽略测试用例的执行 @unittest.skip("skipping")

# addTest 就是把测试脚本类中的测试用例一个  一个添加到测试套件中

def creatSuit():
    # suit = unittest.TestSuite()
    # suit.addTest(main.Baidu("test_hao"))
    # suit.addTest(main.Baidu("test_hbaidu"))

    # 把一个测试脚本中所有的测试用例添加到 suit 中，使用 TestSuite
    # suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(main.Baidu))

    # 使用 TestLoader 来把脚本当中的所有测试用例添加到 suit 当中，是可以通过数组组织的
    # suit1 = unittest.TestLoader().loadTestsFromTestCase(main.Baidu)
    # suit2 = unittest.TestLoader().loadTestsFromTestCase(main.Baidu)
    # suit = unittest.TestSuite([suit1, suit2])

    # 把一个文件夹下以某种形式命名（正则表达式匹配的）的所有文件中的测试用例都加载到测试套件中
    #  通过 discover 来完成
    discovers = unittest.defaultTestLoader.discover("../unittest", pattern="main.py", top_level_dir=None)
    print(discovers)
    return discovers


    # return suit

if __name__ == "__main__":

    # 创建 HTMl 文件路径
    curpath = sys.path[0]
    print(sys.path)
    print(sys.path[0])

    # 1、创建文件夹
    if not os.path.exists(curpath+'/resultReport'):
        os.makedirs(curpath+'/resultReport')

    # 2、文件夹的命名，不能让名称重复，用时间来命名
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print(now)
    print(time.time())
    print(time.localtime(time.time()))

    # 3、文件名
    filename = curpath + '/resultReport/' + now + 'resultReport.html'

    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告",
                                                description=u"用例执行情况", verbosity=2)

    suite = creatSuit()
    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)