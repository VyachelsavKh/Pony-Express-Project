import login_page
import waitings
import log_output
import paths

def test_3():
    log_output.Print('Тест 1')
    driver = login_page.login(paths.wrong_enter_login, paths.wrong_enter_password)

    identifiers = login_page.check_non_entry(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 3 пройден')
    else:
        log_output.Print('Тест 3 не пройден')

    waitings.visual_checking()
    driver.close()


if __name__ == "__main__":
    test_3()