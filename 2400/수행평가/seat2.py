check_list = []

check_list.append(1)

#check_list == [1]

#스터디카페 완전 초기화(완전 처음)
seat1 = Seat(1)
seat2 = Seat(2)
seat3 = Seat(3)
seat_list = [seat1, seat2, seat3]

#체크인을 했을 때
#체크인 객체를 만들고, 그 옵션 정해주고, seat에 checkin 객체 넣기
new_checkin = Checkin()
position = new_checkin.set_position()
new_checkin.random_number()
new_checkin.set_time()
seat_list[position].checkin = new_checkin
check_list.append(seat_list[position])

#check_list == [seat1]