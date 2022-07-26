class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[None]*3 for _ in range(3)]

    def print_board(self):
        for row in self.board:
            for cell in row:
                print('|', end=' ')
                if cell:
                    print(cell, end=' ')
                else:
                    print(" ", end=' ')
                print('|', end=' ')
            print()
            print('- '*9)

    def ask_move(self, player):
        while True:
            move = int(input(f'{player.name} please select a box: '))
            if move in [1,2,3]:
                if not self.board[0][move-1]:
                    self.board[0][move-1] = player.choice
                    break
            elif move in [4,5,6]:
                if not self.board[1][move-4]:
                    self.board[1][move-4] = player.choice
                    break
            elif move in [7,8,9]:
                if not self.board[2][move-7]:
                    self.board[2][move-7] = player.choice
                    break
            print('The box is already taken!')

    def check_diagonal(self, player):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player.choice or \
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player.choice:
            return True
        return False

    def check_win(self, player):
        for a in range(3):
            for b in range(3):
                if self.board[a][0] == self.board[a][1] == self.board[a][2] == player.choice or \
                    self.board[0][a] == self.board[1][a] == self.board[2][a] == player.choice or \
                        self.check_diagonal(player):
                    print(f"{player.name} won!")
                    return True

        return False

    def is_board_full(self):
        for rows in self.board:
            for cell in rows:
                if not cell:
                    return False

        return True
