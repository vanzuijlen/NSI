import  turtle

def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    '''
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(x-15,y)
    turtle.pensize(1)
    turtle.pendown()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.goto(x+15,y)
    turtle.goto(x+15,y+40)
    turtle.circle(15,180)
    turtle.goto(x-15,y+40)
    turtle.goto(x-15,y)
    turtle.end_fill()

if __name__ == '__main__':
    porte2(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()