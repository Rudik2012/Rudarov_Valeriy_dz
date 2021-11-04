

class Kletki:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['&' * rows for i in range(self.nums // rows)]) + '\n' + '&' * (self.nums % rows)

    def __str__(self):
        return  f"{self.nums}"

    def __add__(self, other):
        print("Объединение клеток = ")
        return Kletki(self.nums + other.nums)

    def __sub__(self, other):
        print("Вычитание клкток =")
        return Kletki(self.nums - other.nums) if self.nums - other.nums > 0 else "вычитание невозможно"

    def __mul__(self, other):
        print("Умножение = ")
        return Kletki(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Деление = ")
        return Kletki(self.nums // other.nums)

kletki_1 = Kletki(15)
kletki_2 = Kletki(10)
print(kletki_1 + kletki_2)
print(kletki_1 - kletki_2)
print(kletki_1 * kletki_2)
print(kletki_1 // kletki_2)
print(kletki_2.make_order(2))
