import turtle
import pandas
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

def state(x, y):
    states = turtle.Turtle()
    states.penup()
    states.hideturtle()
    states.goto(x, y)
    states.write(answer)
    states.goto(x, y)

time = 0
while time != 50:
    answer = screen.textinput('guess state', f"your guess? 50/{time}").title()

    if answer == "exit":
        print("\ngoodbye!")
        break


    elif answer not in data['state'].values:
        print("not in state")


    else:
        states = data[data["state"] == answer]
        x = states["x"].values
        y = states["y"].values
        x_int = x[0]
        y_int = y[0]
        state(x_int, y_int)
        time += 1


print("\nwell done!\n")

screen.bye()
