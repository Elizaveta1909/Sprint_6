from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import FILL_DELIVERY_DATE, DELIVERY_DATE_21, RENT_PERIOD_DROPDOWN, RENT_PERIOD_ONE_DAY_OPTION, SCOOTER_COLOR_BLACK, FILL_COMMENT, ORDER_BUTTON_FORM, ORDER_SUBMIT_BUTTON, ORDER_SUCCESS_TITLE
from locators import CONFIRM_MODAL_TITLE, SCOOTER_LOGO, YANDEX_LOGO

class RentScooterPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    def fill_delivery_data(self):
        self.wait.until(EC.element_to_be_clickable(FILL_DELIVERY_DATE)).click()
        self.wait.until(EC.element_to_be_clickable(DELIVERY_DATE_21)).click()
        self.wait.until(EC.element_to_be_clickable(RENT_PERIOD_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(RENT_PERIOD_ONE_DAY_OPTION)).click()
        self.wait.until(EC.element_to_be_clickable(SCOOTER_COLOR_BLACK)).click()
        self.wait.until(EC.element_to_be_clickable(FILL_COMMENT)).send_keys("-")
        
        self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_FORM)).click()
        self.wait.until(EC.visibility_of_element_located(CONFIRM_MODAL_TITLE))
        self.wait.until(EC.element_to_be_clickable(ORDER_SUBMIT_BUTTON)).click()
        
        result = self.wait.until(EC.visibility_of_element_located(ORDER_SUCCESS_TITLE))
        print("Текст результата:", result.text)
        return result.text
    
    def go_to_main_page(self):
        self.wait.until(EC.element_to_be_clickable(SCOOTER_LOGO)).click()
        
        
    def go_to_yandex_page(self):
        self.wait.until(EC.element_to_be_clickable(YANDEX_LOGO)).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_contains("ya.ru"))
        
        