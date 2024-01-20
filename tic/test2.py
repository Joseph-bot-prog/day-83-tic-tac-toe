import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = ["-" for _ in range(9)]

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == "-":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.show_result()
            elif self.check_tie():
                self.show_result(tie=True)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Implement your logic to check for a winner
        for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "-":
                return True
        return False

    def check_tie(self):
        return "-" not in self.board

    def show_result(self, tie=False):
        if tie:
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            winner = "O" if self.current_player == "X" else "X"
            messagebox.showinfo("Game Over", f"{winner} wins!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
