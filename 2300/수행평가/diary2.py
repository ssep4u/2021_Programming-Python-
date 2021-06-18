class Diary:
    def __init__(self, moji):
        self.moji = moji

    def __str__(self):
        return 'Diary: ' + self.moji

d1 = Diary('^^')    #1
d11 = Diary('^^')
d2 = Diary('^^;')   #2
d3 = Diary('^^a')   #4 customizing

diary_list = [d1, d11, d2, d3]

def count_setting():
    count1 = 0
    count2 = 0
    for diary in diary_list:
        print(diary)
        if diary.moji == '^^':
            count1 += 1
        elif diary.moji == '^^;':
            count2 +=1
    print('^^: ', count1)
    print('^^;: ', count2)

def count_customize():
    #빈 dict 만들자
    count_dict = {}
    for diary in diary_list:
        moji = diary.moji
        #moji 꺼내서 없으면 키로 등록 값은 1
        if not moji in count_dict:  #count_dict의 key 들에 moji 가 있는지 확인하고 not
            count_dict[moji] = 1
        #키가 있으면 값 += 1
        else:
            count_dict[moji] += 1

    print(count_dict)

count_customize()




















