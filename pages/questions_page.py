from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import  QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5, QUESTION_6, QUESTION_7, QUESTION_8
from locators import COOKIE_ACCEPT_BUTTON, ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7, ANSWER_8

class MainQuestionsPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)
        
        
    def set_question_1(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_1)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_1)).text
        
    def set_question_2(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_2)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_2)).text  
            
    def set_question_3(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_3)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_3)).text
            
    def set_question_4(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_4)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_4)).text
            
    def set_question_5(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_5)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_5)).text
            
    def set_question_6(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_6)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_6)).text
            
    def set_question_7(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_7)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_7)).text
    
    def set_question_8(self):
        self.wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(QUESTION_8)).click()
        return self.wait.until(EC.visibility_of_element_located(ANSWER_8)).text
                