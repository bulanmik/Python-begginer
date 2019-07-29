# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import mkdir_lesson_5_easy as mkdir

answer = ""

while answer != "N":
    do = int(input("Выберите действие: \n "
          "1.Перейти в папку \n "
          "2.Просмотреть содержимое папки \n "
          "3.Удалить папку \n "
          "4.Создать папку \n " 
          "5.Завершить работу \n"))
    if do == 1:
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
    elif do == 2:
        mkdir.prnt_dir()

    elif do == 3:
        mkdir.remove_dir()

    elif do == 4:
        mkdir.mk_dir()

    elif do == 5:
        answer = "N"


