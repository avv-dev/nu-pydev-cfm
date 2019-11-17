"""
User interface functions
"""
import func

def main_menu():
    menu_items = {0: 'создать папку', 1: 'удалить (файл/папку)', 2: 'копировать (файл/папку)',
                  3: 'просмотр содержимого рабочей директории', 4: 'посмотреть только папки',
                  5: 'посмотреть только файлы', 6: 'просмотр информации об операционной системе',
                  7: 'создатель программы', 8: 'играть в викторину', 9: 'мой банковский счет',
                  10: 'смена рабочей директории', 11: 'выход'}
    menu_commands = {0: 'create_dir', 1: 'delete', 2: 'copy', 3: 'workdir_list', 4: 'workdir_list_dir',
                     5: 'workdir_list_file', 6: 'os_info', 7: 'credits', 8: 'victory', 9: 'account',
                     10: 'workdir_change', 11: 'quit_app'}
    print ('===================================\n'
           '=  Консольный файловый менеджер:  =\n'
           '===================================\n')
    for i in range(len(menu_items)):
        if i <= 9:
            inum = f' {i}'
        else:
            inum = f'{i}'
        print(f'{inum} - {menu_items[i]}')
    selected = input('\nВыберите пункт меню:\n>>> ')
    if selected.isdigit():
        return menu_commands[int(selected)]
    else:
        return 'incorrect_input'


def ui_create_dir():
    print('Создание папки:\n')
    folder_name = input('Введите имя папки:\n>>> ')
    if func.incorrect_name(folder_name, True):
        print('Некорректное имя папки.')
    else:
        check = input(f'Будет создана папка "{folder_name}". Y/N ?\n>>>').lower()
        if check == 'n':
            return False
        elif check == 'y':
            err = func.create_dir(folder_name)
            if err:
                print(f'Папка "{folder_name}" уже существует.')
                return True
            else:
                print(f'Папка "{folder_name}" успешно создана.')
                return False
        else:
            return True


def ui_delete():
    print('Удаление папки:\n')
    file_name = input ( 'Введите имя файла/папки:\n>>> ' )
    check = input(f'Будет удален "{file_name}". Y/N ?\n>>>').lower()
    if check == 'n':
        return False
    elif check == 'y':
        err = func.delete(file_name)
        if err:
            print(f'"{file_name}" не существует.')
            return True
        else:
            print(f'"{file_name}" успешно удалена.')
            return False
    else:
        return True


def ui_copy():
    print('Копирование файла/папки:\n')
    old_name = input('Введите имя файла/папки:\n>>> ')
    new_name = input ( 'Введите имя файла/папки:\n>>> ' )
    if func.incorrect_name(new_name, False):
        print('Некорректное имя файла/папки.')
    else:
        check = input(f'Будет скопировано содержимое "{old_name}" в "{new_name}". Y/N ?\n>>>').lower()
        if check == 'n':
            return False
        elif check == 'y':
            err = func.copy(old_name, new_name)
            if err == 1:
                print(f'Объект для копирования "{old_name}" не существует.')
                return True
            elif err == 2:
                print(f'Адрес размещения "{new_name}" занят другим файлом/папкой.')
                return True
            else:
                print(f'"{old_name}" успешно скопирован в "{new_name}".')
                return False
        else:
            return True


def ui_workdir_list():
    print(f'Содержимое директории:\n{func.current_dir()}\n')
    [ dirs, links, files ] = func.dir_list()
    for elem in dirs:
        print(f'[{elem}]')
    for elem in links:
        print(f'<{elem}>')
    for elem in files:
        print(f'{elem}')


def ui_workdir_list_dir():
    print(f'Поддиректории (папки) в директории:\n{func.current_dir()}\n')
    dirs = func.dir_list()[0]
    for elem in dirs:
        print(f'[{elem}]')


def ui_workdir_list_file():
    print(f'Файлы в директории:\n{func.current_dir()}\n')
    files = func.dir_list()[2]
    for elem in files:
        print(f'<{elem}>')


def ui_os_info():
    print('Информация об операционной системе:\n')
    [type_code, name] = func.os_info()
    type_names = {'linux': 'Linux ',
                  'win32': 'Windows',
                  'cygwin': 'Windows/Cygwin',
                  'darwin': 'Mac OS X',
                  'os2': 'OS/2',
                  'os2emx': 'OS/2 EMX'}
    if type_code in type_names.keys():
        print(type_names[type_code], name.upper())
    else:
        print(name.upper())


def ui_credits():
    print('===================================\n'
          '=  Консольный файловый менеджер:  =\n'
          '===================================\n\n'
          '(c) Vildan Abdullin, 2019\n\n'
          'https://github.com/avv-dev/nu-pydev-cfm\n')


def ui_work_dir_change():
    print('Смена рабочей директории:\n')
    path = input('Введите имя папки:\n>>> ')
    err = func.dir_change(path)
    if err:
        print(f'Путь "{path}" не существует.')
        return True
    else:
        print(f'Рабочая директория успешно изменена.')
        return False


if __name__ == '__main__':
    print(main_menu())