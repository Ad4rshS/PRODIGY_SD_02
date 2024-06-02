import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        # Initialize game variables
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Set up GUI elements
        self.title_label = tk.Label(master, text="Guess the Number Game", font=("Helvetica", 16, "bold"), bg="lightgray")
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(master, text="I have generated a number between 1 and 100. Can you guess what it is?", font=("Helvetica", 12), bg="lightgray")
        self.instructions_label.pack(pady=10)

        self.guess_label = tk.Label(master, text="Enter your guess:", font=("Helvetica", 12), bg="lightgray")
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(master, font=("Helvetica", 12))
        self.guess_entry.pack(pady=10)

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(master, textvariable=self.result_var, font=("Helvetica", 12), bg="lightgray")
        self.result_label.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=("Helvetica", 12, "bold"), bg="blue", fg="white")
        self.guess_button.pack(pady=20)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, font=("Helvetica", 12, "bold"), bg="red", fg="white")
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                self.result_var.set("Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.result_var.set("Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.result_var.set("Invalid input. Please enter an integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightgray")
    app = GuessTheNumberApp(root)
    root.mainloop()
