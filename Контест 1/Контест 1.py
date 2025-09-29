def main1():
    a = 10
    b = 20
    c = 30
    health = 100
    money = 100.00
    man_temperature = 36.6
    name = "Виктор"
    country = "Российская Федерация"
    password = "wlkjj23ih87t^&52hvbh^"

def main2():
    a = 10
    b = a + 5
    a = a + b
    print(a, b)
    print(a)
    print()
    print(b)


def main3():
    a = "Привет"
    b = 10
    print(a * b)

def main4():
    s = input()
    price = int(input())
    weight = int(input())
    money = int(input())


def main5():
    name = "Виктор"
    age = 75
    print(f"Имя: {name}, возраст: {age}")

    a = 2
    b = 5
    print(f"{a} в степени {b} = {a ** b}")

    n = 1.23456789
    print(f"Два знака после запятой: {n:15.4f}")

    print(f"|{n:<15.2f}|")
    print(f"|{n:^15.2f}|")
    print(f"|{n:>15.2f}|")

    name = "виктор"
    print(f"{name.title()}")

    s = "Эту \nстроку \nтребуется \nповторить"
    print(s * 3)


def main6():
    price = int(input())
    weight = int(input())
    money = int(input())

    submission = money - (price * weight)

    print(submission)

def main7():
    s = input()
    a = int(input())
    b = float(input())

    print(f"Строка: {s:^20}\nЦелое: {a:<20}\nДробное: {b:>20.2}")

    print(f'{" " * 40}40')

main7()




