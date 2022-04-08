from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo


def affiche(obj:ICalcGeo):
    print("-- affiche --")
    print(obj)
    print(obj.surface)

def main():
    r = Rectangle(longueur=2,largeur=5)
    c = Carre(cote=2)
    print(c.cote)
    print(c.surface)
    print(c)

    affiche(r)
    affiche(c)

    ce = Cercle(5)
    ce.surface



if __name__ == '__main__': 
    main()