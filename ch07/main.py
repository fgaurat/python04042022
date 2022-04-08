def main():
    age = 45 
    name = "GAURAT"
    first_name = "fred"
    s = f"{name=} {first_name=} {age=}"
    print(s)

    s = "{1} {0} {2}".format(name,first_name,age)
    print(s)
    v1 = 45 
    v2 = "GAURAT"
    v3 = "fred"
    s = "{name} {first_name} {age}".format(name=v2,first_name=v3,age=v1)

    the_values=["GAURAT","fred",45]

    s = "{1} {0} {2}".format(*the_values)
    print(s)

    info = {
        "age" : 45, 
        "name":"GAURAT",
        "first_name":"fred"
    }
    s = "{name} {first_name} {age}".format(**info)
    # s = "{name} {first_name} {age}".format(name="GAURAT",first_name="fred",age="45")
    print(s)
    s = f"{info['name']} {info['first_name']=} {info['age']=}"
    print(s)
    print(50*'-')
    a = 2
    b = 3
    c = a/b
    print(f"{a:>9}/{b:<9} = {c=:.2%}")
    a = 2000
    b = 30000
    c = a/b
    print(f"{a:<9}/{b:<9} = {c=:.2%}")




if __name__ == '__main__':
    main()