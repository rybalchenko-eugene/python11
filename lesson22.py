#  Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

check = True   
BASE = 16
while check:
    num = input('Введите число для перевода в 0x: ')
    if num.isnumeric():
        check = False
    else: 
        print('Неверный ввод, ')
print('№1 Встроенная функция переводит', num, 'как ' ,hex(int(num)))
num = int(num)
convert_num = ''
while num != 0:
    letter = str (num % BASE)
    match letter:
        case '10':
            letter = 'A'
        case '11':
            letter = 'B'
        case '12':
            letter = 'C'
        case '13':
            letter = 'D'
        case '14':
            letter = 'E'
        case '15':
            letter = 'F'
    convert_num = letter + convert_num
    num //= BASE
print('написанная программа переводит ввод как 0x:' , convert_num)

# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.
import math
print('\n №2 Формула квадратного уравнения:  A*x^2 + B*x + C = 0')
a = int(input('Введите A: '))
b = int(input('Введите B: '))
c = int(input('Введите C: '))
d = b**2 - 4*a*c
if d < 0:
    x1 = (-b + complex(d**0.5))/(2*a)
    x2 = (-b - complex(d**0.5))/(2*a)
else:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
print(f'd= {d}, x1 = {x1}, x2 = {x2}')
    
# ✔ Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import fractions
fract1 = input('\n №3 Введите первую дробь вида A/B: ')
fract2 = input('Введите вторую дробь вида C/D: ')
list1 = fract1.split('/')
list2 = fract2.split('/')
# проверки на корректный ввод не проводим
# умножение
import math
num1 = int(list1[0])*int(list2[0])
div1 = int(list1[1])*int(list2[1])
nod = math.gcd(num1, div1)
print(f'произведение дробей = {num1/nod}/{div1/nod}')
# сложение
num2 = int(list1[0])*int(list2[1]) + int(list2[0])*int(list1[1])
div2 = int(list1[1])*int(list2[1])
nod = math.gcd(num2, div2)
print(f'сложение дробей = {num2/nod}/{div2/nod}')
# проверка
fr1 = fractions.Fraction(int(list1[0]), int(list1[1]))
fr2 = fractions.Fraction(int(list2[0]), int(list2[1]))
print('Умножение встроенным модулем = ', (fr1 * fr2))
print('Сложение встроенным модулем = ', (fr1 + fr2))