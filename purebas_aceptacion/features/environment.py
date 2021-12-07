# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from unittest import TestCase


@fixture
def browser_chrome(context):
    context.driver = Chrome()
    context.url = 'http://192.168.33.10:8000/principal/'
    context.test = TestCase()
    context.driver.get(context.url)
    #yield context.driver
    #context.driver.quit()
    
  
def before_all(context):
    use_fixture(browser_chrome, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.