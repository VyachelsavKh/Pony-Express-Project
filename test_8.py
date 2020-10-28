import waitings
import log_output
import login_page
import arrived_at_the_warehouse_no_sorting

def test_8():
    log_output.Print('Тест 8')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 8 не пройден')

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