class House:
    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        max_floor = self.number_of_floors
        if (new_floor > max_floor) or (new_floor < 1):
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor+1):
                print(floor)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)