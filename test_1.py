import login_page
import pytest

'''
Тест-кейс №1. Вход существующего пользователя в систему
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
'''

def test_1():
    driver = login_page.login()

    login_page.check_enty(driver)

    driver.close()