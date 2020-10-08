from facade import facade
from random import shuffle
from porte import porte
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    '''
    # Dessine la facade
    facade(x, y_sol, c_facade, 0)

    # Construit la liste des éléments (porte ou fenetre)
    liste_element = ["porte","fenetre","fenetre"]
    shuffle(liste_element)

    for i in range (-1,2):
        if liste_element[i] == "porte":  # dessiner une porte
            porte(x+i*40, y_sol, c_porte)
        else:  # dessiner une fenetre
            fenetre(x+i*40, y_sol)

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()