import time



class TrafficLight:
    #атрибут
    color = "белый"

    # метод
    def running(self):
        # while True:
        print("Красный")
        time.sleep(7)
        print("желтый")
        time.sleep(2)
        print("зеленый")
        time.sleep(4)


TrafficLight = TrafficLight()
TrafficLight.running()


import itertools

class TrafficLight_1:
    color = [["red", [7, 41]], ["yellow", [2, 43]], ["green", [2, 42]]]

    def running(self):
        for i in itertools.cycle(self.color):
            print(f'\r\033[{i[1][1]}m\033[1m{i[0]}\033[0m', end='')
            time.sleep(i[1][0])


TrafficLight = TrafficLight_1()
TrafficLight.running()

