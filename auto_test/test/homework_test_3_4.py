import pytest
from selenium import webdriver


@pytest.mark.githab
def test_github():
    driver = webdriver.Chrome()
    url_git = 'https://github.com/'
    driver.get(url_git)

    assert driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    assert driver.current_url == url_git


@pytest.mark.googl
def test_googl():
    driver = webdriver.Chrome()
    url_googl = 'https://www.google.com/'
    driver.get(url_googl)

    assert driver.title == "Google"
    assert driver.current_url == url_googl
