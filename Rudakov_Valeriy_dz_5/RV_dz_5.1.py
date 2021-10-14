def gen_num(n):
    for num in range(1, n + 1, 2):
        yield num


print(*gen_num(int(input("Введеите число n - предел генератора"))))
