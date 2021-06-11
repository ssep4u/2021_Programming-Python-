import room
room_list = [room.show1(), room.show2()]
def select_floor():
    num = input('방을 선택하세요')
    if num == '1':
        room.show1()
    elif num == '2':
        room.show2()

select_floor()