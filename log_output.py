import paths
import datetime

if paths.print_to_output_to_file:
    current_date = datetime.datetime.now()
    output_file_name = current_date.strftime('%Y.%d.%m,%H.%M.%S.log')


def Print(string):
    if paths.print_to_output_to_file:
        print(string)
        with open(output_file_name, 'a') as output_file:
            output_file.write(string + '\n')
    else:
        print(string)

if __name__ == '__main__':
    print('Файл содержит средства записи логов')
