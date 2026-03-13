import turtle
import time

ventana = turtle.Screen()
ventana.title("Breakout 2vs2")
ventana.bgcolor("#04102c")
ventana.setup(width=600, height=800)
ventana.tracer(0)

jugador1 = turtle.Turtle()
jugador1.shape("square")
jugador1.color("blue")
jugador1.shapesize(stretch_wid=1, stretch_len=5)
jugador1.penup()
jugador1.goto(0, -350)

jugador2 = turtle.Turtle()
jugador2.shape("square")
jugador2.color("blue")
jugador2.shapesize(stretch_wid=1, stretch_len=5)
jugador2.penup()
jugador2.goto(0, 350)

borde  = turtle.Turtle()
borde.hideturtle()
borde.speed(0)
borde.color("white")
borde.pensize(4)
borde.penup()
borde.goto(-293, -385)
borde.pendown()

for _ in range(2):
    borde.forward(580)
    borde.left(90)
    borde.forward(780)
    borde.left(90)

linea = turtle.Turtle()
linea.color("white")
linea.penup()
linea.goto(-390, 0) 
linea.setheading(0)

for i in range(90):
    linea.pendown()
    linea.forward(20)
    linea.penup()
    linea.forward(20)


pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 4
pelota.dy = -4

puntuacion1 = 0
puntuacion2 = 0

alerta = turtle.Turtle()
alerta.color("gold")
alerta.penup()
alerta.speed(0)
alerta.goto(0, 0)
alerta.hideturtle()

texto1 = turtle.Turtle()
texto1.hideturtle()
texto1.speed(0)
texto1.color("white")
texto1.penup()
texto1.goto(-250, -320)

texto1.write("J1: 0", align="left", font=("Verdana", 28, "bold"))

texto2 = turtle.Turtle()
texto2.hideturtle()
texto2.speed(0)
texto2.color("white")
texto2.penup()
texto2.goto(250, 290)

texto2.write("J2: 0", align="right", font=("Verdana", 28, "bold"))


def mover_jugador1_izquierda():
    x = jugador1.xcor()
    if x > -240:
        jugador1.setx(x - 40)

def mover_jugador1_derecha():
    x = jugador1.xcor()
    if x < 240:
        jugador1.setx(x + 40)

def mover_jugador2_izquierda():
    x = jugador2.xcor()
    if x > -240:
        jugador2.setx(x - 40)

def mover_jugador2_derecha():
    x = jugador2.xcor()
    if x < 240:
        jugador2.setx(x + 40)

ventana.listen()
ventana.onkeypress(mover_jugador1_izquierda, "Left")
ventana.onkeypress(mover_jugador1_derecha, "Right")
ventana.onkeypress(mover_jugador2_izquierda, "a")
ventana.onkeypress(mover_jugador2_derecha, "d")

while True:
    ventana.update()
    time.sleep(0.01)

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)  

    if pelota.xcor() > 290 or pelota.xcor() < -290:
        pelota.dx *= -1
    
    if pelota.ycor() > 380:
        pelota.dy *= -1

    if (pelota.ycor() < -330 and pelota.ycor() > -360) and (pelota.xcor() < jugador1.xcor() + 50 and pelota.xcor() > jugador1.xcor() - 50):
        pelota.sety(-330)
        pelota.dy *= -1
        puntuacion1 += 1
        texto1.clear()
        texto1.write(f"J1: {puntuacion1}", align="left", font=("Verdana", 28, "bold"))
        texto2.clear()
        texto2.write(f"J2: {puntuacion2}", align="right", font=("Verdana", 28, "bold"))
    
    if pelota.ycor() < -380:
        alerta.write("¡🏆 Jugador 2 gana!", align="center", font=("Verdana", 35, "bold"))
        ventana.update()

        time.sleep(4)

        alerta.clear()
        pelota.goto(0, 0)
        pelota.dy *= -1
        puntuacion1 = 0
        puntuacion2 = 0
        texto1.clear()
        texto1.write(f"J1: {puntuacion1}", align="left", font=("Verdana", 28, "bold"))
        texto2.clear()
        texto2.write(f"J2: {puntuacion2}", align="right", font=("Verdana", 28, "bold"))
    
    if (pelota.ycor() > 330 and pelota.ycor() < 360) and (pelota.xcor() < jugador2.xcor() + 50 and pelota.xcor() > jugador2.xcor() - 50):
        pelota.sety(330)
        pelota.dy *= -1
        puntuacion2 += 1
        texto1.clear()
        texto1.write(f"J1: {puntuacion1}", align="left", font=("Verdana", 28, "bold"))
        texto2.clear()
        texto2.write(f"J2: {puntuacion2}", align="right", font=("Verdana", 28, "bold"))

    if pelota.ycor() > 380:
        alerta.write("¡🏆 Jugador 1 gana!", align="center", font=("Verdana", 35, "bold"))
        ventana.update()

    
        time.sleep(4)

        alerta.clear()
        pelota.goto(0, 0)
        pelota.dy *= -1
        puntuacion1 = 0
        puntuacion2 = 0
        texto1.clear()
        texto1.write(f"J1: {puntuacion1}", align="left", font=("Verdana", 28, "bold"))
        texto2.clear()
        texto2.write(f"J2: {puntuacion2}", align="right", font=("Verdana", 28, "bold"))
    





