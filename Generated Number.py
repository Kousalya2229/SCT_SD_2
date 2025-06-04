import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("400x300")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.guess_button = tk.Button(master, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.guess_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="📉 Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="📈 Too high! Try again.")
            else:
                self.result_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} attempts.")
        except ValueError:
            self.result_label.config(text="⚠️ Enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

# Run the app
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
