import pandas as pd


class TicTacToe:

    def __init__(self):
        self.board = pd.DataFrame(
            [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']
            ],
            columns=['a', 'b', 'c'],
            index=[1, 2, 3]
        )
        self.all_moves = []
        self.has_winner = None
        self.winner = None

    def get_move(self, cross):
        while True:
            if cross:
                move = input('-=' * 8 + '\n' + " It's 'X' turn. Say your move: ").lower()
            else:
                move = input('-=' * 8 + '\n' + " It's 'O' turn. Say your move: ").lower()
            if move in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
                move = list(move.strip())
                if self.board[move[0]][int(move[1])] == ' ':
                    break
                else:
                    print("Sorry, they've played in this house before. Try again.")
            else:
                print(f"Sorry, '{move}' is no an option. Say like 'a1', 'b2', 'c3'...")

        self.all_moves.append(move)
        self.play_move(move, cross)

    def show_board(self):
        board = self.board
        print(f"  {board['a'][1]}", '|', f" {board['b'][1]} ",  '|', f"{board['c'][1]}")
        print('-'*15)
        print(f"  {board['a'][2]}", '|', f" {board['b'][2]} ",  '|', f"{board['c'][2]}")
        print('-'*15)
        print(f"  {board['a'][3]}", '|', f" {board['b'][3]} ",  '|', f"{board['c'][3]}")

    def play_move(self, move, cross):
        letter = move[0]
        number = int(move[1])
        if cross:
            self.board.loc[number, letter] = 'X'
        else:
            self.board.loc[number, letter] = 'O'
        self.show_board()
        return True

    def check_winner(self):
        col_concat = self.board['a'].map(str) + self.board['b'].map(str) + self.board['c'].map(str)
        row_concat = [
            self.board['a'][1] + self.board['a'][2] + self.board['a'][3],
            self.board['b'][1] + self.board['b'][2] + self.board['b'][3],
            self.board['c'][1] + self.board['c'][2] + self.board['c'][3],
            self.board['a'][1] + self.board['b'][2] + self.board['c'][3],
            self.board['c'][1] + self.board['b'][2] + self.board['a'][3],
        ]

        for row in col_concat[:]:
            if row == 'XXX':
                self.winner = 'X'
                self.has_winner = True
            if row == 'OOO':
                self.winner = 'O'
                self.has_winner = True
        for col in row_concat:
            if col == 'XXX':
                self.winner = 'X'
                self.has_winner = True
            if col == 'OOO':
                self.winner = 'O'
                self.has_winner = True


if __name__ == '__main__':
    turn = False
    ttt = TicTacToe()
    ttt.show_board()
    while True:
        if ttt.has_winner:
            break
        ttt.get_move(turn)
        ttt.check_winner()
        turn = not turn
    print('-=' * 8)
    print('    End Game!')
    print('-=' * 8)
    print(f"The winner is '{ttt.winner}'")
