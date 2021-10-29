class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)  #['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):       #FPI 조나현
        print(self.board)

    def set(self, row, col):    #송이김밥 수민
        pass

    def set_winner(self):       #쓰리라프 선우
        # - 3줄
        # | 3줄
        # \
        # /
        return self.turn
        #비기는 조건: 다 채워졌을때 위의것에 해당안됐을때: self.board에 '.'이 없는 상태    #스우파 도윤
        return 'd'  #draw

    def change_turn(self):  #모두의 틱택토 설
        #self.turn 'X'면 'O', 'O'면 'X'로 바꾸자
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X'
        self.turn = 'O' if self.turn == 'X' else 'X'

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()        # ...\n...\n...
    game_engine.set(3, 2)
    game_engine.show_board()        #['.', '.', '.', '.', '.', '.', '.', 'X', '.']
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner()) #'X'
    game_engine.change_turn()
    print(game_engine.turn)     #'O'