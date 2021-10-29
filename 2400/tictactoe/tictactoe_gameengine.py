class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)  #['.','.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self):       #김유임 임사랑
        print(self.board)

    def set(self, row, col):    #티크태크토크 정나라
        pass

    def set_winner(self):
        # 클링이2김1박1 이지민
        #- 3줄
        #| 3줄

        # 포피포피 양가영
        #/
        #\
        #무승부: 위의 조건 다 통과
        # , 더이상 놓을 자리가 없음: self.board에 빈칸이 없음: self.board에 '.' 없음
        return 'd'  #draw

        pass

    def change_turn(self):  #와르르 전유리
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()    #...\n...\n...
    game_engine.set(2, 2)
    game_engine.show_board()    #['.', '.', '.', '.', 'X', '.', '.', '.', '.']
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()  # ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()  # '-'  -> 'X'
    game_engine.change_turn()
    print(game_engine.turn)     #'O'
    game_engine.change_turn()
    print(game_engine.turn)  # 'X'





