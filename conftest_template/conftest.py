# Файл с фикстурами (функциями настроек PyTest)
# Фикстуры автоматически будут импортироваться из него в файлы с тестами
# При наличии файла conftest.py в поддиректориях могут возникать коллизии,
# связанные с переопределением фикстур!

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # ---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    # -------------------------------------------------------------------
    yield browser
    print("\nquit browser..")
    browser.quit()