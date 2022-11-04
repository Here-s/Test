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
    discover = unittest.defaultTestLoader.discover("../unittest", pattern="main.py", top_level_dir=None)
    return discover


    return suit

if __name__ == "__main__":
    suit = creatSuit()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)