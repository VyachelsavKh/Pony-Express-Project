import waitings
import time
import log_output
import login_page
import arrived_at_the_warehouse_no_sorting

'''
Тест-кейс №12. Проверка ввода некорректного номера накладной в блок событий 71
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «71. Прибыл на склад (без сортировки)» - 
        Открылась форма «Ввод данных о блоке»
4) Нажать кнопку «Продолжить без курьера» - 
    Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
5) В поле ввода «Номер объекта» ввести текст «11-1111-1111» и нажать кнопку Enter - 
    Номер накладной «11-1111-1111» добавлен в блок и отображается в таблице объектов
6) В списке объектов выбрать введенный номер «11-1111-1111» и нажать кнопку удалить - 
    Номер накладной «11-1111-1111» удалён из блока и не отображается в списке объектов
'''

def test_12():
    log_output.Print('Тест 12')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 12 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.check_menu(driver)

    if result == 'ERROR':
        log_output.Print('Тест 12 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    name = '11-1111-1111'

    result = arrived_at_the_warehouse_no_sorting.enter_object_number(driver, name)

    if result == 'ERROR':
        log_output.Print('Тест 12 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.check_element_11_1111_1111(driver)

    if result == name:
        log_output.Print('Накладная 11-1111-1111 была добавлена и видна')
    else:
        log_output.Print('Накладная 11-1111-1111 не была добавлена')
        log_output.Print('Тест 12 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.delete_element_11_1111_1111(driver)

    if result == 'ERROR':
        log_output.Print('Не смог удалить накладную')
        log_output.Print('Тест 12 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.check_element_11_1111_1111(driver)

    if result == name or result != 'ERROR':
        log_output.Print('Накладная 11-1111-1111 не была удалена')
        log_output.Print('Тест 12 не пройден')
    else:
        log_output.Print('Накладная 11-1111-1111 была удалена')
        log_output.Print('Тест 12 пройден')

    waitings.visual_checking()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()
    return

if __name__ == "__main__":
    test_12()