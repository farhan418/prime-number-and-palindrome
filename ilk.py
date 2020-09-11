
ufuk ='108'
if ufuk == '109':
    print('helal oğluuum')
elif ufuk == '110':
    print('amk şişkosu')
elif ufuk == '108':
    print('yok amına')
else:
    print('yalan söyleme amk çocu')


def asal(w):
    for q in range(2,w):
        for b in range (2,w):
            if q % b == 0 and q > b:
                break
        else:
            print(q)
    return 'Finish'

print(asal(1000))

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


def asal(w):
for q in range(2,w):
for b in range (2,w):
if q % b == 0 and q > b:
break
else:
print(q)
return 'Finish'

print(asal(1000))