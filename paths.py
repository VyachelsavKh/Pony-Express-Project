pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'
driver_path = r'./chromedriver.exe'
pegas_title = 'Пегас'

correct_enter_login = 'ext.mgu_education'
correct_enter_password = 'rg#P5hZm4F'

wrong_enter_login = 'wrong_login'
wrong_enter_password = 'wrong_password'

search_time = 1
transition_time = 1
visual_check_time = 5

print_to_output_to_file = 1

if __name__ == "__main__":
    print("Файл содержит пути и константы:")
    print('pegas_url - путь к сайт')
    print('driver_path - путь к драйверу')
    print('pegas_title - название по которому определяем сайт')
    print('myLogin - правильный логин на сайте')
    print('myPassword - правильный пароль на сайте')
    print('search_time - время поиска элемента на странице')
    print('transition_time - время открытия новой страницы')
    print('visual_check_time - время на физуальный контроль выполненных действий')
    print('print_to_output_to_file - в каком формате пистаь логи 1 - в файл и на экран, 0 - только экран')

