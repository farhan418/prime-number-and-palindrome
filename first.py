
from math import sqrt
# sqrt function is basically finds square rooth of a number 


def prime(w):
    for q in range(2,w):
        for b in range (2, int(sqrt(q))):
            if q % b == 0 :
                break
        else:
            print(q)
    return 'Finish'

print(prime(1000))

'''
for x in range(2, 101):
        for i in range(2, 101):
            if x % i == 0 and x > i:
                break
        else:
            print(x)
'''




def polind(text):
    if text == text[::-1]:
        print(text + ' ' + 'is a polindrom')
    else:
        print(text + ' ' + 'is not a polindrom')

polind('qwerewq')


