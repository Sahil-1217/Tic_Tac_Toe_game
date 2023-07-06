# import tkinter as tk
# from tkinter import messagebox

# # Create the Tic Tac Toe game class


# class TicTacToe:
#     def _init_(self):
#         self.current_player = 'X'
#         self.board = [[' ' for _ in range(3)] for _ in range(3)]

#     def check_winner(self):
#         # Check rows
#         for row in self.board:
#             if row[0] == row[1] == row[2] != ' ':
#                 return row[0]

#         # Check columns
#         for col in range(3):
#             if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
#                 return self.board[0][col]

#         # Check diagonals
#         if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
#             return self.board[0][0]

#         if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
#             return self.board[0][2]

#         return None

#     def make_move(self, row, col):
#         if self.board[row][col] == ' ':
#             self.board[row][col] = self.current_player
#             return True
#         return False

#     def switch_player(self):
#         if self.current_player == 'X':
#             self.current_player = 'O'
#         else:
#             self.current_player = 'X'


# # Create the GUI window
# window = tk.Tk()
# window.title("Tic Tac Toe")

# # Create the game instance
# game = TicTacToe()

# # Create the buttons
# buttons = []
# for row in range(3):
#     button_row = []
#     for col in range(3):
#         button = tk.Button(window, text=' ', width=10, height=5,
#                            command=lambda r=row, c=col: button_click(r, c))
#         button.grid(row=row, column=col, padx=5, pady=5)
#         button_row.append(button)
#     buttons.append(button_row)


# # Handle button click event
# def button_click(row, col):
#     if game.make_move(row, col):
#         buttons[row][col].config(text=game.current_player)
#         winner = game.check_winner()
#         if winner:
#             messagebox.showinfo("Game Over", "Player " + winner + " wins!")
#             window.quit()
#         else:
#             game.switch_player()


# # Run the GUI main loop
# window.mainloop()
import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.window, text='', font=('Arial', 20), width=5, height=3,
                                                   command=lambda row=row, col=col: self.button_click(row, col))
                self.buttons[row][col].grid(row=row, column=col)

    def button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                messagebox.showinfo(
                    'Game Over', f'Player {self.current_player} wins!')
                self.window.quit()
                return

            if self.check_draw():
                messagebox.showinfo('Game Over', 'It\'s a draw!')
                self.window.quit()
                return

            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True

    def run(self):
        self.window.mainloop()


game = TicTacToeGUI()
game.run()
