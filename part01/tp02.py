

l = ['valeur 1','valeur 2','valeur 3','valeur 4']


for value in l:
    taille = len(value)
    # print(value+" "+str(taille))
    print(value,taille)


for i in range(len(l)):
    print(i,l[i])

# range 
# 0 valeur 1
# 1 valeur 2
# 2 valeur 3
# 3 valeur 4

print(l)

# for i in l:
# for i in range(5):

i = 0
s = str(i)

print(range(len(l)))

l2 = list(range(len(l)))
print(l2)


for i in range(10):
    print(i)
else:
    print("dans le else")

l = ['valeur 1','valeur 2','valeur 3','valeur 4']
to_find = "valeur 12"


for item in l:
    if to_find == item:
        print(to_find,"trouvé")
        break
else:
    print(to_find,"pas trouvé")

# valeur 12 : pas trouvé
# valeur 1 : trouvé


for i in range(10):
    if i == 5:
        pass 
    print(i)


print(50*'-')

