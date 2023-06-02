# Напишите функцию для транспонирования матрицы


def rev_matrix(array: list[int]) -> list[int]:
    res_matrix = []

    for row in range(0, len(array[0])):
        row_arr = []
        for line in array:
            row_arr.append(line[row])
        res_matrix.append(row_arr)
    return res_matrix


matrix = [[2, 4, 7], [3, 8, 3], [4, 45, 3], [5, 18, 22]]
print(matrix)
print(rev_matrix(matrix))


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного
# аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def to_dict(**kwargs) -> dict:
    res_dict = {}
    for key, value in kwargs.items():
        if type(value) == list or type(value) == dict or type(value) == set:
            res_dict.setdefault(str(value), key)
        else:
            res_dict.setdefault(value, key)
    return res_dict


print(to_dict(a=1, b=3, c=5, d='res', f=[3, 1, '5gt'], g=(1, 5, 33, 0)))

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно
# сохраняйте все операции поступления и снятия средств в список.
#  Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

account = 0
history = []
counter = 1


def addition(sum: float) -> account:
    global account
    global counter
    if sum % 50 == 0 and sum >= 50:
        account += sum
        history.append(('added', sum))
        counter += 1
        if counter % 3 == 0:
            account *= 1.03
    else:
        print('Sum should be div.50 ')
        return


def withdrawal(sum: float):
    global account
    global counter
    if sum % 50 == 0 and sum <= account:
        account -= sum
        history.append(('withdrawed', sum))
        counter += 1
        if counter % 3 == 0:
            account *= 1.03
    else:
        print('Sum should be div.50 or sum > account')
        return


def check_sum():
    print(f'{account= :.2f}')


addition(100)
addition(75)
addition(150)
withdrawal(34)
withdrawal(200)
check_sum()
