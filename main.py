import unittest
from libs.HTMLTestRunner import HTMLTestRunner
from datetime import datetime

timer = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


# 批量添加cases
suite = unittest.TestLoader().discover(
    start_dir='./TestCases', pattern='test*.py')

if __name__ == '__main__':
    fp = r'./report/result_' + timer + '.html'
    with open(fp, 'wb') as filename:
        # HTMLTestRunner(stream = sys.stdout, verbosity = 1, title = None, description = None)
        runner = HTMLTestRunner(stream=filename, verbosity=2, title='test_repost', description='case 执行情况。')
        runner.run(suite)
