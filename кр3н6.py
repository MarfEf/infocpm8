def digit_sum(n):
    return sum(int(digit) for digit in str(n))

numbers = list(map(int, input("Введите последовательность натуральных чисел через пробел: ").split()))
max_sum = max(digit_sum(num) for num in numbers)

result = [num for num in numbers if digit_sum(num) == max_sum]

print("Числа с максимальной суммой цифр:", result)
