from pages.scooter_rent_page import RentScooterPage

class TestRentScooter:
    
    def test_fill_scooter_info_to_rent(self, rent_step):
        result = rent_step.fill_delivery_data()
        assert "Заказ оформлен" in result
        
    def test_go_to_main_page(self, driver):
        rentscooter = RentScooterPage(driver)
        rentscooter.go_to_main_page()
        assert driver.current_url == 'https://qa-scooter.education-services.ru/'
        
    def test_go_to_yandex_page(self, driver):
        rentscooter = RentScooterPage(driver)
        rentscooter.go_to_yandex_page()
        assert "ya.ru" in driver.current_url
