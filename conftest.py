import pytest
from selenium import webdriver
from data import BASE_URL
from pages.login_page import LoginPage
from pages.questions_page import MainQuestionsPage
from locators.questions_locators import FAQ_SUBHEADER
from locators.login_locators import ORDER_BUTTON_HEADER, ORDER_BUTTON_HOME
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.scooter_rent_page import RentScooterPage

base_url = BASE_URL


@pytest.fixture(scope='function')
def driver():

    browser = webdriver.Firefox()
    browser.get(base_url)
    
    yield browser
    browser.quit()
    
@pytest.fixture
def questions_page(driver):
    page = MainQuestionsPage(driver)
    page.accept_cookies()
    page.scroll_to_faq()
    return page
 
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