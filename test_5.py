import waitings
import log_output
import login_page
import service_menu

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
    log_output.Print('Тест 5')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 5 не пройден')
        waitings.visual_checking()
        driver.close()
        return

    result = service_menu.editing_user_groups_button(driver)

    if result == 'ERROR':
        log_output.Print('Тест 5 не пройден')
    else:
        log_output.Print('Тест 5 пройден')

    waitings.visual_checking()
    driver.close()

if __name__ == "__main__":
    test_5()