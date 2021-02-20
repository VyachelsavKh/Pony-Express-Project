import login_page
import service_menu
import pytest

'''
Тест-кейс №5. Просмотр списка групп пользователей
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» -
    В выпавшем списке доступен пункт «Сервис» - «Управление» разрешениями»
4) Выбрать пункт «Группы пользователей» - 
    Открылась форма «Редактирование групп пользователей»
'''

def test_5():
    driver = login_page.login()

    login_page.check_enty(driver)

    service_menu.editing_user_groups_button(driver)

    driver.close()