from src.lexer import *
from src.converter import *

string = "cos(4)+sin(7*4)"
# string = "1+x"


instance = is_valid(string)

print(instance)
if len(is_valid(string)) == 0:
    print("Некорректный ввод")
else:
    if "x" in instance:
        # выполнение на 4
        pass
    else:
        print(to_postfix(instance))
        if len(to_postfix(instance)) == 0:
            print("Некоррекктный ввод")
        else:
            #сам калькулятор
            pass
