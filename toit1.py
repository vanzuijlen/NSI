import turtle

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    y = y_sol + niveau * 60
    turtle.penup()
    turtle.goto(x-80, y)
    turtle.pensize(0)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(x+80, y)
    turtle.goto(x, y+40)
    turtle.goto(x-80, y)
    turtle.end_fill()

if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()