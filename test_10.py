import waitings
import time
import log_output
import login_page
import arrived_at_the_warehouse_no_sorting

def test_10():
    log_output.Print('Тест 10')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 10 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    result = arrived_at_the_warehouse_no_sorting.check_menu(driver)

    if result == 'ERROR':
        log_output.Print('Тест 10 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    name = '11-1111-1112'

    arrived_at_the_warehouse_no_sorting.enter_object_number(driver, name)

    if result == 'ERROR':
        log_output.Print('Тест 10 не пройден')
        waitings.visual_checking()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return

    time.sleep(1)

    back_ground_colour = arrived_at_the_warehouse_no_sorting.check_colour(driver)

    if back_ground_colour == 'background-color: rgb(194, 48, 48);':
        log_output.Print('Рамка стала красной')
        log_output.Print('Тест 10 пройден')
    else:
        log_output.Print('Рамка стала другого цвета')
        log_output.Print('Тест 10 не пройден')

    waitings.visual_checking()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()
    return

if __name__ == "__main__":
    test_10()