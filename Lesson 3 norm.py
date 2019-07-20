
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachi(n,m):
    f1 = 1
    f2 = 1

    current = f2
    old = f1
    fibolist = [1,1]
    for i in range(1, m):
        new_new = current + old
        fibolist.append(new_new)
        print (new_new)
        old = current
        current = new_new
    print (fibolist[n:m+1], len(fibolist))

fibonachi(17,20)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sortirovka(lst):

    for j in range(1, len(lst)):
        for i in range(1,len(lst)):
            if lst[i-1] > lst[i]:
                temp = lst[i-1]
                lst[i-1] = lst[i]
                lst[i] = temp

lst = [5, 1, 4, 2, 8, 0, 7]

sortirovka(lst)
print(lst)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_(function, itteration):
    #реализация возможно только с использованиеь lambda, подставляемой на место function
    new_itteration = list()

    for i in itteration:

        if function(i) is True:
            new_itteration.append(i)

        else:
            continue
    print(new_itteration)

filter_((lambda i: i < 0), [0,-2,4,0,4,-5])

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def if_parlgrm(a, b, c, d):
# [AC ^ 2} + BD ^ 2} = 2{(AB ^ 2} + AD ^ 2}) признак параллелограмма
# d2= (х2— х1)2+ (y2— y1)2. длина отрезка по координатам

    import math

    ac_d = math.sqrt((c[0] - a[0])**2 + (c[1] - a[1]))
    bd_d = math.sqrt((d[0] - b[0])**2 + (d[1] - b[1]))
    ab_d = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1]))
    ad_d = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1]))

    if ac_d**2 + bd_d**2 == 2*(ab_d**2 + ad_d**2):
        print("Да, это парллелограмм")
    else:
        print("Нет, это не параллелограмм")

if_parlgrm([0,0], [1,0.33], [2.33,1], [2,0])