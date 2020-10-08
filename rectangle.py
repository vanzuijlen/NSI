import turtle

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    '''
    turtle.penup()
    turtle.goto(x-w/2,y)
    turtle.pendown()
    turtle.goto(x+w/2,y)
    turtle.goto(x+w/2,y+h)
    turtle.goto(x-w/2,y+h)
    turtle.goto(x-w/2,y)

if __name__ == '__main__':
    rectangle(0,0,150,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()