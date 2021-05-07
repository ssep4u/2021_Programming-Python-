class Icecream:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor
        # 이름: name, 맛: flavor, 설명:description

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'


# 아이스홈런볼 = Icecream('아이스홈런볼', '초콜릿, 바닐라, 피넛')
# 아이스홈런볼.set_description('초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!')
# print(아이스홈런볼)
# print(아이스홈런볼.description)
#
# 아빠는딸바봉 = Icecream('아빠는딸바봉', '딸기, 바닐라')
# print(아빠는딸바봉)
#
# 블랙소르베 = Icecream('블랙소르베', '레몬, 라임')
# print(블랙소르베)


class Cup:
    _CUP_CATEGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]

    # Cup._CUP_CATEGORIES[self.count_flovor-1]
    def __init__(self, name, count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor - 1]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        아이스홈런볼 = Icecream('아이스홈런볼', '초콜릿, 바닐라, 피넛')
        아이스홈런볼.set_description('초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!')

        아빠는딸바봉 = Icecream('아빠는딸바봉', '딸기, 바닐라')

        블랙소르베 = Icecream('블랙소르베', '레몬, 라임')
        
        self.menu.append(아이스홈런볼)
        self.menu.append(아빠는딸바봉)
        self.menu.append(블랙소르베)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1, icecream)
    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                    #메뉴 보여주자
            flavor = input('맛을 고르세요: ')     #사용자 선택
            flavor = int(flavor)                #인덱스를 위해 문자 -> 숫자
            icecream = self.menu[flavor - 1]    #메뉴에서 인덱스로 가져오자
            self.order_menu.append(icecream)    #주문한 메뉴에 추가하자
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:        #주문내역 보여주자
            print(icecream)


    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t종류: {Cup._CUP_CATEGORIES[self.count_flavor - 1]}'

# 이지꺼 = Cup('더블컵', 2)
# print(이지꺼)
# 이지꺼.order()

나현이꺼 = Cup('싱글컵', 1)
나현이꺼.order()
print(나현이꺼)
