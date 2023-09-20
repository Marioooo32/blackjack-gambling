import tkinter as tk
import random

# Create the window
window = tk.Tk()
window.title("Blackjack")
window.geometry("400x300")

# Create the score labels
user_score = 0
computer_score = 0
user_score_label = tk.Label(window, text="Your Score: 0")
user_score_label.pack()
computer_score_label = tk.Label(window, text="Computer Score: 0")
computer_score_label.pack()

# Create the card labels
user_cards = []
computer_cards = []
user_cards_label = tk.Label(window, text="Your Cards: ")
user_cards_label.pack()
computer_cards_label = tk.Label(window, text="Computer's First Card: ")
computer_cards_label.pack()

# Deal the initial cards
def deal():
    global user_cards, computer_cards, user_score, computer_score
    user_cards = [random.randint(1, 11), random.randint(1, 11)]
    computer_cards = [random.randint(1, 11), random.randint(1, 11)]
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    update_score()
    update_cards()

# Hit the user with another card
def hit():
    global user_cards, user_score
    user_cards.append(random.randint(1, 11))
    user_score = sum(user_cards)
    update_score()
    update_cards()

# Stand and let the computer play
def stand():
    global computer_cards, computer_score
    while computer_score < 17:
        computer_cards.append(random.randint(1, 11))
        computer_score = sum(computer_cards)
    update_cards()
    check_winner()

# Update the score labels
def update_score():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Update the card labels
def update_cards():
    user_cards_label.config(text=f"Your Cards: {user_cards}")
    computer_cards_label.config(text=f"Computer's First Card: {computer_cards[0]}")

# Check the winner and display the result
def check_winner():
    if user_score > 21:
        result = "You went over. You lose!"
    elif computer_score > 21:
        result = "Computer went over. You win!"
    elif user_score == computer_score:
        result = "It's a draw!"
    elif user_score == 21:
        result = "You win with a blackjack!"
    elif computer_score == 21:
        result = "Computer wins with a blackjack!"
    elif user_score > computer_score:
        result = "You win!"
    else:
        result = "You lose!"
    tk.messagebox.showinfo("Result", result)

# Create the buttons
deal_button = tk.Button(window, text="Deal", command=deal)
deal_button.pack()
hit_button = tk.Button(window, text="Hit", command=hit)
hit_button.pack()
stand_button = tk.Button(window, text="Stand", command=stand)
stand_button.pack()

# Add the warning label
warning_label = tk.Label(window, text="You shouldn't play at the casino!")
warning_label.pack()

# Add the made with love label
made_with_love_label = tk.Label(window, text="Made with love by Mario <3", font=("Arial", 16, "bold"))
made_with_love_label.pack()

# Start the game
deal()

# Run the window
window.mainloop()