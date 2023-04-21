import unittest
from TestCases import test_demo01
import os
from pathlib import Path

abs_p = os.path.abspath(__file__)
print(abs_p)

pp = Path(__file__)
print(pp.parent.parent.parent)

ppp = os.path.join(pp.parent.parent.parent, 'TestCases')
print(ppp)

# Selenium_pageObject_Demo/TestCases

# test loader demo.
# TestLoader是对TestSuite的补充。


# 实例化loader对象
loader = unittest.TestLoader()
suite = loader.discover(ppp, 'test*.py')  # 指定目录，批量添加

# 实例化运行对象
runner = unittest.TextTestRunner()
runner.run(suite)
