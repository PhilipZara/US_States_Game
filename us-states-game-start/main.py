import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv("50_states.csv")
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()


all_states = data.state.to_list()

answer_state = screen.textinput("Guess The States",
                                "What's another state name?").title()

guessed_states = []

while len(guessed_states) < 50:

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

    elif answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]

        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break

    answer_state = screen.textinput("{}/50 states correct".format(len(guessed_states)),
                                    "What's another state name?").title()
