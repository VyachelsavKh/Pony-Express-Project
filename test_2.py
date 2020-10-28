import waitings
import log_output
import login_page
import main_page

def test_2():
    log_output.Print('Тест 2')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 2 не пройден')

    result = main_page.quit(driver)

    if result == 'ERROR':
        log_output.Print('Тест 2 не пройден')
    else:
        log_output.Print('Тест 2 пройден')

    waitings.visual_checking()
    driver.close()


if __name__ == "__main__":
    test_2()