from src.calculator import *
from src.converter import *
from src.lexer import *

# Ваедите пример
string = "2^3"

instance = is_valid(string)

if len(instance) == 0:
    print("Некорректный ввод")
else:
    if "x" in instance:
        print("Укажите начало границы отрезка:")
        x1 = int(input())
        print("Введите конец отрезка: ")
        x2 = int(input())
        print("Вы хотите найти корни уравнения на данном отрезке? [Y/n]: ")
        answer = input()
        if answer == "Y":
            print("Корень уравнения:", secant_method(Arithmetics(to_postfix(instance)).solve, x1, x2))
        print("Вы хотите рассчитать интеграл на заданном отрезке? [Y/n]: ")
        answer = input()
        if answer == "Y":
            print("Результат вычисления:", integral(Arithmetics(to_postfix(instance)).solve, x1, x2))

    else:
        if len(to_postfix(instance)) == 0:
            print("Некорректный ввод")
        else:
            print("Результат примера:", Arithmetics(to_postfix(instance)).solve(0))
