import datetime

pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'
driver_path = r'./chromedriver.exe'

login = 'ext.mgu_education'
password = 'rg#P5hZm4F'

print_to_output_to_file = 1
    
if print_to_output_to_file:
    date = datetime.datetime.now()
    output_file_name = date.strftime('%Y.%d.%m,%H.%M.%S.log')