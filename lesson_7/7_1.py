class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f"Color = {self.color}, passenger seats = {self.seats}. "
                f"Baby seat availability: {self.is_baby_seat}")


car_1 = Car("black", 3, False)
car_2 = Car("blue", 4, True)
car_3 = Car("white", 5, True)
car_4 = Car("green", 3, True)
car_5 = Car("gray", 4, False)

cars_list = []
cars_list.append(car_1)
cars_list.append(car_2)
cars_list.append(car_3)
cars_list.append(car_4)
cars_list.append(car_5)


class Taxi:
    def __init__(self, cars: list[Car]):
        self.car = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        if is_baby == 1:
            count_passengers -= 1
        for i in cars_list:
            suitable_car = (i.seats >= count_passengers) and (is_baby <= i.is_baby_seat)
            if suitable_car and i.is_busy is False:
                i.is_busy = True
                return print(i)


taxi1 = Taxi(cars_list)
taxi2 = Taxi(cars_list)
taxi1.find_car(4, True)
taxi2.find_car(4, True)
