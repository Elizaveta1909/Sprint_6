from selenium.webdriver.common.by import By

SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
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
ORDER_BUTTON_FORM = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[normalize-space()='Заказать']")
