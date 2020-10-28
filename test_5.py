import waitings
import log_output
import login_page
import service_menu

def test_5():
    log_output.Print('Тест 5')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 5 не пройден')

    result = service_menu.editing_user_groups_button(driver)

    if result == 'ERROR':
        log_output.Print('Тест 5 не пройден')
    else:
        log_output.Print('Тест 5 пройден')

    waitings.visual_checking()
    driver.close()

if __name__ == "__main__":
    test_5()