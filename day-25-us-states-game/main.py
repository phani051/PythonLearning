import turtle, pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
sname = turtle.Turtle()
sname.penup()
sname.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
print(states_list)

correct_answers = []

while len(correct_answers) < 50:

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 Correct States", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_state = []
        for state in states_list:
            if state not in correct_answers:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("State_to_learn.csv")
        break
    for a in states_list:
        if a == answer_state:
            correct_answers.append(a)
            print(a)
            state_data = data[data.state == a]
            # x_cor = data[data.state == a]['x'].to_list()[0]
            # y_cor = data[data.state == a]['y'].to_list()[0]
            print(state_data.x, state_data.y)
            sname.goto(int(state_data.x), int(state_data.y))
            sname.write(a, align="center", font=("Arial", 8, "normal"))
        else:
            continue




