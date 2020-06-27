import os

import pytest
import allure


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--alluredir', './report1/xml'])
    os.system("allure generate ./report1/xml -o ./report1/html")

