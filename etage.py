from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
        Cette fonction a été codée avec un liste de fonction !
    '''
    # Murs
    facade(x, y_sol, couleur, niveau)
    # Eléments
    liste_elements_etage = ["fenetre", "fenetre_balcon"]
    for i in range(-1,2):
        numero_element=randint(0,1)
        if liste_elements_etage[numero_element]=="fenetre":
            fenetre(x+i*40, y_sol + niveau*60)
        else:
            fenetre_balcon(x+i*40, y_sol + niveau*60)

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()