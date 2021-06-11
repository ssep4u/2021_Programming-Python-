import room
room_list = [room.show1, room.show2]
def select_floor():
    num = input('방을 선택하세요')
    num = int(num) - 1  #'1' -> 0, '2' -> 1
    room_list[num]()

select_floor()