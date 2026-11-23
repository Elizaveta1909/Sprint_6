from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import SCOOTER_LOGO, YANDEX_LOGO, COOKIE_ACCEPT_BUTTON


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
    
    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def scroll_and_click(self, locator):
        self.scroll_to(locator)
        self.click(locator)

    def type_text(self, locator, text):
        self.find_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def wait_url_contains(self, part):
        self.wait.until(EC.url_contains(part))

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def accept_cookies(self):
        self.click(COOKIE_ACCEPT_BUTTON)

    def go_to_main_page(self):
        self.click(SCOOTER_LOGO)

    def go_to_yandex_page(self):
        self.click(YANDEX_LOGO)
        self.switch_to_last_window()
        self.wait_url_contains("ya.ru")