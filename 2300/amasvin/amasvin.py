class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')

    def __init__(self, name, price):  # 생성자
        self.name = name
        self.price = price
        self.cup = 0    #Drink._CUPS[0] => '레귤러', Drink._CUPS[1] => '점보'
        self.ice = 2    #100%   Drink._ICES[2]
        self.sugar = 2  #100%   Drink._SUGARS[2]

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):   #컵의 종류 보여주자
            print(f'{index + 1}: {cup}')
        cup = input('컵사이즈를 선택하세요: ')   #컵 종류 선택하자
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup) - 1
            self.cup = cup  #self.cup에 넣자
        if self.cup == 1:   #점보일때 +500원
            self.price += 500
        self.set_ice()

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):  #얼음량 종류 보여주자
            print(f'{index + 1}: {ice}')
        ice = input('얼음량을 선택하세요: ') #얼음량 선택하자
        if ice == '0':
            self.set_cup()
            return
        self.ice = 2 if ice == '' else int(ice) - 1 #self.ice에 넣자
        # if ice == '':   #self.ice에 넣자
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1
        self.set_sugar()

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):   #당도 선택사항 보여주자
            print(f'{index + 1}: {sugar}')
        sugar = input('당도를 선택하세요: ')               #당도 선택하자
        if sugar == '0':    #이전 질문으로...
            self.set_ice()
            return
        self.sugar = 2 if sugar == '' else int(sugar) - 1 #self.sugar에 넣자

    def order(self):
        self.set_cup()
        # self.set_ice()
        # self.set_sugar()

    def __str__(self):  # 스트링=문자열 리턴
        return f'이름: {self.name}\t가격: {self.price}원' \
            + f'\t컵사이즈: {Drink._CUPS[self.cup]}' \
            + f'\t얼음량: {Drink._ICES[self.ice]}' \
            + f'\t당도: {Drink._SUGARS[self.sugar]}'




class Coffee(Drink):
    pass

# 수민이꺼 = Coffee('초코버블티', 3300)
# 수민이꺼.order()
# print(수민이꺼)

class Bubbletea(Drink):
    _PEALRS = ('타피오카', '코코', '젤리', '알로에')

    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0       #'타피오카', '코코', '젤리', '알로에'

    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEALRS):  #펄 종류 보여주자
            print(f'{index + 1}: {pearl}')
        pearl = input('펄을 선택하세요: ')#펄 선택하자
        self.pearl = 0 if pearl == '' else int(pearl) - 1   #self.pearl에 넣자

    def __str__(self):
        return super().__str__() + f'\t펄: {Bubbletea._PEALRS[self.pearl]}'

    def order(self):
        super().order()
        self.set_pearl()


class Order:
    def __init__(self):
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def init_menu(self):
        drink1 = Coffee('아메리카노', 1800)
        drink2 = Bubbletea('하동녹차오레오', 3300)
        drink3 = Bubbletea('딸기요거트', 3400)
        self.menu.append(drink1)
        self.menu.append(drink2)
        self.menu.append(drink3)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink.name}\t{drink.price}원')

    def order_drink(self):
        while True: #반복 시작
            self.show_menu()  # 메뉴 보여주자
            drink = input('메뉴를 선택하세요: ') #메뉴 선택하자
            drink = int(drink) - 1
            new_drink = self.menu[drink]
            new_drink.order()   #  옵션 선택하자
            self.order_menu.append(new_drink)   #  self.order_menu에 추가하자
            is_add = input('더 주문하실까요?(n: 끝): ')#  더 주문?
            if is_add == 'n':   #반복 끝
                break
        print(self) #총가격 계산하고, 주문내역 보여주자    자기의 __str__() 호출
    def sum_price(self):
        total_price = 0
        for drink in self.order_menu:   #self.order_menu에서 하나씩 꺼내자
            total_price += drink.price  #음료수.price의 합계를 구하자
        return total_price

    def __str__(self):      #주문 내역
        s = '-' * 20 + '주문 내역' + '-' * 20 + '\n'   #주문내역입니다. 제목 보여주자
        for drink in self.order_menu:   #self.order_menu에 있는 음료수 목록 보여주자
            s += f'{drink}\n'   #str(drink)
        s += f'주문한 음료수 개수: {len(self.order_menu)}개\n'
        s += f'총 가격: {self.sum_price()}원'   #총가격 보여주자
        return s

order = Order()
order.order_drink()