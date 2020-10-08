import turtle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    '''
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

if __name__ == '__main__':
    trait(0,0,100,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()