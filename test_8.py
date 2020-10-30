import waitings
import log_output
import login_page
import arrived_at_the_warehouse_no_sorting

'''
Тест-кейс №8. Создание блока событий 71 без курьера
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «71. Прибыл на склад (без сортировки)» - 
        Открылась форма «Ввод данных о блоке»
4) Нажать кнопку «Продолжить без курьера» - 
    Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
'''

def test_8():
    log_output.Print('Тест 8')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 8 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.check_menu(driver)

    if result == 'ERROR':
        log_output.Print('Тест 8 не пройден')
    else:
        log_output.Print('Тест 8 пройден')

    waitings.visual_checking()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()

if __name__ == "__main__":
    test_8()