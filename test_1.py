import login_page
import waitings
import log_output

'''
Тест-кейс №1. Вход существующего пользователя в систему
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
'''

def test_1():
    log_output.Print('Тест 1')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Correct identifiers':
        log_output.Print('Тест 1 пройден')
    else:
        log_output.Print('Тест 1 не пройден')

    waitings.visual_checking()
    driver.close()


if __name__ == "__main__":
    test_1()
