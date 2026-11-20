from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SCOOTER_LOGO, COOKIE_ACCEPT_BUTTON, ORDER_BUTTON_HEADER, FILL_NAME, FILL_SURNAME, FILL_ADRESS, FILL_METRO, FILL_PHONE, MOVE_ON_BUTTON, ABOUT_RENT_TITLE, METRO_STATION_SOKOLNIKI

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)
        
    def click_order_button(self, locator=ORDER_BUTTON_HEADER):
        self.wait.until(EC.visibility_of_element_located(SCOOTER_LOGO))
        button = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
               
        #self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_HEADER)).click()
        
    def login(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(FILL_NAME)).send_keys('Алиса')
        self.wait.until(EC.visibility_of_element_located(FILL_SURNAME)).send_keys('Практиковна')
        self.wait.until(EC.visibility_of_element_located(FILL_ADRESS)).send_keys('Москва')
        self.wait.until(EC.visibility_of_element_located(FILL_METRO)).click()
        self.wait.until(EC.visibility_of_element_located(METRO_STATION_SOKOLNIKI)).click()
        self.wait.until(EC.visibility_of_element_located(FILL_PHONE)).send_keys('+79999991122')
        
        self.wait.until(EC.element_to_be_clickable(MOVE_ON_BUTTON)).click()
        return self.wait.until(EC.visibility_of_element_located(ABOUT_RENT_TITLE)).text
        
        
        
        