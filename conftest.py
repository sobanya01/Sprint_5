import pytest
from selenium import webdriver
import uuid as u
import random


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)

    yield chrome_driver

    chrome_driver.quit()


domains = ["ya.ru", "mail.ru", "gmail.com", "hotmail.com"]


@pytest.fixture
def email_generator():
    name = str(u.uuid4())[:10]

    domain = random.choice(domains)

    return f"{name}@{domain}"

wrong_domains = ["ya", "ru", "@ya", "@ru", ".", "", "_ru"]

@pytest.fixture
def wrong_email_generator():
    name = str(u.uuid4())[:10]

    domain = random.choice(wrong_domains)

    return f"{name}{domain}"