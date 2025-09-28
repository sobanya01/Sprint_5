from data import *
import random
import uuid as u
from selenium.webdriver.common.by import By


def email_generator():
    name = str(u.uuid4())[:10]

    domain = random.choice(domains)

    return f"{name}@{domain}"


def wrong_email_generator():
    name = str(u.uuid4())[:10]

    domain = random.choice(wrong_domains)

    return f"{name}{domain}"
