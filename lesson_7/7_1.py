class Car:
    def __init__(self, color, count_passenger_seats, is_baby_seat):
        self.color = color
        self.seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f"Color = {self.color}, passenger seats = {self.seats}. "
                f"Baby seat availability: {self.is_baby_seat}")


car_1 = Car("black", 3, False)
print(str(car_1))
