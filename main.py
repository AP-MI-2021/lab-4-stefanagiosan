
def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def printMenu():
    print("1. Citire lista")
    print("2. lista dupa ce s-au eliminat duplicatele")
    print("3. Afisarea sumei primelor n numere pozitive din lista ")
    print("4.Afisare daca numerele pozitive din lista sunt in ordine crescatoare")
    print("5.")
    print("x. Iesire")


def elimina_duplicatele(l):
    '''
    Afisam lista dupa ce eliminam duplicatele
    :param l: lista cu numere intregi din care eliminam duplicatele
    :return: se afiseaza lista fara duplicate
    '''
    cop = []
    for i in l:
        if i not in cop:
            cop.append(i)
    print(str(cop))


def suma_primelor_n_numere_pozitive(l,n):
    '''
    Se face suma primelor n numere pozitive din lista, iar daca nu sunt n numere se afiseaza
    "dimensiunea listei este prea mica"
    :param l: lista din care se iau numerele pozitive
    :param n: cate numere pozitive se adauga in suma
    :return: returnam suma daca avem destule numere pozitive sau in caz contrar ,mesaj
    '''

    suma = 0
    nr = 1
    for i in l:
        if nr <= n and i>=0 :
            suma = suma + i
            nr = nr + 1
    if nr < n:
        print("Dimensiunea listei este prea mica")
    else:
        return suma


def test_suma_primelor_n_numere_pozitive():
    assert suma_primelor_n_numere_pozitive([1,2,-3,3,5],3) == (6)
    assert suma_primelor_n_numere_pozitive([10,100,1000,1],4) == (1111)
    assert suma_primelor_n_numere_pozitive([1,2,-5,-6],2) == (3)



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


def numarul_de_divizori_proprii(n):
    '''
    Calculam cati divizori proprii are numarul n
    :param n: numarul la care se calculeaza divizorii
    :return: se returneaza numarul de divizori proprii
    '''
    nr = 0
    for i in range(2,n-1):
        if n % i == 0:
            nr = nr + 1
    return nr


def test_numarul_de_divizori_proprii():
    assert numarul_de_divizori_proprii(25) == (1)
    assert numarul_de_divizori_proprii(19) == (0)
    assert numarul_de_divizori_proprii(12) == (4)
    assert numarul_de_divizori_proprii(7) == (0)


def main():
    test_nr_pozitive_in_ordine_crescatoare()
    test_numarul_de_divizori_proprii()
    test_suma_primelor_n_numere_pozitive()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune== "2":
            elimina_duplicatele(l)
        elif optiune == "3":
            n = int(input("dati nr n:"))
            print(suma_primelor_n_numere_pozitive(l,n))
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

