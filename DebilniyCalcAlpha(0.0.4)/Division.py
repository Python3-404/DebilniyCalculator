import os
from colorama import Fore, Back
from colorama import init

# use Colorama to make Termcolor work on Windows too
init()
print( Fore.BLACK )
print( Back.GREEN )
a = float(input("Первое число: "))
print( Back.YELLOW )
b = float(input("Второе число: "))
c = a / b
print( Back.CYAN )
print("Результат: " + str(c))
print()
os.system("Division.py")
