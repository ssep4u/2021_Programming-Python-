from tictactoe_game_engine import TictactoeGameEngine


class TictactoeConsole:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        # show board
        self.game_engine.show_board()
        # 무한반복
        while True:
            #  input row, col
            row = int(input('행: '))
            col = int(input('열: '))
            #  set row, col
            self.game_engine.set(row, col)
            #  show board
            self.game_engine.show_board()
            #  set winner
            winner = self.game_engine.set_winner()
            #  승자가 있거나 무승부 일 때, 게임 오버, 결과 출력하자
            if winner == 'X' or winner == 'O':
                print(f'{winner} 이김!!! ㅊㅊ🎊')
                break
            elif winner == 'd':
                print('무승부!!! 🎎')
                break
            #  change turn
            self.game_engine.change_turn()


if __name__ == '__main__':
    ttt_console = TictactoeConsole()
    ttt_console.play()