import pytest
from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:

    # Logout пользователя
    def test_logout_success(self, driver):
        # Авторизоваться под заранее созданным пользователем.
        driver.get(url)
        driver.find_element(*SIGN_UP_BUTTON).click()
        # Заполнить все поля формы авторизации и нажать кнопку «Войти».
        Wait(driver, 3).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        Wait(driver, 3).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
        # Нажать кнопку «Выйти».
        driver.find_element(*LOGOUT_BUTTON).click()
        # Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», там теперь отображается кнопка «Вход и регистрация».
        Wait(driver, 3).until(EC.visibility_of_element_located(SIGN_UP_BUTTON))
        assert driver.find_element(*SIGN_UP_BUTTON).is_displayed()
        avatar = driver.find_elements(*AVATAR_BUTTON)
        username = driver.find_elements(*USERS_NAME_BUTTON)
        assert len(avatar) == 0
        assert len(username) == 0
