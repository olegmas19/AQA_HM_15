import pytest
from selene import browser, be

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(params=[(1280, 720), (1400, 600), (1920, 1080)])
def browser_options_desktop(request):
    browser.open('https://github.com/')
    width, height = request.param
    browser.driver.set_window_size(width, height)
    yield
    browser.quit()

@pytest.fixture(params=[(414, 890), (439, 932), (375, 667)])
def browser_options_mobile(request):
    width, height = request.param
    browser.driver.set_window_size(width, height)
    yield
    browser.quit()


def test_github_desktop(browser_options_desktop):
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()

def test_github_mobile(browser_options_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-content').should(be.visible).click()
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()
