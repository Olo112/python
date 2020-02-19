import turtle

# Setting up the line and backround

line = turtle.Turtle()
wn = turtle.Screen()
wn.title("Fibonacci number spiral")
wn.bgcolor("black")
line.color("yellow")

# Let's move our line
# First squares

line.speed(3)
for x in range(3):
    line.forward(50)
    line.left(90)
line.forward(100)



for x in range(3):
    line.left(90)
    line.forward(50)
    
line.right(90)
line.forward(50)

# Second square

line.right(90)
line.forward(150)

for x in range(2):
    line.right(90)
    line.forward(100)

line.forward(50)
line.right(90)
line.forward(100)

# Third square

for x in range(4):
    line.forward(150)
    line.right(90)

line.forward(150)
line.left(90)

# Fourth square

for x in range(4):
    line.forward(250)
    line.left(90)

# And so on...

line.forward(250)
line.left(90)
line.forward(250)

for x in range(3):
    line.forward(400)
    line.left(90)
	
line.right(90)
line.forward(250)

for x in range(3):
	line.right(90)
	line.forward(650)


line.hideturtle()
input("Press enter to finish")
