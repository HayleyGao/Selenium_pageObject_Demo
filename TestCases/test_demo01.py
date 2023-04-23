import unittest
from PageObjects.loginPage import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print('starting...')

    def tearDown(self) -> None:
        print('finished!')

    def test_01(self):
        assert 1 != 2

    def test_02(self):
        assert 'a' == 'a'


# if __name__ == "__main__":
#     unittest.main()
