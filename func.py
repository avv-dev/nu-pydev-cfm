"""
File manager functions
"""
import os, shutil, sys


def incorrect_name(path, is_folder):
    prohibited = ['\\', '/', ';', ':', '*', '?', '"', '<', '>', '|']
    for prohibited_symbol in prohibited:
        if prohibited_symbol in path:
            return True
        elif is_folder and ('.' in path):
            return True
    return False


def create_dir(path):
    if path in os.listdir(os.getcwd()):
        return True
    else:
        os.mkdir(path)
        return False


def delete(path):
    if not (path in os.listdir(os.getcwd())):
        return True
    else:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        return False


def copy(old_path, new_path):
    if not (old_path in os.listdir(os.getcwd())):
        return 1
    elif new_path in os.listdir(os.getcwd()):
        return 2
    else:
        shutil.copy(old_path, new_path)
        return 0


def current_dir():
    return os.getcwd()


def dir_list():
    names = os.listdir(os.getcwd())
    dirs = []
    links = []
    files = []
    for name in names:
        if os.path.exists(name):
            if os.path.isdir(name):
                dirs.append(name)
            elif os.path.islink(name):
                links.append(name)
            elif os.path.isfile(name):
                files.append(name)
    return [dirs, links, files]


def os_info():
    return [sys.platform, os.name]


def dir_change(path):
    if os.path.exists(path):
        os.chdir(path)
        return False
    else:
        return True


if __name__ == '__main__':
    print(incorrect_name(input('Path:'), True))