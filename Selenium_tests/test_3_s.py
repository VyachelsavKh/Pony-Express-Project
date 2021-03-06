import login_page
import paths_s
import time
import pytest

'''
Тест-кейс №3. Попытка входа несуществующего пользователя в систему
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя, не заведенный в системе, в поле для логина, произвольный непустой пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Система вернула ошибку Неправильный логин или пароль
'''

def test_3():
    driver = login_page.login(paths_s.wrong_enter_login, paths_s.wrong_enter_password)

    time.sleep(0.5)

    login_page.check_non_entry(driver)

    driver.close()