import turtle

window = turtle.Screen()
window.bgcolor('black')

#colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle.bgcolor('black')

for x in range(150):
    turtle.pencolor(colors[x % 6])
    turtle.forward(x)
    turtle.right(59)

window.exitonclick()
