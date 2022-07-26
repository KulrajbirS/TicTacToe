from Player import Player
from TicTacToe import TicTacToe

if __name__ == "__main__":
    player1 = Player()
    player2 = Player()
    tictactoe = TicTacToe(player1, player2)
    tictactoe.print_board()
    while True:
        tictactoe.ask_move(player1)
        tictactoe.print_board()
        if tictactoe.check_win(player1):
            break
        if tictactoe.is_board_full():
            print("Tied!")
            break
        tictactoe.ask_move(player2)
        tictactoe.print_board()
        if tictactoe.check_win(player2):
            break
