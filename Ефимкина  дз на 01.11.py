X = int(input("Введите натуральное число X: "))

i = 1
while i <= X:
    if X % i == 0:
        print(i)
    i += 1
