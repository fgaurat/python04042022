
class Rectangle:
    def __init__(self,longueur,largeur) -> None:
        print(f"def __init__(self,{longueur=},{largeur=})")
        self._longueur = longueur
        self._largeur = largeur
    
    def __str__(self) -> str:
        return f"Rectangle : {self.get_longueur()},{self.largeur}"



    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,p):
        self._longueur = p
    
    @largeur.setter
    def largeur(self,p):
        self._largeur = p

    @property
    def surface(self):
        return self._longueur * self._largeur

    
    def __del__(self):
        print("def __del__(self)")
    

