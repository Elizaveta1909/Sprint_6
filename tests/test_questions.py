import pytest
import allure
from data import FAQ


class TestQuestions:

    @allure.title('Проверка отображения ответов на вопросы')
    @pytest.mark.parametrize("number, expected_text", FAQ)
    def test_get_answer(self, questions_page, number, expected_text):
        questions_page.open_question(number)
        assert questions_page.get_answer(number) == expected_text