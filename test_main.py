import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By




@pytest.fixture()
def page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    param = request.param
    if param == 'contract':
        driver.get(' https://iccs.spbstu.ru/edu/09.03.01/09.03.01_02/ ')
    elif param == 'Информатика и вычислительная техника':
        driver.get(' https://iccs.spbstu.ru/edu/09.03.01/ ')
    return driver

@pytest.mark.parametrize('page', ['contract'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CLASS_NAME, "dropdown-toggle")
    assert title.text == 'Абитуриентам'


@pytest.mark.parametrize('page', ['Информатика и вычислительная техника'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == '09.03.01«Информатика и вычислительная техника»'














