import login_page
import waitings
import log_output

def test_1():
    log_output.Print('Тест 1')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Correct identifiers':
        log_output.Print('Тест 1 пройден')
    else:
        log_output.Print('Тест 1 не пройден')

    waitings.visual_checking()
    driver.close()


if __name__ == "__main__":
    test_1()