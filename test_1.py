from testpage import OperationHelper
import time
import logging


# def test_step1(browser): # Негативный тест
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login('test') 
#     testpage.enter_pass('test')
#     testpage.click_login_button()
#     assert testpage.get_error_text() == "401"


def test_step2(browsers):
    logging.info('Test2 Starting')
# Вход с валидными данными
    test_page1 = OperationHelper(browsers)
    test_page1.go_to_site()
    test_page1.enter_login("Roman83")
    test_page1.enter_pswd("5a45102d64")
    test_page1.click_button()
    time.sleep(3)
#создание сообщения
    test_page1.click_contact()
    time.sleep(3)
#заполнение обязательных полей email
    test_page1.enter_cont_name("Роман")
    test_page1.enter_cont_email("roman78@mail.ru")
    test_page1.enter_cont_text("Текст сообщения")
    time.sleep(3)
#отправка сообщения
    test_page1.click_button()
    time.sleep(3)
#проверка факта отправления сообщения
    assert test_page1.get_alert_text() == "Form successfully submitted"
    time.sleep(1)