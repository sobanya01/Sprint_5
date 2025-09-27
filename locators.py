from selenium.webdriver.common.by import By

# Вход и регистрация
SIGN_UP_BUTTON = (
    By.XPATH,
    '//button[text()="Вход и регистрация"]',
)  # Кнопка Вход и регистрация

NO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]')  # Кнопка Нет аккаунта
MAKE_ACCOUNT_BUTTON = (
    By.XPATH,
    '//button[text()="Создать аккаунт"]',
)  # Кнопка Создать аккаунт (зарегистрироваться)
SIGNUP_EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
PASSWORD_SUBMIT_INPUT = (By.XPATH, '//input[@name="submitPassword"]')

ERROR_EMAIL_INPUT = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
ERROR_PASSWORD_INPUT = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
ERROR_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
ERROR_MESSAGE_EMAIL_INPUT = (By.CSS_SELECTOR, ".input_span__yWPqB")

LOGIN_EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
LOGIN_PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

AVATAR_BUTTON = (By.CSS_SELECTOR, ".circleSmall")
USERS_NAME_BUTTON = (By.CSS_SELECTOR, ".profileText.name")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

# Объявления
LOGIN_TO_POST_POPUP = (By.CSS_SELECTOR, ".popUp_shell__LuyqR")
POST_AN_AD_BUTTON = (
    By.XPATH,
    "//*[text()='Разместить объявление']",
)  # Разместить объявление
PRODUCT_NAME = By.XPATH, "//input[@name='name']"  # Название товара
PRODUCT_DESCRIOTION = By.XPATH, "//textarea[@name='description']"  # Описание товара
PRODUCT_PRICE = By.XPATH, "//input[@name='price']"  # Стоимость товара
CITIES = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]"  # Города
SELECT_CITY = (
    By.XPATH,
    "//span[text()='Санкт-Петербург']",
)  # Выбор города (Санкт-Петербург)
CATEGORIES = (
    By.XPATH,
    "(//button[contains(@class, 'dropDownMenu_arrowDown')])[1]",
)  # Категории
CATEGORY = By.XPATH, "//span[text()='Книги']"  # Выбор категории (Книги)
PRODUCT_STATUS = (
    By.XPATH,
    "//div[contains(@class, 'radioUnput_inputRegular')]",
)  # Состояние товара Б/У
POST_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")  # Кнопка "Опубликовать"
# USERS_PRODUCT_NAME_= By.XPATH, "//h2[text()='']" # Название объявления в разделе "Мои объявления"
MY_POSTS = (By.CLASS_NAME, "profile_profile__bixlA")  # мои объявления
POST = (By.XPATH, "//*[@class='about']/h2")
