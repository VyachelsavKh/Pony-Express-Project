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

print_to_output_to_file = 0 #  каком формате пистаь логи 1 - в файл и на экран, 0 - только экран

urls = [
    'http://configurations-backend-edu.pegasus.ponyex.local/',  #0
    'http://couriers-backend-edu.pegasus.ponyex.local/',        #1
    'http://delivery-edu.pegasus.ponyex.local/',                #2
    'http://delivery-backend-edu.pegasus.ponyex.local/',        #3
    'http://enumerations-backend-edu.pegasus.ponyex.local/',    #4
    'http://events-edu.pegasus.ponyex.local/',                  #5
    'http://events-backend-edu.pegasus.ponyex.local/',          #6
    'http://geography-edu.pegasus.ponyex.local/',               #7
    'http://geography-backend-edu.pegasus.ponyex.local/',       #8
    'http://localizations-backend-edu.pegasus.ponyex.local/',   #9
    'http://organization-backend-edu.pegasus.ponyex.local/',    #10
    'http://warehouses-edu.pegasus.ponyex.local/',              #11
    'http://warehouses-backend-edu.pegasus.ponyex.local/',      #12
    'http://waybills-backend-edu.pegasus.ponyex.local/'         #13
]