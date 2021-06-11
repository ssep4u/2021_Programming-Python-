import room

def select_floor():
    num = input('방을 선택하세요')
    if num == '1':
        print('죽음')
    elif num == '2':
        room.show()

select_floor()