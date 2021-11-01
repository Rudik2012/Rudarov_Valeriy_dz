class Stationery:
    def __init__(self, title="Что-то рисует"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки.{self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


stat = Stationery()
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

supply = [stat, pen, pencil, handle]

for i in supply:
    i.draw()