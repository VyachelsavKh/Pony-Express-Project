import login_page
import arrived_at_the_warehouse_no_sorting
import time
import pytest

'''
Тест-кейс №11. Проверка ввода некорректного номера накладной в блок событий 71
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «71. Прибыл на склад (без сортировки)» - 
        Открылась форма «Ввод данных о блоке»
4) Нажать кнопку «Продолжить без курьера» - 
    Открылась форма «71. Прибыл на склад (без сортировки)» с номером созданного блока
5) В поле ввода «Номер объекта» ввести текст «0012345666» и нажать кнопку Enter - 
    Система вернула ошибку «Марка не привязана»
'''

def test_11():
    driver = login_page.login()

    time.sleep(0.5)

    login_page.check_enty(driver)

    time.sleep(0.5)

    arrived_at_the_warehouse_no_sorting.check_menu(driver)

    number = '0012345666'

    time.sleep(0.5)

    arrived_at_the_warehouse_no_sorting.enter_object_number(driver, number)

    time.sleep(0.5)

    result = arrived_at_the_warehouse_no_sorting.check_error(driver)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    assert result == 'Марка не привязана', 'Система вернула другую ошибку'