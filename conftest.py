import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import FAQ_SUBHEADER, ORDER_BUTTON_HEADER, ORDER_BUTTON_HOME
from pages.login_page import LoginPage
from pages.scooter_rent_page import RentScooterPage

url = "https://qa-scooter.education-services.ru"


@pytest.fixture(scope='function')
def driver():

    browser = webdriver.Firefox()
    browser.get(url)
    
    yield browser
    browser.quit()
 
@pytest.fixture(scope= 'function') 
def page_is_visible(driver):
    
    wait = WebDriverWait(driver, 7)
    element = wait.until(EC.presence_of_element_located(FAQ_SUBHEADER))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    wait.until(EC.visibility_of_element_located(FAQ_SUBHEADER))

    
@pytest.fixture(params=[ORDER_BUTTON_HEADER, ORDER_BUTTON_HOME], ids=["header", "home"])
def rent_step(driver):
    customer_step = LoginPage(driver)
    customer_step.click_order_button()
    customer_step.login()
    return RentScooterPage(driver)