l = []
for i in range(10):
    l.append(i)



def fib(n:int)->list:    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a,end=" ")
        a, b = b, a+b
    print()

def fib2(n):    # return Fibonacci series up to n
    """return a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib2(200)

# Now call the function we just defined:
fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
l = fib2(2000)
print(l)
# [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]

def add(a=0,b=0):
    c = a+b
    return c

r = add(5,6)
print(r)
r = add()
print(r)


r = add(b=6,a=5)



def sayHello(name,firstName,age=45):
    print("Hello",name,firstName,age)



    
sayHello("GAURAT","Fred")  # ok
sayHello("GAURAT",firstName="Fred")# ok

print("toto")
print("toto","tutu")
print("toto","tutu","tata")



def sayHello2(*values):
    print(values[0])

sayHello2('fred','gaurat')
sayHello2('fred','gaurat',45)
sayHello2('fred','gaurat',45,"python")


def add2(l):
    somme = 0
    for value in l:
        somme = somme+value

    return somme


def add3(*l):
    somme = 0
    for value in l:
        somme = somme+value

    return somme


la_liste = [1,2,3,4]
listSomme = add2(la_liste) # 10
print(listSomme)
listSomme = add3(1,2,3,4) # 10
print(listSomme)
listSomme = add3(1,2,3) # 6
print(listSomme)


def sayHello3(**keywords):
    print(keywords)
    print(keywords['name'])
    # print("Hello",name,firstName,age)



sayHello3(name="toto",firstName="tutu",job="dev",age=45)

def sayHello4(*values,**keywords):
    print(values)
    print(keywords)

sayHello4("val1","val2",name="titi",firstname="tutu")



# def sayHello5(name,firstname,/):
def sayHello5(*,name,firstname):
    print("hello",name,firstname)

sayHello5("gaurat","fred")
sayHello5(name="gaurat",firstname="fred")