import os
import sys
import mkdir_lesson_5_easy

print(f"File`s arguments - {sys.argv}")


# arg[1] помощь _____________________________________________________________________________________________
def print_help():
    print("1. help - получение сравки")
    print("2. mkdir <dir_name> - создание директории")
    print("3. cp <file_name> - создает копию указанного файла - тестовый ключ")
    print("4. rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("5. cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("6. cls - отображение полного пути текущей директории")


# arg [2] создание директории_______________________________________________________________________________
def make_dir():

    dir_name = input("Укажите название создаваемой директории ")


    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"path {dir_name} was made")
    except FileExistsError:
        print(f"path {dir_name} exists!!!")

# arg [3] copy file _____________________________________________________________________________________________
def copy_file():
    mkdir_lesson_5_easy.copy_file()

#arg [4] remove_file_____________________________________________________________________________________________
def remove_file():
    mkdir_lesson_5_easy.remove_file()

# arg [5] change directory_______________________________________________________________________________________
def changedir():
    mkdir_lesson_5_easy.change_dir()

# arg [6] print path_____________________________________________________________________________________________
def print_path():
    print(os.getcwd())

x = sys.argv
i = 1

for i in x:
    if i == "help":
        print_help()
    elif i == "mkdir":
        make_dir()
    elif i == "cp":
        copy_file()
    elif i == "rm":
        remove_file()
    elif i == "cd":
        changedir()
    elif i == "cls":
        print_path()
    else:
        None
        print("Нет аргумента")







# do = {"help": print_help(),
#       "mkdir": make_dir(),
#       "cp": copy_file(),
#       "rm": remove_file(),
#       "cd": changedir(),
#       "prnt": print_path()}

# i = 1
# x = len(sys.argv)
# while i < x:
#     if sys.argv[i] == do[i]:
#         do[i]
#         i += 1

#
# try:
#     key = sys.argv[1]
# except IndexError:
#     key = None
#
# try:
#     key = sys.argv[2]
# except IndexError:
#     dir_name = None
#
# try:
#     key = sys.argv[3]
# except IndexError:
#     key = None
#
# try:
#     key = sys.argv[4]
# except IndexError:
#     dir_name = None
#
# try:
#     key = sys.argv[5]
# except IndexError:
#     key = None
#
# try:
#     key = sys.argv[6]
# except IndexError:
#     key = None
#
# if key:
#     if do.get(key):
#         do[key]()
#     else:
#         print("Укажите ключ help для справки")