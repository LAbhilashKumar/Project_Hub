import tkinter as tk

import random
import pyautogui

SEGEMENT_SIZE = 20
SNAKE = [(100, 100)]
SNAKE_DIRECTION = "Right"
SCORE=0

window = tk.Tk()
window.title("Snake game")
screen_width, screen_height = pyautogui.size()

center_x = (screen_width // 2)
center_y = (screen_height // 2)
# print(center_x,"\n",centersd_y)
x_position = center_x - (screen_width // 2)
y_position = center_y - (screen_height // 2)


window.geometry(f"750x750+{x_position}+{y_position}")
canvas = tk.Canvas(width=750, height=750, bg="black")
window.config(bg="black")
window.resizable(0, 0)
icon_image=tk.PhotoImage(file=r"C:\Users\ABHILASH\Downloads\snake.png")
window.iconphoto(False,icon_image)


def food():
    global food_x, food_y
    food_x = random.randint(0, 720 // SEGEMENT_SIZE) * SEGEMENT_SIZE
    food_y = random.randint(0, 720 // SEGEMENT_SIZE) * SEGEMENT_SIZE
    canvas.create_oval(food_x, food_y, food_x + 15, food_y + 15, tags="food", fill="red",outline="white")
    canvas.pack()


def snake():
    canvas.delete("snake")
    segment = SNAKE
    for x, y in segment:
        canvas.create_rectangle(x, y, x + SEGEMENT_SIZE, y + SEGEMENT_SIZE, tags="snake", outline="white", fill="green")


def move_snake():
    global food_x, food_y,SCORE
    snake_head_x, snake_head_y = SNAKE[0]

    if SNAKE_DIRECTION == "Up":
        new_head = (snake_head_x, snake_head_y - SEGEMENT_SIZE)
    elif SNAKE_DIRECTION == "Down":
        new_head = (snake_head_x, snake_head_y + SEGEMENT_SIZE)
    elif SNAKE_DIRECTION == "Left":
        new_head = (snake_head_x - SEGEMENT_SIZE, snake_head_y)
    elif SNAKE_DIRECTION == "Right":
        new_head = (snake_head_x + SEGEMENT_SIZE, snake_head_y)

    SNAKE.insert(0, new_head)

    if food_x == new_head[0] and food_y == new_head[1]:
        canvas.delete("food")
        food()
        SCORE+=1

    else:
        SNAKE.pop()

    snake()

    if new_head in SNAKE[1:] or new_head[0] < 0 or new_head[0] >= 750 or new_head[1] < 0 or new_head[1] >= 750:
        print(f"Game Over! Your Score: {SCORE}")
        window.quit()
    else:
        window.after(100, move_snake)


def change_direction(new):
    global SNAKE_DIRECTION
    if new == "Up" and SNAKE_DIRECTION != "Down":
        SNAKE_DIRECTION = "Up"
        print("up")
    elif new == "Down" and SNAKE_DIRECTION != "Up":
        SNAKE_DIRECTION = "Down"
        print("Down")
    elif new == "Left" and SNAKE_DIRECTION != "Right":
        SNAKE_DIRECTION = "Left"
        print("left")
    elif new == "Right" and SNAKE_DIRECTION != "Left":
        SNAKE_DIRECTION = "Right"
        print("Right")


window.bind("<Right>", lambda event: change_direction("Right"))
window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))

food()
move_snake()#snake()
window.mainloop()
