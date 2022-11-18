#Ruubiku Kuubiku Scrambler ehk RKS
#Marten Uiboupin
#VOCO ITA 22
import random
import time

yes = input(' Kas soovite genereerida 3x3 või 2x2 scramble? (3/2): ')
moves = ["U", "D", "F", "B", "R", "L", "U'", "D'", "F'", "B'", "R'", "L'", "U2", "D2", "F2", "B2", "R2", "L2"]

def three_by_three():
    s = [random.choice(moves) for x in range(random.randint(20, 23))]
    return ' '.join(s)

def two_by_two():
    s = [random.choice(moves) for x in range(random.randint(9, 12))]
    return ' '.join(s)

kriips2 = '---------------------------------\n'
kriips = '\n------------------------------'
kriips3 = '\n---------------'
kriips4 = '---------------\n'

a = three_by_three()
b = two_by_two()

if yes == '3':
    print(kriips2 + ' 3x3 Scramble: ' + a)
elif yes == '2':
    print(kriips2 + ' 2x2 Scramble: ' + b)

def aeg(seK):
    min = seK // 60
    seK = seK % 60
    min = min % 60
    print(kriips2 + " Teie aeg oli: {0}:{1}".format(int(min),seK) + kriips3)
    if lõpp_aeg >= 30:
        print(' Ur trash kid!')
    elif lõpp_aeg <= 10:
        print(' Holy cow!')
    else:
        print(' Noice!')

def aeg2(seK):
    min = seK // 60
    seK = seK % 60
    min = min % 60
    print(kriips2 + " Teie aeg oli: {0}:{1}".format(int(min),seK) + kriips3)
    if lõpp_aeg >= 20:
        print(' Ur trash kid!')
    elif lõpp_aeg <= 5:
        print(' Holy cow!')
    else:
        print(' Noice!')

keskmine = [] 

for g in range(5):
    input(f"{kriips2} Vajutage ENTER, et alustada aeg")
    algus = time.time()
    input(f"{kriips2} Vajutage uuesti ENTER, et lõpetada aeg")
    lõpp = time.time()

    lõpp_aeg0 = lõpp - algus
    lõpp_aeg = round(lõpp_aeg0, 2)

    if yes == '3':
        aeg(lõpp_aeg)
    elif yes == '2':
        aeg2(lõpp_aeg)
    
    keskmine.append(lõpp_aeg)

keskmine1 = keskmine.copy()
keskmine1.remove(max(keskmine1))
keskmine1.remove(min(keskmine1))
keskmine0 = sum(keskmine1) / len(keskmine1)

print(f'{kriips4} Teie viie keskmine aeg on on {round(keskmine0, 2)} sekundit')
