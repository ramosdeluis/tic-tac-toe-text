from tictactoe import TicTacToe


def play_game():
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


if __name__ == '__main__':
    play_game()
