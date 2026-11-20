import pytest
from pages.questions_page import MainQuestionsPage


@pytest.mark.usefixtures("page_is_visible")
class TestQuestionsList:
    
    def test_get_answer_1(self, driver):
        main = MainQuestionsPage(driver)
        text_1 = main.set_question_1()
        assert text_1 == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        
    def test_get_answer_2(self, driver):
        main = MainQuestionsPage(driver)
        text_2 = main.set_question_2()
        assert text_2 == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        
    def test_get_answer_3(self, driver):
        main = MainQuestionsPage(driver)
        text_3 = main.set_question_3()
        assert text_3 == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
                      
    def test_get_answer_4(self, driver):
        main = MainQuestionsPage(driver)
        text_4 = main.set_question_4()
        assert text_4 == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
            
    def test_get_answer_5(self, driver):
        main = MainQuestionsPage(driver)
        text_5 = main.set_question_5()
        assert text_5 == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
            
    def test_get_answer_6(self, driver):
        main = MainQuestionsPage(driver)
        text_6 = main.set_question_6()
        assert text_6 == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.' 
                
    def test_get_answer_7(self, driver):
        main = MainQuestionsPage(driver)
        text_7 = main.set_question_7()
        assert text_7 == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
                
    def test_get_answer_8(self, driver):
        main = MainQuestionsPage(driver)
        text_8 = main.set_question_8()
        assert text_8 == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'