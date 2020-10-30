import waitings
import time
import log_output
import login_page
import included_in_consolidation

'''
Тест-кейс №13. Создание блока событий 79
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» и выпавшем списке выбрать пункт 
    «Производство» – «Регистрация событий» – «79. Включен в консолидацию» - 
        Открылась форма «Точка назначения»
4) Нажать кнопку «Выбрать» -
    Открылась форма «Выберите точку назначения»
5) Ввести в поле ввода номер точки «1202» - 
    В таблице с точками отображается точка с введенным номером
6) Выбрать в таблице точку 1202 и нажать кнопку «Добавить - 
    Открылась форма «Точка назначения» с выбранной точкой 1202
7) Нажать кнопку «Далее» -
    Открылась форма «79. Включен в консолидацию» с номером созданного блока и точкой назначения 1202
'''

def test_13():
    log_output.Print('Тест 13')
    driver = login_page.login()

    result = included_in_consolidation.input_dote_name(driver, '1202')

    if result == 'ERROR':
        log_output.Print('Тест 13 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    time.sleep(1)

    result = included_in_consolidation.choose_the_first_group(driver)

    if result == 'ERROR':
        log_output.Print('Тест 13 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    time.sleep(1)

    result = included_in_consolidation.continue_button(driver)

    if result == 'ERROR':
        log_output.Print('Тест 13 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    time.sleep(1)

    result = included_in_consolidation.check_menu(driver)

    if result == 'ERROR':
        log_output.Print('Тест 13 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    log_output.Print('Тест 13 пройден')
    waitings.visual_checking()

    waitings.visual_checking()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()
    return

if __name__ == "__main__":
    test_13()
