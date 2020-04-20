# you can find the problem here https://open.kattis.com/problems/2048
# written by David Stålmarck 2019-11-25


listan = []

for i in range(4):
    a = [int(x) for x in input().split()]
    listan.append(a)

move = int(input())


def byta_plats(listan):
    listan2 = []
    for itr in range(4):
        local= []
        for lista in listan:
            local.append(lista[itr])
        listan2.append(local)
    return listan2

def left(listan):
    new_list = []
    for lista in listan:

        lista = list(filter(lambda b: b !=0, lista))

        length = len(lista) - 1

        for el in range(length):
            try:
                if lista[el] == lista[el+1]:

                    lista[el] = str(lista[el]*2)
                    lista.pop(el+1)
            except IndexError:
                break
        while len(lista)<4:
            lista.append(0)

        new_list.append(lista)
    return new_list

def right(listan):
    new_list = []
    for lista in listan:

        lista = list(filter(lambda b: b !=0, lista))

        length = len(lista) - 1

        for el in range(length, 0, -1):
            try:
                if lista[el] == lista[el-1]:

                    lista[el] = str(lista[el]*2)
                    lista.pop(el-1)
            except IndexError:
                break

        while len(lista)<4:
            lista.insert(0, 0)
        new_list.append(lista)


    return new_list


def make_sexy(listan):
    string = ''
    for lista in listan:
        for el in lista:
            string += str(el) + ' '
        string += '\n'
    return string



if move == 0:
    print(make_sexy(left(listan)))
elif move == 1:
    svar = left(byta_plats(listan))
    print (make_sexy(byta_plats(svar)))
if move == 2:
    print(make_sexy(right(listan)))
elif move == 3:
    svar2 = right(byta_plats(listan))
    print(make_sexy(byta_plats(svar2)))