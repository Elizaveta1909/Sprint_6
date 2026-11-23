import allure
from pages.login_page import LoginPage

class TestQuestionsList:
    
    @allure.title('Проверка заполнения формы "Для кого самокат"')
    def test_login(self, driver):
            login = LoginPage(driver)
            login.click_order_button()
            login.login()
            assert login.is_about_rent_title_visible  #Убедились что успешно авторизовались и переходим на следующую страницу регистрации
            