import time

from behave import step
from selenium import webdriver

@step("Navigate to Google")
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(3)