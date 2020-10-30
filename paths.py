pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/' # путь к сайту
browser = 'Firefox' # 'Chrome' # какой браузер используем
driver_path = r'./firefoxdriver.exe' # r'./chromedriver.exe' # путь к драйверу
pegas_title = 'Пегас' # название по которому определяем сайт

correct_enter_login = 'ext.mgu_education' # правильный логин на сайте
correct_enter_password = 'rg#P5hZm4F' # правильный пароль на сайте

wrong_enter_login = 'wrong_login' #
wrong_enter_password = 'wrong_password' #

search_time = 10 # время поиска элемента на странице
transition_time = 5 # время на открытие новой страницы
visual_check_time = 0 # время на визуальный контроль выполненных действий

print_to_output_to_file = 1 #  каком формате пистаь логи 1 - в файл и на экран, 0 - только экран