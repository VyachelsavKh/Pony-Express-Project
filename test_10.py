import waitings
import time
import log_output
import login_page
import arrived_at_the_warehouse_no_sorting

'''
Тест-кейс №10. Проверка ввода некорректного номера накладной в блок событий 71
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «71. Прибыл на склад (без сортировки)» - 
        Открылась форма «Ввод данных о блоке»
4) Нажать кнопку «Продолжить без курьера» - 
    Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
5) В поле ввода «Номер объекта» ввести текст «11-1111-1112» и нажать кнопку Enter - 
    Поле ввода стало красным
'''

def test_10():
    log_output.Print('Тест 10')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 10 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.check_menu(driver)

    if result == 'ERROR':
        log_output.Print('Тест 10 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    name = '11-1111-1112'

    result = arrived_at_the_warehouse_no_sorting.enter_object_number(driver, name)

    if result == 'ERROR':
        log_output.Print('Тест 10 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    time.sleep(1)

    back_ground_colour = arrived_at_the_warehouse_no_sorting.check_colour(driver)

    if back_ground_colour == 'background-color: rgb(194, 48, 48);':
        log_output.Print('Рамка стала красной')
        log_output.Print('Тест 10 пройден')
    else:
        log_output.Print('Рамка стала другого цвета')
        log_output.Print('Тест 10 не пройден')

    waitings.visual_checking()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()
    return

if __name__ == "__main__":
    test_10()