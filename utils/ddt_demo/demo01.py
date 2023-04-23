import unittest
import ddt


def func(a, b):
    x = a + b
    return x


@ddt.ddt
class TestDemo(unittest.TestCase):

    @ddt.data(1, 2, 4)
    def test_01(self, v):
        print(v)

    @ddt.data((1, 2, 3), [3, 1, 4])
    @ddt.unpack  # 当迭代的参数为多维数组时，需要使用该装饰器来解析参数
    def test_02(self, a, b, c):
        print(a,b,c)

    @ddt.data({"a":1,'b':2,'c':3}, {"a":3,'b':1,'c':5})   # 迭代的参数值类型可以为字典，字典的key值需要与形参的名称一致
    @ddt.unpack
    def test_03(self, a, b, c):
        print(a,b,c)

    def test_04(self):
        assert func(1, 2) == 3


if __name__ == "__main__":
    unittest.main()
