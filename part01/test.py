a=0
b=1
# a, b = 0, 1

while a < 10:
    print(a)
    #a=a+1
    c = a+b
    a = b # 1
    b = c  # 0+1
    
    a, b = b, a+b
    #a,b = 1,0+1
