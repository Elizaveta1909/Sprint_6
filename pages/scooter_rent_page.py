import allure
from pages.base_page import BasePage
from locators.rent_locators import FILL_DELIVERY_DATE, DELIVERY_DATE_21, RENT_PERIOD_DROPDOWN, RENT_PERIOD_ONE_DAY_OPTION, SCOOTER_COLOR_BLACK, FILL_COMMENT, ORDER_BUTTON_FORM, ORDER_SUBMIT_BUTTON, ORDER_SUCCESS_TITLE
from locators.rent_locators import CONFIRM_MODAL_TITLE, SCOOTER_LOGO

class RentScooterPage(BasePage):

    @allure.step('Заполнить форму "Про аренду"')    
    def fill_delivery_data(self):
        self.click(FILL_DELIVERY_DATE)
        self.click(DELIVERY_DATE_21)
        self.click(RENT_PERIOD_DROPDOWN)
        self.click(RENT_PERIOD_ONE_DAY_OPTION)
        self.click(SCOOTER_COLOR_BLACK)
        self.type_text(FILL_COMMENT, "-")
        self.click(ORDER_BUTTON_FORM)
        self.find_visible(CONFIRM_MODAL_TITLE)
        self.click(ORDER_SUBMIT_BUTTON)
    
    @allure.step('Убедиться, что отображается текст об успешном оформлении заказа')   
    def get_success_text(self):
        return self.get_text(ORDER_SUCCESS_TITLE)

    @allure.step('Нажать на логотип "Самокат"')
    def go_to_main_page(self):
        self.click(SCOOTER_LOGO)
        
        
        