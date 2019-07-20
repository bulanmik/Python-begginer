 #Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def rd(x,y=0):

    m = int('1'+'0'*y)
    print('m= ', m)
    q = x*m
    print('q= ', q)
    c = int(q)
    print('c= ', c)
    i = int( (q-c)*10 )
    print('i= ', i)
    if i >= 5:
        c += 1
    return c/m

print(rd(10.44444, 0))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить



def happy_number(ticket_number):
    ticket_number = str(ticket_number)

    while len(ticket_number) == 6:

        print(ticket_number)
        ticket_number1_3 = sum((int(ticket_number[i]) for i in range(0,2)))
        #print(ticket_number1_3)
        ticket_number4_6 = sum((int(ticket_number[i]) for i in range(3,5)))
        #print(ticket_number4_6)

        if ticket_number1_3 == ticket_number4_6:
           result = "Happy Number!"
        else:
            result = "Try again"
        return result

    print("Цифр должно быть 6, попробуйте еще раз!")



print(happy_number(123123))