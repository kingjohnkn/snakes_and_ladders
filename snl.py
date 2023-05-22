import tkinter as tk
from PIL import ImageTk, Image


def start_game():
    global img_roll

    # Buttons for Players
    # Player 1
    b1 = tk.Button(
        root,
        text="Player 1",
        height=1,
        width=10,
        fg="red",
        bg="cyan",
        font=("Cursive", 14, "bold"),
        activebackground="white",
    )
    b1.place(x=1000, y=300)

    # Player 2
    b2 = tk.Button(
        root,
        text="Player 2",
        height=1,
        width=10,
        fg="red",
        bg="orange",
        font=("Cursive", 14, "bold"),
        activebackground="white",
    )
    b2.place(x=1000, y=400)

    # Exit
    b3 = tk.Button(
        root,
        text="Exit",
        height=1,
        width=10,
        fg="white",
        bg="red",
        font=("Cursive", 14, "bold"),
        activebackground="green",
        command=root.destroy,
    )
    b3.place(x=1000, y=50)

    # Dice
    img_roll = Image.open("images/dice.png")
    img_roll = img_roll.resize((65, 65))
    img_roll = ImageTk.PhotoImage(img_roll)
    b4 = tk.Button(
        root,
        image=img_roll,
        height=80,
        width=80,
    )
    b4.place(x=1025, y=150)


root = tk.Tk()
root.geometry("1200x800")
root.title("Snakes and Ladders")

F1 = tk.Frame(root, width=1200, height=800, relief="raised")
F1.place(x=0, y=0)

# Set board
img1 = ImageTk.PhotoImage(Image.open("images/snl_board.png"))
Lab = tk.Label(F1, image=img1)
Lab.place(x=0, y=0)

# Player 1 coin
coin1 = tk.Canvas(root, width=40, height=40)
coin1.create_oval(10, 10, 40, 40, fill="blue")
coin1.place(x=100, y=600)


# Setting Buttons
start_game()

root.mainloop()
