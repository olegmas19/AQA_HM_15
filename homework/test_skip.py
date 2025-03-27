import pytest
from selene import browser, be

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


@pytest.fixture(params=[(1280, 720), (1400, 600), (1920, 1080), (414, 890), (439, 932), (375, 667)])
def browser_options_desktop(request):
    browser.open('https://github.com/')
    width, height = request.param
    browser.driver.set_window_size(width, height)
    if width <= 439:
        yield 'mobile'
        browser.quit()
    else:
        yield 'desktop'
        browser.quit()


def test_github_desktop(browser_options_desktop):
    if browser_options_desktop == 'mobile':
        pytest.skip(reason='Разрешение браузера для моб.устройств')
    else:
        browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()


def test_github_mobile(browser_options_desktop):
    if browser_options_desktop == 'desktop':
        pytest.skip(reason='Разрешение браузера десктопное')
    else:
        browser.element('.Button-content').should(be.visible).click()
        browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()
