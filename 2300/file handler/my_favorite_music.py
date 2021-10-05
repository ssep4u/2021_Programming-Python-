#파일 저장하자
with open('my_favorite_music.txt', 'w', encoding='utf-8') as f:
    f.write('이선우:너를생각해(경서)\n')
    f.write('주서영:낙하(신봉선)\n')

#파일 불러오자
with open('my_favorite_music.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline() #'이선우:너를생각해(경서)\n'
        if line == '':
            break
        #이름: 이선우[Tab]좋아하는 음악: 너를생각해(경서)
        line_list = line.split(':') #['이선우', '너를생각해(경서)\n']
        name = line_list[0]
        music = line_list[1].rstrip()
        print(f'이름: {name}\t좋아하는 음악: {music}')
        #print(line.rstrip())