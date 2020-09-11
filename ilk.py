



def prime(w):
    for q in range(2,w):
        for b in range (2,w):
            if q % b == 0 and q > b:
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


