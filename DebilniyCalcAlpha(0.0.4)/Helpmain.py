import os
import time
mode = input("Выберите режим(+, -, *, /,): ")
if mode == "+":
    os.system("Start LaunchPlus.py")
elif mode == "-":
    os.system("Start LaunchMinus.py")
elif mode == "*":
    os.system("Start LaunchMultiplication.py")
elif mode == "/":
    os.system("Start LaunchDivision.py")
else:
    print("Ошибка, пожалуйста подождите . . .")
    time.sleep(2)
    os.system("cls")
    os.system("Helpmain.py")
