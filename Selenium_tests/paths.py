pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/' # путь к сайту

#browser = 'Chrome' # какой браузер используем
#driver_path = r'./chromedriver.exe' # путь к драйверу

browser = 'Firefox' # какой браузер используем
driver_path = r'./firefoxdriver.exe' # путь к драйверу

pegas_title = 'Пегас' # название по которому определяем сайт

correct_enter_login = 'ext.mgu2_education' # правильный логин на сайте
correct_enter_password = 'rg#P5hZm4F' # правильный пароль на сайте

wrong_enter_login = 'wrong_login' #
wrong_enter_password = 'wrong_password' #

search_time = 10 # время поиска элемента на странице
transition_time = 5 # время на открытие новой страницы

print_to_output_to_file = 0 # В каком формате пистаь логи 1 - в файл и на экран, 0 - только экран

destinationPointId_1202 = "4110acc0-137f-4fe6-bf69-50ee2590ded4" # Id точки назначения 1202

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

#swagger_tail = 'api/manual/index.html'