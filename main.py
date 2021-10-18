
def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def printMenu():
    print("1. Citire lista")
    print("2.")
    print("3.")
    print("4.Afisare daca numerele pozitive din lista sunt in ordine crescatoare")
    print("x. Iesire")

'''
Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură. Dacă
sunt mai puțin de n numere pozitive în listă, se afișează mesajul “Dimensiunea listei este prea
mică”.
'''



'''
pb 4. Să se afișeze “DA” în cazul în care toate numerele pozitive din listă sunt în ordine crescătoare și
“NU” altfel.
'''

def nr_pozitive_in_ordine_cresc(l):
    '''
    Se creeaza o lista noua doar cu numerele pozitive, iar apoi se verifica daca toate din noua lista sunt in ordine crescatoare
    :param l: lista de nr intregi din care se iau numerele pozitive
    :return: True, daca numerele pozitive sunt ordonate crescator, iar False in caz contrar
    '''

    pozitive = []
    for x in l:
        if x >= 0:
            pozitive.append(x)

    if pozitive == []:
        return False
    else:
        length = len(pozitive)
        for i in range(length - 1):
            t=pozitive[i+1] - pozitive[i]
            if t < 0:
                return False
        return True


def test_nr_pozitive_in_ordine_crescatoare():
    assert nr_pozitive_in_ordine_cresc([-1,4,5,6,-7]) == True
    assert nr_pozitive_in_ordine_cresc([-1, 4, 8, 6, -7]) == False
    assert nr_pozitive_in_ordine_cresc([-1, 4, -5, 6, -7]) == True
    assert nr_pozitive_in_ordine_cresc([-1, -4, 15, 6, -7]) == False

def main():
    test_nr_pozitive_in_ordine_crescatoare()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "3":
            n = int(input("dati nr n:"))
        elif optiune == "4":
            if  nr_pozitive_in_ordine_cresc(l) == False :
                print ("NU")
            else:
                print("DA")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")



if __name__=='__main__':
    main()

