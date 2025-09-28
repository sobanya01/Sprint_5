import pytest
from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *


class TestSignUp:

    # Регистрация пользователя
    def test_signup_success(self, driver):
        driver.get(url)
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*SIGN_UP_BUTTON).click()
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        # Заполнить все поля формы регистрации.
        driver.find_element(*SIGNUP_EMAIL_INPUT).send_keys(email_generator)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*PASSWORD_SUBMIT_INPUT).send_keys(password)
        # Нажать кнопку «Создать аккаунт».
        driver.find_element(*MAKE_ACCOUNT_BUTTON).click()
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert driver.current_url == url  # на сайте ошибка, будет /login
        assert driver.find_element(*AVATAR_BUTTON).is_displayed()
        assert driver.find_element(*USERS_NAME_BUTTON).is_displayed()
        assert driver.find_element(*USERS_NAME_BUTTON).text == "User."

    # Регистрация существующего пользователя
    def test_signup_with_existing_user(self, driver):
        driver.get(url)
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*SIGN_UP_BUTTON).click()
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        # Заполнить все поля формы регистрации данными уже существующего в системе пользователя и нажать кнопку «Создать аккаунт».
        driver.find_element(*SIGNUP_EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*PASSWORD_SUBMIT_INPUT).send_keys(password)
        # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        driver.find_element(*MAKE_ACCOUNT_BUTTON).click()
        Wait(driver, 3).until(EC.presence_of_element_located(ERROR_EMAIL_INPUT))

        assert driver.find_element(*ERROR_EMAIL_INPUT).is_displayed()
        assert driver.find_element(*ERROR_PASSWORD_INPUT).is_displayed()
        assert driver.find_element(*ERROR_PASSWORD_CONFIRM_INPUT).is_displayed()
        assert driver.find_element(*ERROR_MESSAGE_EMAIL_INPUT).text == "Ошибка"

    # Регистрация пользователя c email не по маске  *******@*******.***
    def test_signup_with_invalid_email(self, driver):
        driver.get(url)
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*SIGN_UP_BUTTON).click()
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        # Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
        driver.find_element(*SIGNUP_EMAIL_INPUT).send_keys(wrong_email_generator)
        driver.find_element(*MAKE_ACCOUNT_BUTTON).click()

        Wait(driver, 3).until(EC.presence_of_element_located(ERROR_EMAIL_INPUT))
        # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        assert driver.find_element(*ERROR_EMAIL_INPUT).is_displayed()
        assert driver.find_element(*ERROR_PASSWORD_INPUT).is_displayed()
        assert driver.find_element(*ERROR_PASSWORD_CONFIRM_INPUT).is_displayed()
        assert driver.find_element(*ERROR_MESSAGE_EMAIL_INPUT).text == "Ошибка"
