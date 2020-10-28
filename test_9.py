import waitings
import log_output
import login_page
import arrived_at_the_warehouse_no_sorting

def test_9():
    log_output.Print('Тест 9')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 9 не пройден')

    result = arrived_at_the_warehouse_no_sorting.check_menu(driver)

    if result == 'ERROR':
        log_output.Print('Тест 9 не пройден')

    name = '11-1111-1111'

    arrived_at_the_warehouse_no_sorting.enter_object_number(driver, name)

    waitings.visual_checking()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()

if __name__ == "__main__":
    test_9()