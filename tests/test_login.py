from pages.login_page import LoginPage

class TestQuestionsList:
    
    def test_login(self, driver):
            login = LoginPage(driver)
            login.click_order_button()
            success_login = login.login()
            assert success_login == 'Про аренду' #Убедились что успешно авторизовались и переходим на следующую страницу регистрации
            