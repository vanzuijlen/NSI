# module immeuble

from couleur_aleatoire import couleur_aleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import turtle

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    '''
    # Nombre d'étage (aléatoire)
    nb_etages = randint(0,4)
    #Couleurs des éléments (aléatoire)
    couleur_facade = couleur_aleatoire()
    couleur_porte = couleur_aleatoire()
    # Dessin du RDC
    rdc(x, y_sol, couleur_facade, couleur_porte)

    # Dessin des étages
    niveau = 1
    while niveau <= nb_etages:
        etage(x, y_sol, couleur_facade,niveau)
        niveau = niveau + 1

    # Dessin du toit
    toit(x, y_sol, niveau)

if __name__ == '__main__':
    immeuble(-10,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()