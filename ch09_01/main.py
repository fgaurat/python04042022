from Rectangle import Rectangle


def main():
    r = Rectangle(2,5)
    print(r)
    r1 = Rectangle(22,55)

    r.longueur = 12
    a = r.longueur

    print("longueur",a)

    print("get_longueur",r.longueur) # 12? 
    print(r.surface)
    # s = r.get_surface()
    # print("get_surface",r.get_surface())
    
    # r.longueur = -30
    # r.set_longueur(30)
    
    # print(r.get_longueur())


    str_r = str(r)

    print(r)

if __name__ == '__main__': 
    main()