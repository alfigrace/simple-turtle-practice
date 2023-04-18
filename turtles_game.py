import turtle
import random

window = turtle.Screen()
window.bgcolor('black')

player1 = turtle.Turtle()
player1.color('red')
player1.shape('turtle')
player1.penup()
player1.goto(-250, 100)

player2 = player1.clone()
player2.color('white')
player2.penup()
player2.goto(-250, -100)

player1.goto(350, 60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-250, 100)

player2.goto(350, -140)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-250, -100)

dice = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if player1.pos() >= (300, 100):
        print("Red wins!")
        break
    elif player2.pos() >= (300, -100):
        print("White wins!")
        break
    else:
        player1_turn = input("Press enter to roll the dice: ")
        dice_outcome = random.choice(dice)
        print("The dice: ", dice_outcome)
        print("Number of steps: ", 20*dice_outcome)
        player1.fd(20*dice_outcome)

        player2_turn = input("Press enter here: ")
        dice_outcome = random.choice(dice)
        print("The dice: ", dice_outcome)
        print("Number of steps: ", 20*dice_outcome)
        player2.fd(20*dice_outcome)

window.exitonclick()
