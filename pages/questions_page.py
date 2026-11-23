import allure
from pages.base_page import BasePage
from locators.questions_locators import FAQ_SUBHEADER, QUESTIONS, ANSWERS


class MainQuestionsPage(BasePage):

    @allure.step('Проскролить вниз до вопросов')
    def scroll_to_faq(self):
        self.scroll_to(FAQ_SUBHEADER)
        self.find_visible(FAQ_SUBHEADER)

    @allure.step('Раскрыть вопрос')
    def open_question(self, n):
        self.js_click(QUESTIONS[n - 1])

    @allure.step('Получить текст ответа')
    def get_answer(self, n):
        return self.get_text(ANSWERS[n - 1])