from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    '''
    turtle.pensize(1)
    turtle.fillcolor('#eef')
    turtle.begin_fill()
    rectangle(x,y+20,30,30)
    turtle.end_fill()

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()