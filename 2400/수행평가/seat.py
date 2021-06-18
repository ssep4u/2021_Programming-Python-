class Seat:
    def __init__(self, position):
        self.position = position
        self.checkin = None
        self.checkout = None




    def set_checkin(self):
        new_checkin = Checkin()

        self.checkin = new_checkin
