import pytest
from selene import browser, be

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

@pytest.fixture()
def browser_options_desktop():
    pass


def test_github_desktop(browser_options_desktop):
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()


def test_github_mobile(browser_options_desktop):
    browser.element('.Button-content').should(be.visible).click()
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()
