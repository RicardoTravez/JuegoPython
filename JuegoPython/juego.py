import turtle
import os
import random

#variables
contador = 0

#buncion que busca la carpeta de las imagenes
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)

#creamos la ventana
rt = turtle.Screen()
rt.title("Transformaciones Majin Buu")
rt.setup(width = 600, height = 600)
rt.bgcolor('white')

#imagenes del juego
image = resource_path("cara.gif")
pizza = resource_path('pizza.gif')
img1 = resource_path('pi1.gif')
img2 = resource_path('pi2.gif')
img3 = resource_path('pi3.gif')
img4 = resource_path('pi4.gif')

#cargar las imagenes
rt.addshape(image)
rt.addshape(pizza)
rt.addshape(img1)
rt.addshape(img2)
rt.addshape(img3)
rt.addshape(img4)

#cabeza del jugador
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape(image)
cabeza.penup()
cabeza.goto(122,-100)
cabeza.direction = 'stop'

#cuerpo del jugador
cuerpo = turtle.Turtle()
cuerpo.speed(0)
cuerpo.shape(img1)
cuerpo.penup()
cuerpo.goto(125,-220)
cuerpo.direction = 'stop'

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape(pizza)
comida.penup()
comida.goto(-100,80)
comida.direction = 'stop'

#funciones
def arriba():
    cabeza.sety(cabeza.ycor() + 20)
    cuerpo.sety(cuerpo.ycor() + 20)

def abajo():
    cabeza.sety(cabeza.ycor() - 20)
    cuerpo.sety(cuerpo.ycor() - 20)

def izquierda():
    cabeza.setx(cabeza.xcor() - 20)
    cuerpo.setx(cuerpo.xcor() - 20)

def derecha():
    cabeza.setx(cabeza.xcor() + 20)
    cuerpo.setx(cuerpo.xcor() + 20)

#escuchar teclado
rt.listen()
rt.onkeypress(arriba, 'Up')
rt.onkeypress(abajo, 'Down')
rt.onkeypress(izquierda, 'Left')
rt.onkeypress(derecha, 'Right')

#mostrar en la pantalla
while True:
    rt.update()

    #interseccion con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        contador = contador + 1
        comida.goto(x,y)
        
    #cambio del cuerpo
    if 1 <= contador < 3: cuerpo.shape(img1)
    if 3 <= contador < 5: cuerpo.shape(img2)
    if 5 <= contador < 7: cuerpo.shape(img3)
    if 9 <= contador: cuerpo.shape(img4)
