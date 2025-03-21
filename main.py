import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_error(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_error)

guessed_states = []
while True:
    user_answer = screen.textinput(title=f"Guess the states, {len(guessed_states)}/50", prompt="What's another state's name? : ").title()
    data = pd.read_csv("50_states.csv")
    states_name = data.state.to_list()
    if user_answer == "Exit":
        remaining_states =[]
        for state in states_name:
            if state not in guessed_states:
                remaining_states.append(state)
        remaining_df = pd.DataFrame(remaining_states)
        remaining_df.to_csv("left_out_states.csv")
        break

    if len(guessed_states) < 50:
        if user_answer in states_name:
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.color("black")
            pen.penup()
            position = data[data.state == user_answer]
            pen.goto(position.x.item(), position.y.item())
            pen.write(f"{user_answer}", align = "center", font = ("Arial", 7, "normal"))
            guessed_states.append(user_answer)
    else:
        break

turtle.mainloop()

# screen.exitonclick()


