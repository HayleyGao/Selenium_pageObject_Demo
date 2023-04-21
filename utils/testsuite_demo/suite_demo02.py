import unittest
from TestCases import test_demo01

# test suite demo.

suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(test_demo01.TestLogin))  # 将一个类的所有方法添加

# 实例化运行对象
runner = unittest.TextTestRunner()
runner.run(suite)
