import allure
from pages.base_page import BasePage
from locators.login_locators import SCOOTER_LOGO, ORDER_BUTTON_HEADER, FILL_NAME, FILL_SURNAME, FILL_ADRESS, FILL_METRO, FILL_PHONE, MOVE_ON_BUTTON, ABOUT_RENT_TITLE, METRO_STATION_SOKOLNIKI

class LoginPage(BasePage):
    
    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self, locator=ORDER_BUTTON_HEADER):
        self.find_visible(SCOOTER_LOGO)
        self.scroll_and_click(locator)
               
    @allure.step('Заполнить форму "Для кого самокат"')    
    def login(self):
        self.accept_cookies()
        self.type_text(FILL_NAME, 'Алиса')
        self.type_text(FILL_SURNAME, 'Практиковна')
        self.type_text(FILL_ADRESS, 'Москва')
        self.click(FILL_METRO)
        self.click(METRO_STATION_SOKOLNIKI)
        self.type_text(FILL_PHONE, '+79999991122')
        self.click(MOVE_ON_BUTTON)
        
    @allure.step('Убедиться, что отображается заголовок следующей формы')   
    def is_about_rent_title_visible(self):    
        return self.find_visible(ABOUT_RENT_TITLE)
        
        
        
        