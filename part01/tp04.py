def mult2Old(value): # mult2([1,2,3,4])
    # value => [1,2,3,4]
    result = []
    for the_number in value:
        result.append(the_number*2)

    return result

def mult2(the_number):
    return the_number*2

l = [1,2,3,4]
# r = mult2(l)
# r = list(map(mult2,l))
r = list(map(lambda the_number:the_number*2,l))
print(r)
#r = [2,4,6,8]
