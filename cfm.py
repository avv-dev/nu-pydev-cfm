"""
Console file manager
Provides basic file manager functionality as well as some useful tips.
"""
from ui import *
from apps import victory, accountant

while True:
    selection = 'incorrect_input'
    while selection == 'incorrect_input':
        selection = main_menu()
    if selection == 'create_dir':
        ui_create_dir()
    elif selection == 'delete':
        ui_delete()
    elif selection == 'copy':
        ui_copy()
    elif selection == 'workdir_list':
        ui_workdir_list()
    elif selection == 'workdir_list_dir':
        ui_workdir_list_dir()
    elif selection == 'workdir_list_file':
        ui_workdir_list_file()
    elif selection == 'os_info':
        ui_os_info()
    elif selection == 'credits':
        ui_credits()
    elif selection == 'victory':
        victory.victory()
    elif selection == 'account':
        accountant.accountant()
    elif selection == 'workdir_change':
        ui_work_dir_change()
    elif selection == 'quit_app':
        break
    else:
        pass