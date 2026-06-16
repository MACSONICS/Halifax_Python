import turtle

# Step 1: Create the game screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0) # Turn off the screen updates

# Step 2: Create paddles for left and right sides
# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)


# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Step 3: Create the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Step 4: Create the score display
score_left = 0
score_right = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left Player: 0  Right Player: 0", align="center", font=("Courier", 24, "normal"))

# Step 5: Move paddles vertically
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        # Prevent going off the screen
        y += 20
        left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:
        # Prevent going off the screen
        y -= 20
        left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        # Prevent going off the screen
        y += 20
        right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:
        # Prevent going off the screen
        y -= 20
        right_paddle.sety(y)

# Step 6: Keyboard bindings
screen.listen()
screen.onkeypress(left_paddle_up, "w")
# Fixed to ensure it works for left paddle
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")

# Step 7: Game loop
while True:
    screen.update()

# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Check for collision with top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

# Check for collision with paddles
    if (ball.dx > 0 and ball.xcor() > 340 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0 and ball.xcor() < -340 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

# Check for ball going out of bounds
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score_display.clear()
        score_display.write(f"Left Player: {score_left} Right Player: {score_right}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        score_display.clear()
        score_display.write(f"Left Player: {score_left}  Right Player: {score_right}", align="center", font=("Courier", 24, "normal"))
