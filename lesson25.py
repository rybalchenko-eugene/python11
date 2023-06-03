# inp = '234/23/5/23/56'
# a1, a2, a3, *a4 = inp.split('/')
# dict1 = {a2: a1, a3: tuple(a4)}
# print(dict1)
#
# text1 = 'переданный аргумент object. Мы знаем, что все целые числа в Python являются типом int. Это означает, что проверка объекта type(3) == object в точности эквивалентна проверке объекта int == object, что  однозначно неверно. В Python, как это известно - все является объектом, следовательно дочерний класс (в данном случае int) наследуется от родителя'
# dict2 = {word: ord(word) for word in text1}
# iter_dict = iter(dict2.items())
# for i in range(0, 5):
#     print(next(iter_dict))
#
# gen1 = (i for i in range(0,100,2) if i%10 + i//10 != 8)
# print(*gen1)
# print(gen1)
#
# print((i for i in range(1,100) if i%3 == 0))

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов:  путь, имя файла, расширение файла.
text = 'C:\Windows\diagnostics\index\DiagnosDev.com'


def file_parse(ttext: str) -> tuple:
    *path, name = ttext.split('\\')
    name, ex = name.split('.')
    path = "\\".join(path)
    return (path, name, ex)


print(*file_parse(text), sep='\n')

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
# ставка int,  премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве
# ключа  и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

name_list = ['Ivan', 'Petr', 'Ivan2', 'Bok', 'Spor']
stake_list = [200, 250, 300, 100, 140]
bonus_list = ['-5%', '10.2%', '7%', '12.75%', '4%']
salary_list = {name: stake_list[name_list.index(name)] * (float(bonus_list[name_list.index(name)][:-1]) / 100 + 1) for
          name in name_list}
print(salary_list)
# Создайте функцию генератор чисел Фибоначчи (см. Википедию)
a = int(input('Give amount: '))
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(a)))
