class Cafe:
    def __init__(self):
        self.seat_list = []

        for num in range(1, 10+1):
            self.seat_list.append(Seat(num))

    def checkin(self):
        self.show_empty_seat_list()  #빈자리 보여주자
        checkin_position = input('자리 선택하세요: ')    #자리선택하자
        checkin_position = int(checkin_position)
        new_checkin = Checkin() #Checkin 생성하자
        new_checkin.set_random_number() #checkin 랜덤넘버 생성하자
        self.seat_list[checkin_position - 1].checkin = new_checkin

        self.show_empty_seat_list()  # 빈자리 보여주자

    def show_empty_seat_list(self):
        empty_seat_list = []
        for seat in self.seat_list: #전체 자리에서 하나씩 꺼낼거야
            if seat.checkin == None: #checkin 정보가 없으면,
                empty_seat_list.append(seat)    #빈자리 리스트에 추가
        for seat in empty_seat_list:
            print(seat)

    def checkout(self):
        checkout_position = input('checkout 자리 선택하세요: ')
        checkout_position = int(checkout_position)
        rn = input('입실시 받은 번호는: ')
        rn = int(rn)
        if self.seat_list[checkout_position - 1].checkin.random_number == rn:
            self.seat_list[checkout_position - 1].checkin = None
        else:
            print('번호틀림')

        self.show_empty_seat_list()  # 빈자리 보여주자

class Seat:
    def __init__(self, position):
        self.position = position    #위치
        self.checkin = None         #체크인정보 영수증

    def __str__(self):
        return str(self.position)

    
class Checkin:
    #랜덤숫자
    def __init__(self):
        self.random_number = -1

    def set_random_number(self):
        rn = 100#랜덤숫자 뽑자
        self.random_number = rn


cafe = Cafe()
cafe.checkin()
cafe.checkout()
    
    
    
    
    
    
    
    
        
    
    