import unittest
import ddt
from common.getData import getData


@ddt.ddt
class TestDemo(unittest.TestCase):

    @ddt.data(1, 2, 4)
    def test_01(self, v):
        print(v)

    @ddt.data(getData())
    @ddt.unpack  # 当迭代的参数为多维数组时，需要使用该装饰器来解析参数
    def test_02(self, a, b):
        print(a, b)

    @ddt.data(getData())  # 迭代的参数值类型可以为字典，字典的key值需要与形参的名称一致
    @ddt.unpack
    def test_03(self, account, pwd):
        print(account, pwd)


if __name__ == "__main__":
    unittest.main()
