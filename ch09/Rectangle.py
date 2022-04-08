
class Rectangle:
    def __init__(self,longueur,largeur) -> None:
        print(f"def __init__(self,{longueur=},{largeur=})")
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self,p):
        self._longueur = p

    def set_largeur(self,p):
        self._largeur = p

    def get_surface(self):
        return self._longueur * self._largeur