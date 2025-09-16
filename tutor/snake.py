import turtle
import random
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(False)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(100, 0)

x = turtle.Turtle()
x.shape("square")
x.color("brown")
x.penup()
x.speed(0)

# 랜덤한 위치에 생성
# 뱀이 부딫히면 게임 리셋

def place_food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

body = []

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

def move():
    x = head.xcor()
    y = head.ycor()
    if head.direction == "up":
        head.sety(y+20)
    if head.direction == "down":
        head.sety(y-20)
    if head.direction == "right":
        head.setx(x+20)
    if head.direction == "left":
        head.setx(x-20)

def update_body():
    for i in range(len(body)-1, 0, -1):
        body[i].goto(body[i-1].pos())
    if body:
        body[0].goto(head.pos())

def reset_game():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for b in body:
        b.goto(1000, 1000)
    body.clear()
    score = 0
    update_score()

score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def update_score():
    pen.clear()
    pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

update_score()
place_food()

while True:
    screen.update()
    update_body()
    move()

    if abs(head.xcor()) > 290:
        reset_game()
    if abs(head.ycor()) > 290:
        reset_game()
    
    for b in body:
        if b.pos() == head.pos():
            reset_game()

    if head.pos() == food.pos():
        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        new_body.speed(0)
        body.append(new_body)

        score += 10

        if score > high_score:
            high_score = score
        update_score()

        place_food()
    
    time.sleep(0.05)

'''
실행

1. 임포트
2. 화면 설정 + 머리 오브젝트 + 먹이 오브젝트
3. 키입력 방향 움직임

↓
[무한 게임 루프]
├─ move() ←  헤드 움직임
├─ update_body() ← 몸통 움직임
├─ 충돌 검사
│   ├─ 벽 충돌 → reset_game()
│   └─ 몸통 충돌 → reset_game()
├─ 먹이 (점수획득)
│   ├─ 몸통 추가
│   └─ 점수 업데이트
↓
무한반복

장애물 추가
네모난 갈색 장애물 한개 

'''