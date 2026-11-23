from selenium.webdriver.common.by import By

SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
COOKIE_ACCEPT_BUTTON = By.ID, "rcc-confirm-button"

ABOUT_RENT_TITLE = (By.XPATH, "//div[normalize-space()='Про аренду']")

ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[normalize-space()='Заказать']")
ORDER_BUTTON_HOME = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[normalize-space()='Заказать']")
ORDER_BUTTON_FORM = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[normalize-space()='Заказать']")

MOVE_ON_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")

FILL_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
FILL_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
FILL_ADRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
FILL_METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
METRO_STATION_SOKOLNIKI = (By.XPATH, "//div[normalize-space()='Сокольники']")
FILL_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")


