import turtle
from rectangle import rectangle

def porte(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    '''
    turtle.pensize(1)
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()

if __name__ == '__main__':
    porte(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()