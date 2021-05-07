class Celebrity:
    def __init__(self, name):
        # 이름
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    def __str__(self):
        return f'이름: {self.name}\t소속사: {self.entertainment}'  # <__main__.Celebrity object at 0x000...>


class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)  # Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'
        # return f'이름: {self.name}\t소속사: {self.entertainment}\t드라마: {self.drama}'


class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)      #self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t노래: {self.song}'

현진 = Singer('현진', '神메뉴')
현진.set_entertainment('JYP')
print(현진)
필릭스 = Singer('필릭스', 'Back Door')
필릭스.set_entertainment('JYP')
print(필릭스)

스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)
for 멤버 in 스트레이키즈:        #i: 현진 객체, 필릭스 객체
    print(멤버)
# for i in range(len(스트레이키즈)):        #i: 0, 1
#     print(스트레이키즈[i])

IU = Celebrity('아이유')  # new Celebrity() in java
# IU.set_name('이지은')
IU.set_entertainment('이담')
# IU.info()
# print(IU.name, IU.entertainment)
print(IU)  # 클래스의 __str__() 호출됨

수지 = Celebrity('배수지')
# 수지.set_name('배수지')
수지.set_entertainment('JYP')
# 수지.info()
print(수지)

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)