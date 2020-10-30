import waitings
import log_output
import login_page
import time
import editing_user_groups

'''
Тест-кейс №6. Проверка права на создание группы пользователей и удаление её
1) В браузере открыть ссылку на вход с систему - 
    Открылась страница «Вход в систему» с полями для ввода логина и пароля
2) Ввести логин пользователя в поле для логина, пароль пользователя в поле для пароля и нажать кнопку «Войти» - 
    Открылась «Главная страница» ПЕГАС 2.0 с кнопкой «Menu»
3) Нажать кнопку «Menu» -
    В выпавшем списке доступен пункт «Сервис» - «Управление» разрешениями»
4) Выбрать пункт «Группы пользователей» - 
    Открылась форма «Редактирование групп пользователей»
5) Нажать кнопку «Создать новую» -
    Открылась форма «Создание группы пользователей»
6) Ввести в поле «Название группы» непустое название группы и нажать кнопку «Сохранить» - 
    Система создала группу
7) Ввести название группы в строке поиска - 
    Система оставила только группы с именами начинающимися на
8) Проверить название первой группы в списке -
    Первая группа в списке имеет точно такое же название без доп символов
9) Выделить первую группу в списке - 
    Первая группа в списке выделилась
10) Нажать кнопку Удалить группу - 
    Открылось новое окно с кнопкой Удалить
11) Нажать кнопку Удалить - 
    Вернулось окно со всеми группами
12) Ввести название группы в строке поиска - 
    Не появилось групп либо первая группа в списке обладает схожим, но не таким же именем
'''

def test_6():
    log_output.Print('Тест 6')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 6 не пройден')
        waitings.visual_checking()
        driver.close()
        return

    name = editing_user_groups.create_group(driver)

    if name == 'ERROR':
        log_output.Print('Тест 6 не пройден')
        waitings.visual_checking()
        driver.close()
        return

    time.sleep(1)

    result = editing_user_groups.check_for_a_single_group_with_a_similar_name(driver, name)

    if result == 'ERROR':
        log_output.Print('Тест 6 не пройден')
        waitings.visual_checking()
        driver.close()
        return

    result = editing_user_groups.delete_first_groop(driver)

    if result == 'ERROR':
        log_output.Print('Тест 6 не пройден')
        waitings.visual_checking()
        driver.close()
        return

    result = editing_user_groups.check_for_a_single_group_with_a_similar_name(driver, name)

    if result == 'ERROR':
        log_output.Print('Тест 6 пройден')
    else:
        log_output.Print('Тест 6 не пройден')

    waitings.visual_checking()
    driver.close()

if __name__ == "__main__":
    test_6()
