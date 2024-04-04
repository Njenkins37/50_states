import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
write_turtle = turtle.Turtle()

turtle.shape(image)
data = pandas.read_csv('50_states.csv')
guessed_list = []
state_ser = data['state'].str.strip().str.lower()
state_list = state_ser.to_list()

answer = screen.textinput(title="US States", prompt="Type in a US state").lower()

while len(guessed_list) < len(state_list):

    if answer in state_list and answer.title() not in guessed_list:

        guessed_list.append(answer.title())

        state = data[data.state == answer.title()]
        x_cord = state.x.iloc[0]
        y_cord = state.y.iloc[0]

        write_turtle.penup()
        write_turtle.hideturtle()
        write_turtle.goto(x_cord, y_cord)
        write_turtle.write(move=False, arg=answer.title(), font=('Arial', 8, 'normal'))

        answer = screen.textinput(title=f'{len(guessed_list)}/{len(data)} States Guessed', prompt="Type in a US state")

    elif answer.title() in guessed_list:
        answer = screen.textinput(title=f'{len(guessed_list)}/{len(data)} States Guessed',
                                  prompt="You have already guessed that state.")

    else:
        answer = screen.textinput(title=f'{len(guessed_list)}/{len(data)} States Guessed',
                                  prompt="That is not a US State. Try again")



turtle.mainloop()
