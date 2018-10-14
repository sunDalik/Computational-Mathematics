import numpy as np
import matplotlib.pyplot as plt


def bisection_method_detailed(a, b, e):  # Выводит значения для таблицы
    while abs(a - b) > e:
        print(a)
        print(b)
        c = (a + b) / 2
        print(c)
        print(y(a))
        print(y(b))
        print(y(c))
        print(abs(a - b))
        print("Следующий шаг")
        if y(c) == 0:
            return c
        if y(a) * y(c) < 0:
            b = c
        else:
            a = c
    return c


def newton_method_detailed(x0, e):
    xn = x0 - y(x0) / dy(x0)
    print(x0)
    print(y(x0))
    print(dy(x0))
    print(xn)
    print(abs(x0 - xn))
    print("NEXT")
    while abs(x0 - xn) > e:
        x0 = xn
        xn = x0 - y(x0) / dy(x0)
        print(x0)
        print(y(x0))
        print(dy(x0))
        print(xn)
        print(abs(x0 - xn))
        print("NEXT")
    return xn


def y(x):
    return -1.8 * x ** 3 - 2.94 * x ** 2 + 10.37 * x + 5.38


def dy(x):
    return -1.8 * 3 * x ** 2 - 2.94 * 2 * x + 10.37


def bisection_method(a, b, e):
    n = 0
    while True:
        c = (a + b) / 2
        n = n+1
        if y(c) == 0:
            return "Найденный корень = " + str(
                c) + ", число итераций = " + str(n) + ", значение функции в найденном корне = " + str(y(c))
        if y(a) * y(c) < 0:
            b = c
        else:
            a = c
        if abs(a - b) <= e:
            return "Найденный корень = " + \
                   str(c) + ", число итераций = " + str(n) + ", значение функции в найденном корне = " + str(y(c))


def newton_method(x0, e):
    n = 1
    xn = x0 - y(x0) / dy(x0)
    while abs(x0 - xn) > e or y(xn) > e:
        x0 = xn
        xn = x0 - y(x0) / dy(x0)
        n = n+1
    return "Найденный корень = " + \
           str(xn) + ", число итераций = " + str(n) + ", значение функции в найденном корне = " + str(y(xn))


x = np.arange(-5, 5, step = 0.001)
plt.plot(x, y(x))
plt.axhline(0, color='black', linewidth=0.3)
plt.axvline(0, color='black', linewidth=0.3)
plt.savefig("Graph.png")

while True:
    print("Введите 1 для метода половинного деления, 2 для метода ньютона или exit для выхода")
    choice = input()
    if choice == "exit":
        break
    print("Введите 1 для ввода из консоли или 2 для ввода из файла")
    inp = input()
    print("Введите 1 для вывода в консоль или 2 для вывода в файл")
    outp = input()
    if choice == str(1):
        if inp == str("1"):
            print("Введите начало интервала")
            result = False
            while not result:
                try:
                    a = float(input())
                except ValueError:
                    print("Вы ввели не число")
                else:
                    result = True
            print("Введите конец интервала")
            result = False
            while not result:
                try:
                    b = float(input())
                except ValueError:
                    print("Вы ввели не число")
                else:
                    result = True
            print("Введите точность вычислений")
            result = False
            while not result:
                try:
                    e = float(input())
                except ValueError:
                    print("Вы ввели не число")
                else:
                    result = True
            if y(a)*y(b) < 0:
                if outp == str(1):
                    print(bisection_method(a, b, e))
                if outp == str(2):
                    print("Введите путь к файлу для вывода")
                    try:
                        with open(input(), 'w') as f:
                            f.write(bisection_method(a, b, e))
                    except OSError:
                        print("Некорректный путь к файлу")
                    else:
                        result = True
            else:
                print("Некорректный интервал!")

        if inp == "2":
            result = False
            while not result:
                print("Введите путь к файлу для ввода")
                try:
                    with open(input(), 'r') as f:
                        string = [float(v) for v in f.read().split(' ')]
                except OSError:
                    print("Некорректный путь к файлу")
                else:
                    result = True
            if y(string[0])*y(string[1]) < 0:
                if outp == str(1):
                    print(bisection_method(string[0], string[1], string[2]))
                if outp == str(2):
                    print("Введите путь к файлу для вывода")
                    try:
                        with open(input(), 'w') as f:
                            f.write(bisection_method(string[0], string[1], string[2]))
                    except OSError:
                        print("Некорректный путь к файлу")
                    else:
                        result = True
            else:
                print("Некорректный интервал!")

    if choice == str(2):
        if inp == str(1):
            print("Введите начальное приближение")
            result = False
            while not result:
                try:
                    x0 = float(input())
                except ValueError:
                    print("Вы ввели не число")
                else:
                    result = True
            print("Введите точность вычислений")
            result = False
            while not result:
                try:
                    e = float(input())
                except ValueError:
                    print("Вы ввели не число")
                else:
                    result = True
            if outp == str(1):
                print(newton_method(x0, e))
            if outp == str(2):
                print("Введите путь к файлу для вывода")
                try:
                    with open(input(), 'w') as f:
                        f.write(newton_method(x0, e))
                except OSError:
                    print("Некорректный путь к файлу")
                else:
                    result = True
        if inp == str(2):
            result = False
            while not result:
                print("Введите путь к файлу для ввода")
                try:
                    with open(input(), 'r') as f:
                        string = [float(v) for v in f.read().split(' ')]
                except OSError:
                    print("Некорректный путь к файлу")
                else:
                    result = True
            if outp == str(1):
                print(newton_method(string[0], string[1]))
            if outp == str(2):
                print("Введите путь к файлу для вывода")
                try:
                    with open(input(), 'w') as f:
                        f.write(newton_method(string[0], string[1]))
                except OSError:
                    print("Некорректный путь к файлу")
                else:
                    result = True

# 1.4 -- 2.4
# -1.0 -- 0
# -4 -- -2.6

# x1 = bisection_method_detailed(1.4,2.4,10**-2)
# print(x1)
# print('--------------')
# x1 = newton_method_detailed(-3.6,10**-2)
# print(x1)
# print('--------------')
# x1 = bisection_method(1.4, 2.4, 10 ** -6)
# x2 = bisection_method(-1.0, 0, 10 ** -6)
# x3 = bisection_method(-3.6, -2.6, 10 ** -6)
# print(str(x1) + ", " + str(x2) + ", " + str(x3))
# x1 = newton_method(1.1, 10 ** -6)
# x2 = newton_method(-0.8, 10 ** -6)
# x3 = newton_method(-3.6, 10 ** -6)
# print(str(x1) + ", " + str(x2) + ", " + str(x3))
