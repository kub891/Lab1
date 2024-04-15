'''
###################################################################################################################
Dziś zajęcia dotyczą tworzenia funkcji ze zmienną liczbą argumentów wejściowych.
Przed realizacją zadań koniecznie zapoznaj się ze slajdami prezentacji do Wykładu 3 

Dodatkowe linki do filmów, które ułatwią Ci zrozumienie materiału z laboratorium:
"Co oznacza zapis *args oraz **kwargs w funkcjach?"   -  https://www.youtube.com/watch?v=7nwXBWzkqNU
####################################################################################################################

'''


############################### Teoria: Funkcja z dowolną liczbą argumentów wejściowych (*args)  #########################
### def nazwa_funkcji(*args):
###    instrukcje
##     return obiekt                 *args - krotka argumentów pozycyjnych

###### Wyrażenie “args” bierze się z od słowa “arguments” czyli argumenty i jest to zazwyczaj zmienna,
###### która zawiera tuple argumentów pozycyjnych. Wyrażenia z jedną gwiazdką (*) używamy gdy do funkcji
### chcemy przekazać dowolną liczbę argumentów pozycyjnych (czyli takich dla których
### przy wywołaniu funkcji nie podajemy ich nazwy, a przypisanie wartości bazuje na kolejności argumentów dlatego
### args - argumenty umieszczane są w krotce/tupli po której możemy iterować args[0], args[1] itd.
## używamy *args gdy nie są istotne dla nas nazwy zmiennych
### Pamiętaj aby parametr *args umieszczać na końcu listy parametrów w definicji funkcji!


################################## Przykład 1  suma dowolnego ciągu cyfr
# def suma(*args):
#     if not args:                        # wkazane jest kontrolowanie przypadku braku argumentów
#         return('brak argumentów')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


################################### Przykład 2:  suma dowolnego ciągu cyfr plus wartość stałej
# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

#################################### Przykład 3:  suma pierwszych 4 cyfr dowolnego ciągu cyfr
# def suma3(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#     
#      print(sumaLiczb)
#     return(None)
#
# suma3(1,2,3,4,5,6,7,8,9,10)
# suma3()

#########################################################################################################
#############funkcje z dowolną liczbą argumentów kluczowych (**kwargs) ############
### ** kwargs pozwala przekazywać zmienną długość argumentów ze słowami kluczowymi do funkcji.
### W przypadku gdy do naszej funkcji chcemy przekazywać argumenty, które wyróżniają
### się nazwą możemy użyć parametru z dwoma gwiazdkami (**).
### Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika.
### Jego pary klucz-wartość stanowią nazwa i wartość przekazanego argumentu.
### używamy **kwargs gdy istotna dla nas jest nazwa zmiennych

# def nazwa_funkcji(**kwargs):
#     instrukcje
#     return obiekt                 # kwargs - słownik argumentów kluczowe

######## wstaw jako argument funkcji:  *kwargs  ########################################

## “kwargs” z j.ang. “keyword arguments” czyli argumenty nazwane
## i zmienna taka zawiera pary nazwa-wartość argumentu.

## Przykład
# def slownik(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# slownik(a=1, b=2, c=3)

# def witaj(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# witaj(name="yasoob")

########################################## Zapamiętaj:
#### 1. “args” i “kwargs” możesz zastąpić dowolnymi innymi nazwami zmiennych
#### 2. Pamiętaj umieszczając w definicji funkcji wyrażenie z jedną lub dwoma gwiazdkami
### pozwalamy na przekazywanie do niej argumentów w dowolniej liczbie i nazwie.
### bez konieczności konkretnego określenia tych parametrów.
### 3. Pamiętaj o kolejności – wyrażenie z dwoma gwiazdkami
### musi być na końcu, z jedną gwiazdką wcześniej, a pozostałe zdefiniowane argumenty na początku.


#### Gwiazdek możesz również używać w wywołaniu funkcji.
#### Jest to tak zwane rozpakowywanie list i słowników z argumentami.
#### Jeżeli funkcja przyjmuje kilka argumentów i posiadasz listę,
#### która zawiera argumenty, które chcesz przekazać do tej funkcji
#### wystarczy poprzedzić nazwę listy gwiazdką zamiast podawać kolejne argumenty ręcznie.

# list_arg = [1, 3, 5]
#
# def rozpakowywanie(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# rozpakowywanie(*list_arg)     # odpowiednik dużo dłuższego kodu:   rozpakowywanie(list_arg[0], list_arg[1], list_arg[2])
############################################################################################################################################




############Przykład
### Mamy 2 sklepy  z różnymi produktami
# def test_kwargs(id_sklep = 0, liczba_pracownikow = 5, **kwargs):
#     print(id_sklep)
#     print(liczba_pracownikow)
#     print(kwargs)
#
# test_kwargs(1, mleko=100, woda=500)
# print('#################')
# test_kwargs(2, liczba_pracownikow = 15, drabina=500, cement=200)







##################################### Zadanie 0   na rozgrzewkę ##################
## Utwórz funkcję o nazwie "Rozprawka.py", która będzie wyświetlała,
## na ekranie napis "to poprostu jest wspaniałe i niesamowite, musisz to zobaczyć",
## następnie używając w/w funkcji napisz tekst reklamujący, opisujący jeden z 7 Cudów świata gdzie 
## wywołasz tą funkcję w tekście minimum 3 krotnie
######################################################################################################################

def rozprawka():
    print('to poprostu jest wspaniałe i niesamowite, musisz to zobaczyć')


print("Zapraszamy do odwiedzenia Wielkiego Muru Chińskiego - jednego z siedmiu cudów świata!")
rozprawka()
print("Wielki Mur Chiński, to niezwykłe dzieło ludzkiej pomysłowości i wytrwałości.")
rozprawka()
print("Jego widok zapiera dech w piersiach i pozostawia niezapomniane wrażenia.")
rozprawka()

################################   Zadania do realizacji
## Zadanie 1
# Utwórz 1 funkcje wielu-zmiennych wejściowych, która obliczy wartość wyrażenia
## dla dowolnego jednego argumentu wejściowego, x^x
## dla dowolnych dwóch argumentów wejściowych  x^x, 
##dla pozostałych przypadków wyświetli komunikat, że jest błąd.

def func(*args):
    if not args:
        print('Brak argumentów')
    elif len(args) > 2:
        print('Za dużo argumentów')
    elif len(args) == 1:
        return args[0] ** args[0]
    elif len(args) == 2:
        return args[0] ** args[1]
print(func(2,3))

######### Zadanie 2
## Wczytaj poniższy fragment tekstu opisujący komputer
## Napisz funkcję która ustali liczbę występujących w tym tekście wyrazów wskazanych przez użytkownika
## ciąg nazw i liczba wyszukiwanych wyrazów podanych przez użytkownika jest dowolna,
## niemniej w tekście są wyrazy o nazwach kluczowych i potencjalnie zawsze ważnych
### dla innych użytkowników np. komputera, skaner, uwzględnij je w wyszukiwaniu.


text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
       'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
       'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
       'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
       'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
       'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
       'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
       'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
       'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
       'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'

# print(text)

def words(word, text):
    print('Tekst zawiera: ' + str(text.count(word)) + 'slow ' + word)

word = input('Podaj slowo do wyszukania: ')
words(word,text)
############ Zadanie 3 #################
## Utwórz funkcję o nazwie "SredniaLiczb.py", która wczyta N dowolnych liczb 
## i obliczy średnią z w/w liczb, podane przez użytkownika liczby przypisz do listy


numbers = []
while True:
    number = input('Podaj liczbe do sredniej (napisz ,,stop,, jesli chcesz przerwac wpisywanie): ')
    if(number == 'stop'):
        break
    else:
        numbers.append(number)

def srednialiczb(*args):
    result = 0
    for i in range(0, len(args)):
        result = result + int(args[i])  
    return result / len(args)
print(srednialiczb(*numbers))

############ Zadanie ##################
## Utwórz funkcję o nazwie "ZdanieRozdziel.py", która wczyta od użytkownika pewien dowolny tekst,'
## a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
## funkcja w zależności od ustawionych kolejnych parametrów wejściowych funkcji 
## (ustaw domyślnie argumenty wejściowe: True), 
## może ale nie musi wyświetlić następujące informacje: 
## ile w każdym zdaniu jest fragmentów rozdzielonych przez określony znak np. ',', ';' 
##(domyślnie argument wejściowy to przecinek: ',')
## ile w każdym zdaniu jest wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)
## użyj odpowiednich metod dla zmiennych typu string np. split do rozdzielenia elementów: x = ‘blue,red,green’,   x.split(“,”)

def ZdanieRozdziel(txt):
    txt_list = txt.split('.')
    print(txt_list, ' text rozdzielony na zdania')
    print(int(txt.count(',')) + int(txt.count(';')) , 'w texcie jest tyle rozdzielaczy textu')
    print(txt.count(' '), ' W texcie jest tyle wyrazow')

txt = input('Podaj text: ')
ZdanieRozdziel(txt)

########### Zadanie 6  ########################
## Zdefiniuj funkcję "CiagGometryczny.py", która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2) 
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego
## b) sumę elementów ciągu geometrycznego

def CiagGometryczny(n,a1,q):
    print('Wartosc ' + str(n) + ' elemntu ciagu wynosi: ' + str(a1*(q**(n-1))))
    print('suma wyrazow ciagu od 1 do ' + str(n) + ' wynosi ' + str(((a1 + (a1*(q**(n-1))))/2)*n))
CiagGometryczny(5,1,2)
    

# ########################## Zadanie 7
## Zaprojektuj program służący do obsługi prostej bazy danych dla sklepu z
## dowolnej branży o różnej liczbie pracowników. Program zapisuje do kolejnych list
## liczby produktów dostarczonych w danym dniu (nazwa listy odpowiada nazwie towaru)
## liczba towarów powinna być zapamiętana 
# Przetestuj swój program dla różnych przypadków dostawy towaru
# Pamiętaj że asortyment sprzedawanego towaru ulega zmianie
# Użyj kwargs

def base(**kwargs):
    for towar, ilosc in kwargs.items():
        if towar in baza_danych:
            baza_danych[towar].append(ilosc)
        else:
            baza_danych[towar] = [ilosc]

baza_danych = {}

base(jablka=50, banany=30)
base(marchewki=20, jablka=40)
base(banan=20, pomarancze=35, marchewki=15)

print("Zawartość bazy danych: ")
for towar, ilosci in baza_danych.items():
    print(f'{towar}:{ilosci}')




# ########################## Zadanie 8
## W module pole_prostokata.py 
## Zdefiniuj funkcję która obliczy pole powierzchni prostokąta
## W module pole_trojkata.py 
## Zdefiniuj funkcję która obliczy pole powierzchni trójkąta
# W module pola.py
## Korzystając z modułów pole_prostokata i pole_trojkata
## napisz funkcję która ma możliwość obliczenia pola prostokąta, trójkąta i kwadratu
## Użyj zmiennych globals, utwórz moduł globals.py w którym będą przechowywane 
## domyślne wartości dla boków prostokąta, trójkąta, kwadratu (równe 1)

import globals
from pole_prostokata import oblicz_pole_prostokata
from pole_trojkata import oblicz_pole_trojkata

def oblicz_pole(figura):
    if figura == "prostokat":
        a = globals.prostokat_bok_a
        b = globals.prostokat_bok_b
        return oblicz_pole_prostokata(a, b)
    elif figura == "trojkat":
        a = globals.trojkat_podstawa
        h = globals.trojkat_wysokosc
        return oblicz_pole_trojkata(a, h)
    elif figura == "kwadrat":
        a = globals.kwadrat_bok
        return oblicz_pole_prostokata(a, a)
    else:
        return "Nieznana figura"


print("Pole prostokata:", oblicz_pole("prostokat"))
print("Pole trojkata:", oblicz_pole("trojkat"))
print("Pole kwadratu:", oblicz_pole("kwadrat"))

# ########################## Zadanie 9
## Zdefiniuj funkcję wyższego rzędu która ma możliwość obliczenia
## pole powierzchni prostokąta i pola powierzchni trójkąta
## Nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj możliwość 
## obliczenia pola kwadratu

def oblicz_pole(figura, **kwargs):
    if figura == "prostokat":
        a = kwargs['a']
        b = kwargs['b']
        return oblicz_pole_prostokata(a, b)
    elif figura == "trojkat":
        a = kwargs['a']
        h = kwargs['h']
        return oblicz_pole_trojkata(a, h)
    elif figura == "kwadrat":
        a = kwargs['a']
        return oblicz_pole_prostokata(a, a)
    else:
        return "Nieznana figura"


print("Pole prostokata:", oblicz_pole("prostokat", a=3, b=4))
print("Pole trojkata:", oblicz_pole("trojkat", a=3, h=5))
print("Pole kwadratu:", oblicz_pole("kwadrat", a=4))

# ########################## Zadanie 10
## Utwórz funkcję która umożliwia logowanie na serwer
## Ma dwa argumenty wejściowe:
## user i password (domyślne wartości odpowiednio: 'edek2003', 'Wsx123')
## a) nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj dodatkowe
## pola tj. host, port
## b) nie modyfikując zawartości w/w funkcji, użyj dekoratora i  daj możliwość 
## wprowadzania dodatkowych innch pól użytkownikowi (wprowadzane jako słownik
##  np. {'data_base': 'https://pl.wikipedia.org'})

def logowanie(user='edek2003', password='Wsx123'):
    return "Logowanie uzytkownika " + user + " z uzyciem hasła " + password


print(logowanie()) 
print(logowanie('kuba', 'kuba')) 


def dodaj_pola_host_port(func):
    def add(**kwargs):
        if 'host' in kwargs and 'port' in kwargs:
            return func(**kwargs)
        else:
            kwargs['host'] = 'default_host'
            kwargs['port'] = 8080
            return func(**kwargs)
    return add



def logowanie(user='edek2003', password='Wsx123', **kwargs):
    return f"Logowanie uzytkownika " + user + " na serwer host: " + str(kwargs['host']) + " i porcie: " + str(kwargs['port']) + " z użyciem hasła " + password

print(logowanie(user='janek', password='secret', host=123123, port=1234))

# ########################## Zadanie 11
## Zdefiniuj funkcję ciag_gometryczny, która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2) 
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego


def CiagGometryczny(n,a1,q):
    print('Wartosc ' + str(n) + ' elemntu ciagu wynosi: ' + str(a1*(q**(n-1))))
    print('suma wyrazow ciagu od 1 do ' + str(n) + ' wynosi ' + str(((a1 + (a1*(q**(n-1))))/2)*n))
CiagGometryczny(5,1,2)

## Następnie korzystając z dekoratora udoskonal swoją funkcję,
## dodaj możliwość obliczenia sumy elementów ciągu geometrycznego