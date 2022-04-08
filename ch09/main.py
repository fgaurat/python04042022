from Rectangle import Rectangle


def main():
    r = Rectangle(2,5)
    r1 = Rectangle(22,55)
    a = r.get_longueur()
    print("get_longueur",a)
    r.set_longueur(12)
    print("get_longueur",r.get_longueur()) # 12? 

    s = r.get_surface()
    print("get_surface",r.get_surface())
    
    r.longueur = -30
    r.set_longueur(30)
    
    print(r.get_longueur())

if __name__ == '__main__': 
    main()