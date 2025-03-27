import pytest
from selene import browser, be

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

mobile_size_1 = (414, 896)
mobile_size_2 = (430, 932)
desktop_size_1 = (1280, 720)
desktop_size_2 = (640, 360)

@pytest.fixture(params=[mobile_size_1, mobile_size_2, desktop_size_1, desktop_size_2])
def browser_options_desktop(request):

    pass


def test_github_desktop(browser_options_desktop):
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()


def test_github_mobile(browser_options_desktop):
    browser.element('.Button-content').should(be.visible).click()
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()
