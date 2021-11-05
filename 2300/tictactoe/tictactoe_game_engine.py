class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)  # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):  # FPI 조나현
        for a in range(len(self.board)):
            print(self.board[a], end=' ')
            if a % self.SIZE == self.SIZE - 1:  # * 3줄씩 출력
                print()

    def set(self, row, col):  # 송이김밥 수민
        index = self.SIZE * (row - 1) + (col - 1)
        self.board[index] = self.turn

    def position_to_index(self, row, col):
        return self.SIZE * (row - 1) + (col - 1)

    def set_winner(self):  # 쓰리라프 선우, 서연, 지원
        # - 3줄
        for row in range(1, 3 + 1):  # row: 1~3 반복
            if self.board[self.position_to_index(row, 1)] \
                    == self.board[self.position_to_index(row, 2)] \
                    == self.board[self.position_to_index(row, 3)] \
                    == self.turn:  # '.'일 때, 끝 안나게 하자
                return self.turn
        # | 3줄
        for col in range(1, 3 + 1):  # col: 1~3 반복
            if self.board[self.position_to_index(1, col)] \
                    == self.board[self.position_to_index(2, col)] \
                    == self.board[self.position_to_index(3, col)] \
                    == self.turn:  # '.'일 때, 끝 안나게 하자
                return self.turn
        # \
        if self.board[self.position_to_index(1, 1)] \
                == self.board[self.position_to_index(2, 2)] \
                == self.board[self.position_to_index(3, 3)] \
                == self.turn:
            return self.turn
        # /
        if self.board[self.position_to_index(1, 3)] \
                == self.board[self.position_to_index(2, 2)] \
                == self.board[self.position_to_index(3, 1)] \
                == self.turn:  # '.'일 때, 끝 안나게 하자
            return self.turn
        # return self.turn
        # 비기는 조건: 다 채워졌을 때 위의것에 해당안됐을때: self.board에 '.'이 없는 상태    #스우파 도윤
        if not '.' in self.board:  # self.board 안에 '.'이 없다면
            return 'd'  # draw

    def change_turn(self):  # 모두의 틱택토 설
        # self.turn 'X'면 'O', 'O'면 'X'로 바꾸자
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X'
        self.turn = 'O' if self.turn == 'X' else 'X'


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()  # ...\n...\n...
    game_engine.set(3, 2)
    game_engine.show_board()  # ['.', '.', '.', '.', '.', '.', '.', 'X', '.']
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())  # 'X'
    game_engine.change_turn()
    print(game_engine.turn)  # 'O'
    # 무승부 만들자, 확인하자
    # game_engine.board = ['X', 'O', 'X',
    #                      'O', 'O', 'X',
    #                      'X', 'X', 'O']
    # print(game_engine.set_winner()) #'d'
    game_engine.set(1, 3)
    game_engine.set(2, 2)
    game_engine.set(3, 1)
    print(game_engine.set_winner())  # '/'
