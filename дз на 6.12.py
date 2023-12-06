def check_same_color(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        return True
    else:
        return False


x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))


if check_same_color(x1, y1, x2, y2):
    print("Клетки принадлежат одному цвету")
else:
    print("Клетки не принадлежат одному цвету")
