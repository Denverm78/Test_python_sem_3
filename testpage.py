from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocator:

    LOCATOR_BUTTON = (By.CSS_SELECTOR, "button")
    LOCATOR_CONTACT_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PSWD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_MSG = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_TEXT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """button""")
 
    
class OperationHelper(BasePage):

    def enter_login(self, text):
        logging.info(f'Send {text} to element {TestSearchLocator.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocator.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def enter_pswd(self, text):
        logging.info(f'Send {text} to element {TestSearchLocator.LOCATOR_PSWD_FIELD[1]}')
        pswd_field = self.find_element(TestSearchLocator.LOCATOR_PSWD_FIELD)
        pswd_field.clear()
        pswd_field.send_keys(text)

    def click_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocator.LOCATOR_BUTTON).click()
    
    def get_error_msg(self):
        error_field = self.find_element(TestSearchLocator.LOCATOR_ERROR_MSG, time=3)
        text = error_field.text
        logging.info(f'We find text {text} in error field')
        return text

    def click_contact(self):
        link = self.find_element(TestSearchLocator.LOCATOR_CONTACT_FIELD)
        link.click()

    def enter_cont_name(self, text):
        cont_name_field = self.find_element(TestSearchLocator.LOCATOR_CONTACT_NAME)
        cont_name_field.clear()
        cont_name_field.send_keys(text)

    def enter_cont_email(self, text):
        cont_email_field = self.find_element(TestSearchLocator.LOCATOR_CONTACT_EMAIL)
        cont_email_field.clear()
        cont_email_field.send_keys(text)

    def enter_cont_text(self, text):
        cont_text_field = self.find_element(TestSearchLocator.LOCATOR_CONTACT_TEXT)
        cont_text_field.clear()
        cont_text_field.send_keys(text)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert.text
        return alert
