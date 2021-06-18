class GooDS:
    def __init__(self, name, popular):
        self.popular = popular
        self.name = name

    def __str__(self):
        return f'{self.name} {self.popular}'

goods_list = [GooDS('칼날', 5), GooDS('귀멸', 2), GooDS('의', 3)]


def show_popular(goods_list):
    popular_list = []
    for goods in goods_list:
        if goods.popular > 2:
            popular_list.append(goods)
    return popular_list


print(show_popular(goods_list))
