# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Chrome,ChromeOptions
from unittest import TestCase


@fixture
def browser_chrome(context):
    options = ChromeOptions();
    options.add_argument("--start-maximized");
    context.driver = Chrome(chrome_options=options)
    context.url = 'http://127.0.0.1:8000'
    context.test = TestCase()
    context.driver.get(context.url)
    
def before_all(context):
    use_fixture(browser_chrome, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.