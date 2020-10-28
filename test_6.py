import waitings
import log_output
import login_page
import editing_user_groups

def test_6():
    log_output.Print('Тест 6')
    driver = login_page.login()

    identifiers = login_page.check_enty(driver)

    if identifiers == 'Wrong identifiers':
        log_output.Print('Тест 6 не пройден')

    result = editing_user_groups.create_group(driver)

    if result == 'ERROR':
        log_output.Print('Тест 6 не пройден')

    result = editing_user_groups.check_for_a_single_group_with_a_similar_name(driver, result)

    if result == 'ERROR':
        log_output.Print('Тест 6 не пройден')

    result = editing_user_groups.delete_first_groop(driver)

    if result == 'ERROR':
        log_output.Print('Тест 6 не пройден')
    else:
        log_output.Print('Тест 6 пройден')

    waitings.visual_checking()
    driver.close()

if __name__ == "__main__":
    test_6()