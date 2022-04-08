

t1,t2 = "toto","tutu"
print(t1)

a,b,*c = 0,1,3,4,5

print(a)
print(b)
print(c)



laliste = ["toto","toto1","toto2"]

# for elem in laliste:
for i,data in enumerate(laliste):
    print(i,data)



# def f(*values):
#     a,b,c,d = values
#     print(a,b,c,d)

# f(1,2,3,4)



# def f2():
#     return "toto","tutu"

# a,b = f2()



leset = {"valeur1","valeur2","valeur3","valeur1"}
print(leset)

lignes = ['ligne1','ligne1','ligne2']
ligneset = list(set(lignes))
print(ligneset)

ledict = {"name":"Gaurat","firstName":"fred"}
print(ledict["name"])
ledict["name"] = "Martin"
print(ledict["name"])
print(ledict)

for key,value in ledict.items():
    print(key,value)