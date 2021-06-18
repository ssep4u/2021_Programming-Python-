_HAIRSTYLE = ('컷트', '매직', '파마', '염색')
_PRICE = (10000, 20000, 30000, 40000)

def set_style():
    for index, hairstyle in enumerate(_HAIRSTYLE):
        price = _PRICE[index]
        print(f'{index + 1}: {hairstyle}\t{price}원')