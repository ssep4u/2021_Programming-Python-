class Cafe():
    def __init__(self):
        self.seat_list = []
        self.init_seat_list()

    def checkin_seat(self):
        show_empty_seat_list()  #빈좌석보여주기
        position = input()  #좌석 선택하기
        position = int(position)
        self.seat_list[position].set_checkin()

    def show_empty_seat_list(self):
        for seat in self.seat_list:
            if seat.checkin == None
                출력
