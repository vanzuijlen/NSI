import turtle
from random import randint

def couleur_aleatoire():
    turtle.colormode(255)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)