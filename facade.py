import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    turtle.pensize(0)
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.pendown()
    rectangle(x, y_sol + niveau * 60, 140, 60)
    turtle.end_fill()

if __name__ == '__main__':
    facade(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()