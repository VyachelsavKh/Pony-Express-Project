import waitings
import log_output
import login_page
import main_page

'''
Тест-кейс №2. Выход пользователя из системы
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку выход в верхнем правом углу окна системы - 
    Пользователь вышел из системы, открылась страница «Вход в систему»
'''

def test_2():
    log_output.Print('Тест 2')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 2 не пройден')
        waitings.visual_checking()
        driver.close()
        return

    result = main_page.quit(driver)

    if result == 'ERROR':
        log_output.Print('Тест 2 не пройден')
    else:
        log_output.Print('Тест 2 пройден')

    waitings.visual_checking()
    driver.close()


if __name__ == "__main__":
    test_2()