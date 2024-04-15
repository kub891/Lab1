import os   ## moduł obsługi plików, katalogów, dysków
'''
Uwaga: wymienione w przykładach nazwy katalogów i plików
nie występują w Twoim PC-cie, dostosuj ich nazwy do istniejących !!!
Jeśli korzystasz z replit-a .... ścieżkę rozpocznij od "/home"

Operacje na plikach i katalogach:
aby zmieniać, tworzyć katalogi, oglądać ich zawartość itp. będziemy stosować funkcje
i metody z bibioteki o nazwie os, ta biblioteka ma szereg metod, każda metoda umożliwia
zrealizowania pewnych operacji na katalogach. Zapoznaj się z przykładami metod poniżej
a następnie wykonaj zadania
'''
######################## Obsługa dysków i folderów
### Przykład 1
## Metoda getcwd() pozwala sprawdzić jaką ścieżkę ma bieżacy folder, czyli ten w którym
## znajduje się Twój plik z programem

# moj_obecny_folder = os.getcwd()
# print(moj_obecny_folder)

### Przykład 2
### metoda listdir('.') służy do sprawdzania zawartości katalogu

#zawartosc_biezacego_folderu = os.listdir('.')
#print(zawartosc_biezacego_folderu)

### Przykład 3
### listdir('ścieżka dostępu do folderu') - zawartosc_konkretnego_folderu

# zawartosc_wskazanego_folderu = os.listdir('c:\\Windows')
# print(zawartosc_wskazanego_folderu)

### Przykład 4
#print(os.getcwd())   # sprawdzamy jaki jest nasz katalog roboczy/bieżący
#zmiana_katalogu_roboczego = os.chdir('c:\\Users') # zmiana bieżącego katalogu dyskowego na inny np. c:/Users
#print(os.getcwd()) # sprawdzamy jaki jest roboczy po wywołaniu instrukcji zmiany

### Przykład 5 - Filtrowanie nazw plików i katalogów według określonego wzorca
import fnmatch
'''
fnmatch - moduł umożliwiający wyszukiwanie określonych ciągów znaków,
zapewnia obsługę symboli wieloznacznych.
funkcja o takiej samej nazwie jak moduł fnmatch(nazwa, wzorzec) sprawdza czy podana
nazwa (typ String) zaczyna i/lub kończy się na określony wzorzec (typ String)
'''
#zdanie = 'Python to jezyk programowania.py'
#czy_to_prawda1 = fnmatch.fnmatch(zdanie,'P*a') # czy zmienna zdanie zaczyna się na literę P i kończy na m?
#print(czy_to_prawda1)
#czy_to_prawda2 = fnmatch.fnmatch(zdanie,'*.py') # czy zmienna zdanie kończy na m?
#print(czy_to_prawda2)

### Przykład 6
'''
Metoda makedirs() służy do tworzenia nowego folderu w bieżącym folderze
jeżeli folder istnieje to program wyrzuci błąd
'''
#os.makedirs('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa')

### Przykład 7
## Dołączanie pliku/katalogu i rozdzielenie ścieżki do folderu i nazwy wybranego pliku
#print(os.getcwd()) # sprawdzam nazwę folderu roboczego

## zmieniam miejsce "pobytu" przechodzę do katalogu o nazwie Dokument
# os.chdir('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa')

# moja_sciezka = os.getcwd()
# print(moja_sciezka) # ponownie sprawdzam gdzie się znajduję

## path.join łączy ciąg katalogów/pliku w ścieżkę
# nowa_sciezka = os.path.join(moja_sciezka,'Labo1.py')
# print(nowa_sciezka)

#rozdzielona_sciezka1 = os.path.split(os.path.realpath('Labo1.py')) # rozdzielam scieżkę i nazwę pliku
# print(rozdzielona_sciezka1)
# print(rozdzielona_sciezka1[0]) # pierwszy element z krotki
# print(rozdzielona_sciezka1[1])

### Przykład 8 - sprawdzanie rozmiarów plików (w bajtach)

#rozmiar_pliku = os.path.getsize('C:\\Users\\aneta\PycharmProjects\Programowanie1\L1.py')
# print(rozmiar_pliku)

### Przykład 9 - zmiana nazwy folderu
### Syntax: rename(stara_nazwa, nowa_nazwa)
# os.rename('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa', 'C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa2')
# print(os.listdir('C:\\Users\\aneta\PycharmProjects\Programowanie1'))

############################## Operacje  na plikach
'''
Zapoznaj się z możliwymi trybami zapisu do pliku:
http://programista-python.pl/operacje-wejscia-wyjscia-na-plikach-w-pythonie/
Tworzymy nowy plik tekstowy o nazwie: 'FirstFile.txt'
'''
### Przykład 10

## Syntax: open(file, mode)
## atrybut 'w': tryb zapisu, utwórz nowy plik lub nadpisz treść w pliku
# file1 = open('FirstFile.txt', 'w', encoding='utf-8')

# text1 = 'I love python,'
# file1.write(text1)  # zapis do pliku
#
# file1.close()  # operacja zamknięcia pliku

## Dodanie nowych danych do pliku
# file2 = open('FirstFile.txt', 'a', encoding='utf-8')  #  atrybut 'a':  tryb zapisu, dołącz treść
# text2 = ' very ... very much.'
# file2.write(text2)  # zapis do pliku
# file2.close()  # operacja zamknięcia pliku

## Odczyt zawartości
# file2 = open('FirstFile.txt', 'r')  #  atrybut 'r':  tryb odczytu (tryb domyślny)
# odczyt_tresci = file2.read()
# print(odczyt_tresci) # podgląd zawartości całego pliku

## Zapis i odczyt pliku kolejnych linii
#file11 = open('SecondFile.txt', 'w')  #  atrybut 'w':  tryb zapisu, utwórz nowy plik, lub nadpisz treść
#text11 = 'Mit o Prometeuszu, który poświęcił się dla ludzkości, wykradając bogom z Olimpu ogień\n \
#         Mit o Dedalu, praktycznym wynalazcy, i idealiście Ikarze, który leciał zbyt blisko słońca, stopił wosk swoich sztucznych skrzydeł i spadł\n\
#         Mit o Syzyfie skazanym na wieczne wtaczanie głazu, który przy samym szczycie znów spadał – stąd pojęcie syzyfowej pracy\n\
#         Mit o Narcyzie, który zachwycił się własną urodą\n\
#         Mity o Korze i Demeter\n\
#         Mit o jabłku niezgody i pięknej Helenie, o kowalu Hefajstosie i jego żonie Afrodycie\n\
#         Mit o Apollu i Marsjaszu, który ośmielił się współzawodniczyć z bogiem\n\
#         Mit o labiryncie i Tezeuszu, któremu udało się z niego wyjść dzięki podarowanemu mu przez Ariadnę kłębkowi nici\n\
#         Mit o Pigmalionie zakochanym w stworzonej przez siebie rzeźbie kobiety\n\
#         Mit o śpiewaku trackim Orfeuszu, który poszedł do podziemi po swoją żonę Eurydykę\n\
#         Mit o Amorze i Psyche\n\
#         Mit o Niobe, która straciła swoje dzieci z powodu własnej pychy\n'
#
# file11.write(text11)
# file11.close()

# Odczyt zawartości
# file3 = open('SecondFile.txt', 'r')  #  atrybut 'r':  tryb odczytu (tryb domyślny)
# print(file3.read())    # odczyt całości treści
# print(file3.readlines(1))    # odczyt 1 linii

###  odczyt linia po linii
#for linia in file3:
#    print(linia)

# ########## Szybki zapis i odczyt danch - picle
'''
moduł picle służy do utrwalania, zapisywania i odczytywania dowolnych obiektów Pythona.
Tego typu obiekty są nazywane trwałymi (ang.persistent) a plik je przechowujący
pamięcią trwałą (persistent storage). Zakończenie programu nie powoduje bowiem ich zniknięcia.
'''
import pickle
### Przykład 11
## zapis danych do pliku
# filename = 'lista_zakupow.data'
# products = ['jabłka', 'ziemniaki', 'pomidory']
# f1 = open(filename, 'wb')
# pickle.dump(products, f1)
# f1.close()


## usunięcie zmiennej z pamięci i ponowne wczytanie danych
# del products
# # odzyskanie zmiennej
# f2 = open(filename, 'rb')
#
# products = pickle.load(f2)
# for rzecz in products:
#     print(rzecz)

### Przykład 12  - zapisywanie większej liczby obiektów
# products1 = 'jabłka'
# products2 = 'ziemniaki'
#
# f3 = open('myfile.pickle', 'wb')
# pickle.dump((products1,products2), f3)  # zapisujemy obiekty do krotki
# f3.close()
## Uwaga!: bez wywwołania metody .close() dane zostaną zapisane automatycznie najpóźniej
## w momencie zakończenia programu

# del products1, products2
## odzyskanie zmiennej
# f4 = open('myfile.pickle', 'rb')
# products = pickle.load(f4)  # przypisujemy wczytane obiekty do zmiennej
# print(products[0])
# print(products[1])

### Przykład 12  - funkcje pack(), unpack() w zapisie danych do pliku
'''
Jeśli chcemy zapisać dane inne niż tekst do pliku, możemy posłużyć się funkcją pakowania danych (pack)
z wbudowanego modułu struct. Zamienia ona tekst na dane binarne (w takiej postaci jak przechowywane są w
pamięci komputera). Generalnie, struct służy do obsługi danych binarnych przechowywanych w plikach,
bazie danych lub z połączeń sieciowych itp.
'''
from struct import *
'''
Dodatkowe informacje o funkcji pack(), pierwszy argument pack()
zawiera kolejne typy danach które mają być pakowane tj.
?: boolean
h: short int
l: long int
i: int
f: float
q: long long int
'''
# var = pack('hhl', 50, 100, 150)  # Zwróć uwagę że kolejne dane są zapisywane do krotki
# print(var)
# print(unpack('hhl', var))

## Wariant z zapisem do pliku + pack()
#f1 = open('plik2.dat','wb') # litera b oznacza zapis danych binarnych
# number2 = pack('h',9876)
# f1.write(number2)
# f1.close()

## Odczyt danych z pliku
# f2 = open("plik2.dat", "rb")   # litera b oznacza odczyt danych binarnych
# print(unpack('h',f2.read()))
# f2.close()


### Przykład 12 - użycie funkcji eval
'''
Syntax:  eval(expression, globals=None, locals=None)
globals,locals - opcjonalne  x = 10
'''
# x = 1
# y = eval(input('Podaj równanie prostej lub wielomianu: '))
# print(y)

########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.

def zmien_katalog(sciezka):
    try:
        os.chdir(sciezka)
        print("Zmieniono bieżący katalog na: " + sciezka)
    except FileNotFoundError:
        print("Podana ścieżka nie istnieje.")
    print(os.listdir('.'))

# zmien_katalog('/')

########################## Zadanie 2 #########################
## Korzystając z utworzonej funkcji napisz funkcję która będzie zmieniała bieżący katalog
## dyskowy na inny wskazany przez użytkownika oraz będzie wyświetlała zawartość wskazanego przez
## użytkownika katalogu.
## Przetestuj działanie programu dla natepującego przypadku:
## program działa tylko wówczas gdy użytkownik odpowie "yes" na pytanie:
## "Czy mam zmienić katalog?", zastosuj pętle while True(zmuś użytkownika :) do wpisania "yes")

sciezka = input('Podaj sciezke')
while True:
    answ = input('czy napewno zmienic sciezke')
    if(answ.lower() == 'yes'):
        zmien_katalog(sciezka)
        break
    else:
        print('musisz wpisac yes zeby zmienic sciezke')



########################## Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się folderze roboczym
## b) korzystając z metod Pythona i (pętli lub funkcji filter) wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym

os.makedirs("Dokument", exist_ok=True)
os.chdir('Dokument')
not os.path.exists("lab1.doc") and open("lab1.doc", "w")
not os.path.exists("lab2.doc") and open("lab2.doc", "w")
not os.path.exists("lab3.doc") and open("lab3.doc", "w")
os.listdir('.')

def doc(file):
    return ".doc" in file
files_doc = filter(doc, os.listdir('.'))
print(files_doc)
for plik in files_doc:
    print(plik)

########################## Zadanie 4 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2 katalogi:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe i graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku

os.makedirs('StudentDoc', exist_ok=True)
os.makedirs('StudentObrazy', exist_ok=True)
open("StudentDoc/plik1.txt", "w")
open("StudentDoc/plik2.txt", "w")

open("StudentObrazy/plik1.jpg", "w")
open("StudentObrazy/plik2.jpg", "w")

folder = 'StudentDoc'
filess = os.listdir(folder)

for plik in filess:
    sciezka = os.path.join(folder, plik)
    if os.path.isfile(sciezka):
        rozmiar = os.path.getsize(sciezka)
        print(f"Nazwa pliku: {plik}, Rozmiar: {rozmiar} bajtów")


########################## Zadanie 5 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.

os.mkdir("labb")
old_name = "labb"
new_name = "laby"
os.rename(old_name, new_name)

print(os.listdir())

########################## Zadanie 6 ########################
# # Utwórz trzy listy, zapisz, usuń a następnie odczytaj z pliku listy, użyj pickle

import pickle
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['asfasf', 'gasgasg', 'vzxvxz']

with open('listy.pickle', 'wb') as file:
    pickle.dump(list1, file)
    pickle.dump(list2, file)
    pickle.dump(list3, file)

del list1
del list2
del list3


with open('listy.pickle', 'rb') as file:
    lista1 = pickle.load(file)
    lista2 = pickle.load(file)
    lista3 = pickle.load(file)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)


########################## Zadanie 7 ########################
## Zapisz do pliku liczbę 123456789, spakuj, rozpakuj dane
## Sprawdź w dokumentacji pakietu struct typ danej
## https://docs.python.org/3/library/struct.html

import struct

number = 123456789
file = open('liczba.bin', 'wb')
file.write(struct.pack('i', number))
file.close()

file = open('liczba.bin', 'rb')
numberf = struct.unpack('i', file.read())
file.close()

print("Odczytana liczba:", numberf[0])

########################## Zadanie 9 #########################
## Utwórz i zapisz do folderu 5 dowolnych plików tekstowych z dowolnym tekstem
##(więcej niż 5 zdań), możesz tez skopiować dowolny tekst.
## Nazwy plików: Tekst1ID_ABC, Tekst2ID_405.txt, Tekst3ID_607.txt, Tekst4ID_ABC.txt, Tekst5ID_DEF.txt
## Uwaga: pisząc program przyjmij założenie, że masz takich nazw plików w folderze tysiące,
## program ma działać niezależnie od liczby plików w folderze
## Utwórz funkcję która:
## a) odczyta z folderu nazwy wszystkich plików
## b) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.
## Utwórz dodatkowową funkcję która wykorzystując poprzednią funkcję sprawdzi:
## a) ile plików zawiera w identyfikatorze ID liczbę 0
## b) dla wszystkich plików które w nazwie nie mają liczby 0
##    wyznaczy liczbę słów
## c) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.

import os

folder_path = 'teksty'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


tekst1 = "Python wspiera różne paradygmaty programowania: obiektowy, imperatywny oraz w mniejszym stopniu funkcyjny. Posiada w pełni dynamiczny system typów i automatyczne zarządzanie pamięcią, będąc w tym podobnym do języków Perl, Ruby, Scheme czy Tcl. Podobnie jak inne języki dynamiczne jest często używany jako język skryptowy. Interpretery Pythona są dostępne na wiele systemów operacyjnych."
tekst2 = "Python rozwijany jest jako projekt Open Source zarządzany przez Python Software Foundation, która jest organizacją non-profit. Standardową implementacją języka jest CPython (napisany w C), ale istnieją też inne, np. Jython (napisany w Javie), CLPython napisany w Common Lisp, IronPython (na platformę .NET) i PyPy (napisany w Pythonie, zob. bootstrap)."
tekst3 = "Pythona stworzył we wczesnych latach 90. Guido van Rossum  jako następcę języka ABC, stworzonego w Centrum voor Wiskunde en Informatica[w innych językach] (CWI  Centrum Matematyki i Informatyki w Amsterdamie). Van Rossum jest głównym twórcą Pythona, choć spory wkład w jego rozwój pochodzi od innych osób. Z racji kluczowej roli, jaką van Rossum pełnił przy podejmowaniu ważnych decyzji projektowych, często określano go przydomkiem „Benevolent Dictator for Life” (BDFL)."
tekst4 = "Nazwa języka nie pochodzi od zwierzęcia, lecz od serialu komediowego emitowanego w latach siedemdziesiątych przez BBC  „Monty Pythons Flying Circus” (Latający cyrk Monty Pythona). Projektant, będąc fanem serialu i poszukując nazwy krótkiej, unikalnej i nieco tajemniczej, uznał tę za świetną[6]."
tekst5 = "Wersja 1.2 była ostatnią wydaną przez CWI. Od 1995 roku Van Rossum kontynuował pracę nad Pythonem w Corporation for National Research Initiatives (CNRI) w Reston w Wirginii, gdzie wydał kilka wersji Pythona, do 1.6 włącznie. W 2000 roku van Rossum i zespół pracujący nad rozwojem jądra Pythona przenieśli się do BeOpen.com, by założyć zespół BeOpen PythonLabs. Pierwszą i jedyną wersją wydaną przez BeOpen.com był Python 2.0."


for i, tekst in enumerate([tekst1, tekst2, tekst3, tekst4, tekst5], start=1):
    with open(os.path.join(folder_path, f"Tekst{i}ID_ABC.txt"), 'w') as file:
        file.write(tekst)

def odczytaj_nazwy_plikow(folder):
    return os.listdir(folder)

nazwy_plikow = odczytaj_nazwy_plikow(folder_path)
print("Nazwy wszystkich plików w folderze:", nazwy_plikow)

def liczba_wyrazow_ABC(folder):
    return sum(
        len(slowo) >= 3
        for nazwa_pliku in os.listdir(folder)
        if nazwa_pliku.endswith('ABC.txt')
        for slowo in open(os.path.join(folder, nazwa_pliku)).read().split()
    )

print("Liczba wyrazów ABC w plikach zakończonych ciągiem znaków 'ABC':", liczba_wyrazow_ABC(folder_path))