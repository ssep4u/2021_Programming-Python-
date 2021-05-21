def print_menu():
    print('1. 레시피 검색')
    print('2. 레시피 추가')
    print('3. 재료 검색')
    print('4. 레시피 모음')
    print('5. 종료')
    menu = input('>> 메뉴를 선택하세요: ')
    return menu

def main():
    while True:
        menu = print_menu()
        if menu == '1':
            return
            # 레시피 검색
        elif menu == '2':
            return
            # 레시피 추가
        elif menu == '3':
            return
            # 재료 검색
        elif menu == '4':
            return
            # 레시피 모음
        elif menu == '5':
            break
        else:
            print('다시 입력하세요.')

