from selenium.webdriver.common.by import By

SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
COOKIE_ACCEPT_BUTTON = By.ID, "rcc-confirm-button"

ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[normalize-space()='Заказать']")
ORDER_BUTTON_HOME = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[normalize-space()='Заказать']")
ORDER_BUTTON_FORM = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[normalize-space()='Заказать']")

MOVE_ON_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")

FAQ_SUBHEADER = (By.XPATH, "//div[text()='Вопросы о важном']")
QUESTION_1 = (By.XPATH, "(//div[@class='accordion__button'])[1]")
QUESTION_2 = (By.XPATH, "(//div[@class='accordion__button'])[2]")
QUESTION_3 = (By.XPATH, "(//div[@class='accordion__button'])[3]")
QUESTION_4 = (By.XPATH, "(//div[@class='accordion__button'])[4]")
QUESTION_5 = (By.XPATH, "(//div[@class='accordion__button'])[5]")
QUESTION_6 = (By.XPATH, "(//div[@class='accordion__button'])[6]")
QUESTION_7 = (By.XPATH, "(//div[@class='accordion__button'])[7]")
QUESTION_8 = (By.XPATH, "(//div[@class='accordion__button'])[8]")

ANSWER_1 = (By.XPATH, "(//div[@class='accordion__panel']/p)[1]")
ANSWER_2 = (By.XPATH, "(//div[@class='accordion__panel']/p)[2]")
ANSWER_3 = (By.XPATH, "(//div[@class='accordion__panel']/p)[3]")
ANSWER_4 = (By.XPATH, "(//div[@class='accordion__panel']/p)[4]")
ANSWER_5 = (By.XPATH, "(//div[@class='accordion__panel']/p)[5]")
ANSWER_6 = (By.XPATH, "(//div[@class='accordion__panel']/p)[6]")
ANSWER_7 = (By.XPATH, "(//div[@class='accordion__panel']/p)[7]")
ANSWER_8 = (By.XPATH, "(//div[@class='accordion__panel']/p)[8]")



FILL_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
FILL_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
FILL_ADRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
FILL_METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
METRO_STATION_SOKOLNIKI = (By.XPATH, "//div[normalize-space()='Сокольники']")
FILL_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")

ABOUT_RENT_TITLE = (By.XPATH, "//div[normalize-space()='Про аренду']")
FILL_DELIVERY_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
DELIVERY_DATE_21 = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--025') and not(contains(@class, 'outside-month'))]")
RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder' and normalize-space()='* Срок аренды']")
RENT_PERIOD_ONE_DAY_OPTION = (By.XPATH, "//div[@role='option' and normalize-space()='сутки']")
SCOOTER_COLOR_BLACK = (By.ID, "black")
FILL_COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

CONFIRM_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Хотите')]")
ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')][.//div[contains(text(), 'Хотите оформить заказ?')]]//button[normalize-space()='Да']")

ORDER_SUCCESS_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]")
CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
