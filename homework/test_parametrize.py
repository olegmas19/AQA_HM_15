import pytest
from selene import browser, be

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

@pytest.fixture(params=[(1280, 720), (1400, 600), (1920, 1080), (414, 890), (439, 932), (375, 667)])
def browser_options(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize("browser_options", [(1280, 720), (1400, 600), (1920, 1080)], indirect=True)
def test_github_desktop(browser_options):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()

@pytest.mark.parametrize("browser_options", [(414, 890), (439, 932), (375, 667)], indirect=True)
def test_github_mobile(browser_options):
    browser.open('https://github.com/')
    browser.element('.Button-content').should(be.visible).click()
    browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()
