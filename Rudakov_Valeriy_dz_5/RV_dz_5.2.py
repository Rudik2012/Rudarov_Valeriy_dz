n = int(input("Введеите число n - предел генератора"))
gen_num = (num for num in range(1, n + 1, 2))
print(*gen_num)
