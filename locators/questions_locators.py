from selenium.webdriver.common.by import By

COOKIE_ACCEPT_BUTTON = By.ID, "rcc-confirm-button"

FAQ_SUBHEADER = (By.XPATH, "//div[text()='Вопросы о важном']")

QUESTION_1 = (By.XPATH, "(//div[@class='accordion__button'])[1]")
QUESTION_2 = (By.XPATH, "(//div[@class='accordion__button'])[2]")
QUESTION_3 = (By.XPATH, "(//div[@class='accordion__button'])[3]")
QUESTION_4 = (By.XPATH, "(//div[@class='accordion__button'])[4]")
QUESTION_5 = (By.XPATH, "(//div[@class='accordion__button'])[5]")
QUESTION_6 = (By.XPATH, "(//div[@class='accordion__button'])[6]")
QUESTION_7 = (By.XPATH, "(//div[@class='accordion__button'])[7]")
QUESTION_8 = (By.XPATH, "(//div[@class='accordion__button'])[8]")

ANSWER_1 = (By.XPATH, "(//div[@class='accordion__panel']/p)[1]")
ANSWER_2 = (By.XPATH, "(//div[@class='accordion__panel']/p)[2]")
ANSWER_3 = (By.XPATH, "(//div[@class='accordion__panel']/p)[3]")
ANSWER_4 = (By.XPATH, "(//div[@class='accordion__panel']/p)[4]")
ANSWER_5 = (By.XPATH, "(//div[@class='accordion__panel']/p)[5]")
ANSWER_6 = (By.XPATH, "(//div[@class='accordion__panel']/p)[6]")
ANSWER_7 = (By.XPATH, "(//div[@class='accordion__panel']/p)[7]")
ANSWER_8 = (By.XPATH, "(//div[@class='accordion__panel']/p)[8]")

QUESTIONS = [(By.XPATH, f"(//div[@class='accordion__button'])[{i}]") for i in range(1, 9)]
ANSWERS = [(By.XPATH, f"(//div[@class='accordion__panel']/p)[{i}]") for i in range(1, 9)]