import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_list = []

while len(guessed_list) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 Guess the State", prompt="Name a State").title()
    print(answer_state)

    # If answer_state is one of the states in all of the states in 50_states.csv
    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_list:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


