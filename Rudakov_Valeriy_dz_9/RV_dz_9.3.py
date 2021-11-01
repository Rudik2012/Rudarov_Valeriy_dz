class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
         return f"{self.name} {self.surname}"

    def get_total_income(self):
         return f"{sum(self.income.values())}"


meneger = Position("Valeriy", "Rudakov", "FGD", 50000, 2500)
print(meneger.get_full_name(), meneger.position, meneger.get_total_income(), sep=",")




