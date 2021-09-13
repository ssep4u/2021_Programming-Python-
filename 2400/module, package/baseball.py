from baseball_game_engine import make_answer, check
from custom_error import InvalidLengthError

answer = make_answer()
# print(answer)
#무한반복
while True:
#  숫자 묻자
    guess = input("뭘까?")
    #숫자인지 아닌지 확인하자
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):   #3
        # raise InvalidLengthError('정답의 길이와 다른 것을 입력했네요')
        print(f'정답의 길이와 다른 것을 입력했네요. {len(answer)} 문자')
        continue

#  strike, ball 판정하자
    strike, ball = check(guess, answer)
#  출력하자
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
#  정답 == 숫자, 끝내자
    if answer == guess:
        print('정답입니다.')
        break