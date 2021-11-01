
class Road:
    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width

    def asfalt(self, weght=25, thickness=5):
        return f"{(self.lenth * self.width * weght * thickness) / 1000} тонн"

road = Road(5000,20)
print(road.asfalt())