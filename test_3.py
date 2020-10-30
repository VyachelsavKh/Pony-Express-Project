import login_page
import waitings
import log_output
import paths

'''
Тест-кейс №3. Попытка входа несуществующего пользователя в систему
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя, не заведенный в системе, в поле для логина, произвольный непустой пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Система вернула ошибку Неправильный логин или пароль
'''

def test_3():
    log_output.Print('Тест 1')
    driver = login_page.login(paths.wrong_enter_login, paths.wrong_enter_password)

    identifiers = login_page.check_non_entry(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 3 пройден')
    else:
        log_output.Print('Тест 3 не пройден')

    waitings.visual_checking()
    driver.close()


if __name__ == "__main__":
    test_3()