        # Задача 2: Найдите сумму цифр трехзначного числа.
        # *Пример:*
        # 123 -> 6 (1 + 2 + 3)
        # 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите 3х значное число :'))
result = 0
while number > 0:
    result += number % 10
    number //= 10
print(result)
#===============================================================================================

        # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
        # Вместе они сделали S журавликов.
        # Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
        # сделали одинаковое количество журавликов,
        # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
        #*Пример:*
        # 6 -> 1  4  1
        # 24 -> 4  16  4
        #     60 -> 10  40  10

numbers = int(input('Сколько всего журавликов?'))

if numbers < 6 or numbers % 6 !=0:
    print('Не корректное число')
else:
    katy = numbers // 3  * 2
    petSer = (numbers - katy) // 2

    print(f'Петя:{petSer} \n'
          f'Катя:{katy} \n'
          f'Сережа:{petSer}')

# ===============================================================================================
        # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
        # и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
        # где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
        # т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
        #
        # *Пример:*
        #
        # 385916 -> yes
        # 123456 -> no

ticket = int(input('Введите № билета'))

if ticket > 999999 or ticket < 100000:
    print('Такого билета нет')
else:
    sum1 = sum2 = 0
    countDigit = len(str(ticket))
    while countDigit > 0:
        if countDigit > 3:
            sum1 += ticket % 10
            ticket //= 10
            countDigit -= 1
        else:
            sum2 += ticket % 10
            ticket //= 10
            countDigit -= 1
    if sum1 == sum2:
        print('Счастливый билет')
    else:
        print('НEсчастливый билет')
# ===============================================================================================


        # Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
        # если разрешается сделать один разлом по прямой между дольками
        # (то есть разломить шоколадку на два прямоугольника).
        # *Пример:*
        #
        # 3 2 4 -> yes
        # 3 2 1 -> no

size1 = int(input('Введите n размер шоколадки '))
size2 = int(input('Введите m размер шоколадки '))
piece = int(input('Сколько долек хотите отломить '))


if piece > size1 * size2:
    print('Кусок больше шоколадки')
elif piece == size1 * size2:
    print('Ты съешь всю шоколадку')
elif piece % size1 == 0 or piece % size2 == 0:
    print('Yes')
else:
    print('No')








