print("Hello")

# TheWorldIsFlat => UpperCamelCase, PascalCase
# theWorldIsFlat => camelCase
# the_world_is_flat => snake_case
# the-world-is-flat => train-case, spine-case, kebab-case

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

a = 2
b = 3
c = a+b

print("le résultat est : "+str(c))

s1 = 'Hello'
s2 = "Hello"
s3 = 'L\'orage gronde'
s4 = "L'orage gronde"
s5 = "il fait\nbeau"
print(s5)
s6 = "c:\\truc\\numbers"
s7 = r"c:\truc\numbers"
print(s6)
print(s7)
s8 = """
    Il fait 
    beau
    voilà
"""

#  ceci est un commentaire

s9 = '''
    Il fait 
    beau
    voilà
'''
print(s8)


print("-"*50)


s1 = "Python"
print(s1[0])

print(len(s1))
print(s1[len(s1)-1])
print(s1[-1])
print(s1[-6])
print(s1[1:3])
print(s1[2:])
print(s1[:3])
print(s1[2:5])

print(s1[3:-1])

print(s1[50:])


s2 = 'Python'
print(id(s2))
s2 = 'Toto'
print(id(s2))
s3 = 'Toto'
print(id(s2))
print(id(s3))
# s3[0] = 'J'


a = 1
print(id(a))
b = 1
print(id(b))

print(id(1))

print(50*"-")
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])

squares[0] = 12
print(squares)

ma_list = ['toto','tutu',12,5.8]
print(ma_list)
ma_list[0] = 'tata'
print(ma_list)


print(50*'-')



l1 = [1,2,3,4]
l2 = l1[:]
l1[0] = 12
print(l1)
print(l2)
print(50*'-')

l1 = [
    [0,1],
    [2,3],
    [4,5]
]
print(l1)
l2 = l1[:]
l1[0][0] = 1000
print(l1 )
print(l2)


