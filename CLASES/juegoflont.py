import turtle
import time

ventana = turtle.Screen()
ventana.title("Juego Froton")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)

jugador = turtle.Turtle()
jugador.shape("square")
jugador.color("white")
jugador.shapesize(stretch_wid=1, stretch_len=5)
jugador.penup()
jugador.goto(0, -250)

pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("green")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 4
pelota.dy = -4

puntuacion = 0

alerta = turtle.Turtle()
alerta.color("yellow")
alerta.penup()
alerta.speed(0)
alerta.goto(0, 0)
alerta.hideturtle()

texto = turtle.Turtle()
texto.color("white")
texto.penup()
texto.speed(0)
texto.goto(0, 260)
texto.hideturtle()
texto.write("Puntuación: 0", align="center", font=("Courier", 24, "normal"))

def mover_jugador_izquierda():
    x = jugador.xcor()
    if x > -240:
        jugador.setx(x - 40)

def mover_jugador_derecha():
    x = jugador.xcor()
    if x < 240:
        jugador.setx(x + 40)

ventana.listen()
ventana.onkeypress(mover_jugador_izquierda, "Left")
ventana.onkeypress(mover_jugador_derecha, "Right")

while True:
    ventana.update()
    time.sleep(0.01)

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    if pelota.xcor() > 290 or pelota.xcor() < -290:
        pelota.dx *= -1

    if pelota.ycor() > 290:
        pelota.dy *= -1

    if (pelota.ycor() < -235 and pelota.ycor() > -245) and (pelota.xcor() < jugador.xcor() + 55 and pelota.xcor() > jugador.xcor() - 55):
        pelota.sety(-235)
        pelota.dy *= -1
        puntuacion += 1
        texto.clear()
        texto.write(f"Puntuación: {puntuacion}", align="center", font=("Courier", 24, "normal"))

    if pelota.ycor() < -290:
        alerta.write("¡Game Over!", align="center", font=("Courier", 24, "normal"))
        ventana.update()
        

        time.sleep(4)

        alerta.clear()
        pelota.goto(0, 0)
        pelota.dy *= -1
        puntuacion = 0
        texto.clear()
        texto.write(f"Puntuación: {puntuacion}", align="center", font=("Courier", 24, "normal"))