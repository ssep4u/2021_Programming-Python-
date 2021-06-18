class Cafe:
    def __init__(self):
        self.seat_list = []


class Seat:
    def __init__(self, position):
        self.position = position
        self.checkin = None

    def __str__(self):
        return self.position