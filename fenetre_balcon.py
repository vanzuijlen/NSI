import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    '''
    turtle.penup()
    turtle.goto(x-15,y)
    turtle.pensize(1)
    # porte-fenetre
    turtle.fillcolor('#eef')
    turtle.begin_fill()
    rectangle(x,y,30,50)
    turtle.end_fill()
    # balcon
    turtle.pensize(3)
    for i in range(0,9):
        trait(x-20+i*5,y,x-20+i*5,y+25)
    trait(x-20,y,x+20,y)
    trait(x-20,y+25,x+20,y+25)

if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()