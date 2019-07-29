import sys
import os
import shutil


def mk_dir():
    answer = "Y"
    while answer != "N":

        num_dir = int(input('Сколько будем делать директорий? '))
        dir_name = input("Укажите имя родительской директори ")
        path_ = os.getcwd()

        try:
            if num_dir > 1:
                for i in range(num_dir):
                    path_ = os.path.join(os.getcwd(), dir_name + str(i))
                    os.mkdir(path_)
                    os.chdir(path_)
            print(f"Создано {num_dir} папок {dir_name}")
            print(os.getcwd())

        except FileExistsError:
            print("Такая директория уже есть!!!")

        answer = input("Работаем дальше (Y/N)? ")

#mk_dir()

def prnt_dir():
    dir_name = input("Где Вы хотите посмотреть папки? ")
    lst = [name for name in os.listdir(dir_name)
           if os.path.isdir(os.path.join(dir_name, name))]
    print(lst)
    return dir_name

#prnt_dir()

def remove_dir():

    answer = "Y"
    while answer != "N":

        print(os.getcwd())

        dir_name = prnt_dir()

        rm_dir = input("Укажите название диектории к удалению ")

        num_dirs = 0
        all_path = os.path.join(dir_name, rm_dir)
        for dirs in os.walk(all_path):
            num_dirs += 1

        try:
            shutil.rmtree(rm_dir)
            print(f"удалено {num_dirs} директорий типа {rm_dir}")
        except FileExistsError:
            print("Неудачная попытка")

        answer = input("Работаем дальше (Y/N)? ")

#remove_dir()

def remove_file():

    dir_ = input("Укажите путь в директорию для удаления файла ")
    rm_file = input("Укажите название удаляемого файла ")

    path = os.path.join(dir_, rm_file)

    try:
        os.remove(path)
        print(f"Файл {rm_file} успешно удален")
    except WindowsError:
        print("Неудачно!!!")

def copy_file():
    print(os.getcwd())
    from_ = input("укажите откуда копируем ")
    dir_ = os.scandir(from_)
    for i in dir_:
        print(i)
    file_name = input("Какой файл копируем? ")

    try:
        shutil.copy(os.path.join(from_,file_name), os.path.join(from_,"copy"+file_name))
        print("Копирование сделано")
    except NotImplemented:
        print("Копирование не получилось!!!")


#copy_file()

def change_dir():
    where_you = input("Нужен ли Вам путь текущей директории? (Y/N)")
    if where_you == "Y" or "y":
        print(os.getcwd())
    else:
        pass
    change_dir = input("Укажите папку в которую нужно перейти: ")
    try:
        os.chdir(change_dir)
        print("")
    except NameError:
        print("Такой папки нет!!!")