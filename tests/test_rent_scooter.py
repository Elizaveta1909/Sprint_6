from pages.scooter_rent_page import RentScooterPage
from data import BASE_URL
import allure

class TestRentScooter:
    
    @allure.title('Проверка заполнения формы "Про аренду"')
    def test_fill_scooter_info_to_rent(self, rent_step):
        rent_step.fill_delivery_data()
        assert "Заказ оформлен" in rent_step.get_success_text()
        
    @allure.title('Проверка кликабельности логотипа "Самокат"')
    def test_go_to_main_page(self, driver):
        page = RentScooterPage(driver)
        assert page.get_current_url() == BASE_URL
        
    @allure.title('Проверка кликабельности логотипа "Яндекс"')
    def test_go_to_yandex_page(self, driver):
        page = RentScooterPage(driver)
        page.go_to_yandex_page()
        assert "ya.ru" in page.get_current_url()
