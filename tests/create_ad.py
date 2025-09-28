import pytest
from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *


class TestCreateAd:
    # Cоздание объявления авторизованным пользователем
    def test_create_ad_as_authorized_user(self, driver):
        # Раз нельзя использовать условия, придется создавать объявление нового пользователя
        driver.get(url)
        driver.find_element(*SIGN_UP_BUTTON).click()
        Wait(driver, 5).until(EC.visibility_of_element_located(NO_ACCOUNT_BUTTON))
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        Wait(driver, 5)
        Wait(driver, 5).until(EC.visibility_of_element_located(SIGNUP_EMAIL_INPUT))
        driver.find_element(*SIGNUP_EMAIL_INPUT).send_keys(email_generator())
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*PASSWORD_SUBMIT_INPUT).send_keys(password)
        driver.find_element(*MAKE_ACCOUNT_BUTTON).click()
        # Нажать кнопку "Разместить объявление".
        Wait(driver, 5).until(EC.visibility_of_element_located(AVATAR_BUTTON))
        driver.find_element(*POST_AN_AD_BUTTON).click()
        # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        Wait(driver, 5).until(EC.visibility_of_element_located((PRODUCT_NAME)))
        driver.find_element(*PRODUCT_NAME).send_keys(product_name)
        driver.find_element(*PRODUCT_DESCRIOTION).send_keys(product_description)
        driver.find_element(*PRODUCT_PRICE).send_keys(product_price)
        # Выбрать из Dropdown «Категорию» и «Город».
        driver.find_element(*CATEGORIES).click()
        Wait(driver, 5).until(EC.visibility_of_element_located((CATEGORY)))
        driver.find_element(*CATEGORY).click()
        driver.find_element(*CITIES).click()
        Wait(driver, 5).until(EC.visibility_of_element_located((SELECT_CITY)))
        driver.find_element(*SELECT_CITY).click()
        # Выбрать RabioButton «Состояние товара».
        driver.find_element(*PRODUCT_STATUS).click()
        # Нажать кнопку «Опубликовать».
        driver.find_element(*POST_BUTTON).click()
        # Перейти в профиль пользователя.
        Wait(driver, 5).until(EC.element_to_be_clickable((AVATAR_BUTTON)))
        driver.find_element(*AVATAR_BUTTON).click()
        # Проверить: в блоке «Мои объявления» отображается созданное объявление.
        Wait(driver, 5).until(EC.visibility_of_element_located((MY_POSTS)))
        Wait(driver, 5).until(EC.visibility_of_element_located((POST)))
        assert driver.find_element(*POST).is_displayed()

    # Создание объявления неавторизованным пользователем
    def test_create_ad_as_unauthorized_user(self, driver):
        driver.get(url)
        # Нажать кнопку «Разместить объявление».
        driver.find_element(*POST_AN_AD_BUTTON).click()
        # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        Wait(driver, 5).until(EC.visibility_of_element_located((LOGIN_TO_POST_POPUP)))
        assert driver.find_element(*LOGIN_TO_POST_POPUP).is_displayed()
