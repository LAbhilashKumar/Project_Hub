import tkinter as tk
import random
import warnings


warnings.simplefilter("ignore")
remaining_list = []

def button_clicked(button, pressed_button):  # button name , button number
    if Check_winner():
        return
    elif button["text"] == "":
        print("in if block in button_clicked")
        button.config(text="X")
        if Check_winner():
            return

        remaining_list.append(pressed_button)
        print(remaining_list)

        Computer_choice(remaining_list)


def Computer_choice(remaining_list):
    choice = random.randint(1, 9)
    if Check_winner():
        return
    elif choice not in remaining_list:
        button = get_key(choice)
        # if  curr_time - Computer_time >= 3:
        button.config(text="O")
        Check_winner()
        remaining_list.append(choice)
    else:
        Computer_choice(remaining_list)

    # global  Computer_time =time.time()


def get_key(choice):
    buttons = {
        1: button1,
        2: button2,
        3: button3,
        4: button4,
        5: button5,
        6: button6,
        7: button7,
        8: button8,
        9: button9
    }
    return buttons.get(choice)


def restart_button():
    global remaining_list
    remaining_list=[]
    for i in [button1,button2,button3,button4,button5,button6,button7,button8,button9]:
        i.config(text="",bg="grey")


    pass





def Check_winner():

    # horizontal
    if button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or button1["text"] == "O" and \
            button4["text"] == "O" and button7["text"] == "O":
        button1.config(background="green"), button4.config(background="green"), button7.config(
            background="green")  # left
        return True
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or button2["text"] == "O" and \
            button5["text"] == "O" and button8["text"] == "O":
        button2.config(background="green"), button5.config(background="green"), button8.config(
            background="green")  # center
        return True
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or button3["text"] == "O" and \
            button6["text"] == "O" and button9["text"] == "O":
        button3.config(background="green"), button6.config(background="green"), button9.config(
            background="green")  # right
        return True

    # vertical
    elif button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or button1["text"] == "O" and \
            button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="green"), button2.config(bg="green"), button3.config(bg="green")  # top
        return True

    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or button4["text"] == "O" and \
            button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg="green"), button5.config(bg="green"), button6.config(bg="green")  # middle
        return True

    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or button7["text"] == "O" and \
            button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="green"), button8.config(bg="green"), button9.config(bg="green")  # bottom
        return True
    # diagonal

    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or button1["text"] == "O" and \
            button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="green"), button5.config(bg="green"), button9.config(bg="green")  # left to right
        return True

    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or button3["text"] == "O" and \
            button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="green"), button5.config(bg="green"), button7.config(bg="green")  # middle
        return True

    return False
Current_player="user"

window = tk.Tk()
window.title("Tic-Tac-Toe...")
window.geometry("450x550")
window.resizable(0, 0)
window.config(bg="black")



frame = tk.Frame(window)
frame.pack()
# frame.config(bg="grey")
label = tk.Label(frame, text="Your mark:X", font=("consolas", 15, "bold"), bg="black", foreground="white",
                 width=16, height=3)
label.grid(row=0, column=1,sticky="es",pady=5)

button1 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), background="grey",
                    command=lambda: button_clicked(button1, 1))
button1.grid(row=1, column=0, padx=15, pady=15)
button2 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), background="grey",
                    command=lambda: button_clicked(button2, 2))
button2.grid(row=1, column=1, padx=15, pady=15)
button3 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), background="grey",
                    command=lambda: button_clicked(button3, 3))
button3.grid(row=1, column=2, padx=15, pady=15)

button4 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: button_clicked(button4, 4))
button4.grid(row=2, column=0)
button5 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: button_clicked(button5, 5))
button5.grid(row=2, column=1)
button6 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: button_clicked(button6, 6))
button6.grid(row=2, column=2)

button7 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: button_clicked(button7, 7))
button7.grid(row=3, column=0, padx=15, pady=15)
button8 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: button_clicked(button8, 8))
button8.grid(row=3, column=1, padx=15, pady=15)
button9 = tk.Button(frame, text="", width=6, height=3, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: button_clicked(button9, 9))
button9.grid(row=3, column=2, padx=15, pady=15)

Restart = tk.Button(frame, text="Restart", width=7, height=1, font=("consolas", 20, "bold"), bg="grey",
                    command=lambda: restart_button())
Restart.grid(row=4, column=1)
window.mainloop()
