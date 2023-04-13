import unittest
from PageObjects.login import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print('starting...')

    def tearDown(self) -> None:
        print('finished!')

    def home_page(self):
        assert 1 == 1

    def test_correct_username_pwd(self):
        assert 1 != 2

    def test_correct_username_worry_pwd(self):
        assert 'a' == 'a'


if __name__ == "__main__":
    unittest.main()
