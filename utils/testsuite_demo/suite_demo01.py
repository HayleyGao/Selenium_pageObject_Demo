import unittest
from TestCases import test_demo01

# test suite demo.

suite = unittest.TestSuite()
suite.addTest(test_demo01.TestLogin("test_01"))  # 将指定的方法添加

# 实例化运行对象
runner = unittest.TextTestRunner()
runner.run(suite)
