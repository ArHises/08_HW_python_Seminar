"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

"""
def show_main_menue():
    print()
    print('Choose an option from the list:')
    print('1. Provide all information in the list')
    print('2. Add new user information.')
    print('3. Find user by phone-number.')
    print('4. Delete user by phone-number')
    print('5. Exit.')

def main_program(file_name):
    show_main_menue()
    choise = input('Your choise: ')
    while choise != '5':
        print()
        if choise == '1':
            show_list(file_name)
        elif choise == '2':
            add_user(file_name)
        elif choise == '3':
            find_user_menue(file_name)           
        elif choise == '4':
            delete_user(file_name)
        else:
            print('----------- ERROR, try again -----------')
        
        show_main_menue()
        choise = input('Your choise: ')

def show_list(file_name):
    print('--- FULL LIST OF USERS ---')
    with open(file_name, 'r', encoding='utf -8') as file:
        print(file.read())

def add_user(file_name):
    user = ''
    user += input('Enter first name: ')
    user += ' ' + input('Enter last name: ')
    user += ' ' + input('Enter father\'s name: ')
    user += ' ' + input('Enter phone number: ')

    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(user + '\n')
    
    print(f'\n --- User \"{user}\" successfully added! ---')

def find_user(file_name, phone_num):
    with open(file_name, 'r', encoding='utf -8') as file:
        while True:
            line = file.readline()
            user_info = line.split()
            if not line:
                return ''
            elif user_info[-1] == phone_num:
                return line

def find_user_menue(file_name):
    phone_num = input('Enter phone-number: ')
    user = find_user(file_name, phone_num)
    if user:
        print('--- Found! ---')
        print(user)
    else:
        print('--- No such phone-number ---')

def delete_user(file_name):
    phone_num = input('Enter phone-number: ')
    user = find_user(file_name, phone_num)
    if user:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_name, 'w', encoding='utf-8') as file:
            for line in lines:
                user_info = line.split()
                if user_info[-1] != phone_num:
                    file.write(line)
        
        print(f'\n --- User \"{user}\" successfully deleted! ---')
    else:
        print('--- No such phone-number ---')

    

main_program('list_of_users.txt')