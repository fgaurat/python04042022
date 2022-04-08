from collections import deque
from ctypes import sizeof
import sys
ma_liste = []

for i in range(3):
    the_value = "valeur "+str(i+1)
    ma_liste.append(the_value)

#
print(ma_liste)
ma_liste.insert(0,"valeur 0")
print(ma_liste)
first_value = ma_liste.pop(0)
print(first_value)
print(ma_liste)

q = deque(ma_liste)
print(q)
q.appendleft('valeur 0')
print(q)
print(ma_liste)
first_value = q.popleft()
print(first_value)


l = []
for i in range(5):
    if i%2==0:
        l.append(i*2)
print(l)

l = list(map(lambda i: i*2, range(5)))
print(l)

# l = [i*2 for i in range(5) if i%2==0]
l = [i*2 for i in range(5)]
print(l)

ma_liste = ['  toto  ','   tutu','tata   ']

ma_clean_list = []
for s in ma_liste:
    ma_clean_list.append(s.strip())

ma_clean_list = [s.strip() for s in ma_liste]



print(ma_liste)
print(ma_clean_list)
# s = "   fdsfsd   "
# print(s.strip())
# ma_clean_list
# ['toto','tutu','tata']



