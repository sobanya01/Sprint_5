import pytest
from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    # Login пользователя
    def test_login_succes(self, driver):
        driver.get(url)
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*SIGN_UP_BUTTON).click()
        # Заполнить все поля формы авторизации и нажать кнопку «Войти».
        Wait(driver, 3).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        Wait(driver, 3).until(EC.visibility_of_element_located(AVATAR_BUTTON))
        assert driver.find_element(*AVATAR_BUTTON).is_displayed()
        assert driver.find_element(*USERS_NAME_BUTTON).is_displayed()
        assert driver.find_element(*USERS_NAME_BUTTON).text == "User."
        assert driver.current_url == url  # на сайте ошибка, будет /login
