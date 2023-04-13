import unittest
from unittest import TestSuite
from libs.HTMLTestRunner import HTMLTestRunner
from TestCases.test_login import TestLogin
import time
import os

# 参考文档
# http://study.yali.edu.cn/pythonhelp/library/unittest.html
# https://www.cnblogs.com/jodie2019/p/11958461.html

# 批量添加cases
discover = unittest.TestLoader().discover(
    start_dir=r'/Users/hayleygao/PycharmProjects/Selenium_pageObject_Demo/TestCases', pattern='test*.py')

if __name__ == '__main__':
    fp = r'/Users/hayleygao/PycharmProjects/Selenium_pageObject_Demo/report/result_' + str(time.time()) + '.html'
    with open(fp, 'wb') as filename:
        # HTMLTestRunner(stream = sys.stdout, verbosity = 1, title = None, description = None)
        runner = HTMLTestRunner(stream=filename, verbosity=2,title='test_repost', description='case 执行情况。')
        runner.run(discover)
