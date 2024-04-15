################ Methods versus function (metoda vs funkcja)
#### Example
# a = [2, 70, 5, 6]
# a.sort()   # wywołanie metody na obiekcie
# print(a)

# a = [2, 70, 5, 6]
# a = sorted(a)  # override of a variable (nadpisanie zmiennej)
# print(a)

###### Generally, methods and functions have one or more parameters
###### (Metody i funkcje często mają jeden lub więcej parametrów)

#### Example
# a = [2, 70, 5, 6]
# a.sort(reverse=True)
# print(a)
#
# a = [2, 70, 5, 6]
# a = sorted(a, reverse=True)  # override of a variable
# print(a)

######## Function: break() and continue()
## the break() function is often used to stop loops (for, while)
## the continue() function allows to leave a block of instructions and return to the beginning of the loop

## Funkcja break() jest używana często do zakończenia pętli (for, while)
# podczas gdy funkcja continue() pozwala opuścić blok instrukcji i wrócić do początku pętli.

#### Example: the program only prints the numbers 0 1 2 3 4

# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# licz = 0
# while licz in list_1:
#     print(list_1[licz]),
#     licz += 1  # licz = licz + 1
#     if licz >= 5:
#         break

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)




############################## Python module random
## Random module implements pseudo-random number generators for various distributions.

### Example:  random - returns a random float number between 0 and 1
# import random     # generator liczb losowych
# print(random.sample(range(10000),4))
# print(random.choice(range(10000)))


#################### One line if/else statement in Python
########### Example
## Syntax/Składnia: <expression1> if <condition> else <expression2>
## Option 1
# a = 20
# b = 1
# print('większe') if a > b else print('mniejsze')

# Option 2
# a = 1
# b = 20
# x = a > b and print('większe') or print('mniejsze')

# Option 3
# age = 21
# print(('adult', 'kid')[age < 20])  # choice from the tuples

# Option 4
# age = 21
# print(('adult', 'kid')[True])



################################## Python function
## Syntax: def function_name(input_argument1, input_argument2, ... ,input_argumentN):
##       instructions
##      return output_argument   or  return output_arguments
##
##
## Calling the function (wywołanie funkcji )
## name_function(value of input_argument1, ... ,value of input_argumentN)

### Example

# def sum_numbers(x, y):
#     sum_xy = x + y
#     return sum_xy

# print('Result is equal:', sum_numbers(3,5))



####################  Python function:  anonymous function lambda()
#########  Funkcja anonimowa lambda()
## Syntax:     lambda input_arguments: instruction

################# Example

################# Example
# name = 'Ala'
# resultLambda2 = lambda oneWord: oneWord.upper()
# print(resultLambda2(name))



##############################################################
######### Function:  map(), zip(), reduce() i filter()

####### Function map()##################
## Funkcja map() wykonuje operacje z użyciem funkcji na każdym elemencie listy/tupli/słownika:
## Syntax: map(function_name, iter)
## function_name - name of function with one input parameter
## iter is list or dictionary or tuples
## output parameter of mam is list type.
## map() realize operation by using function on each elements of list/tuple/dictionary

######### Example: construct your own function + map()

# def power(number):
#     result = number**2
#     return(result)
#
# list_number = [2, 10, 15, 100, -5]  # equivalent to [double(n) for n in listNumber]
# result_map = map(power, list_number)

# print(list(result_map))  # dump to list

######### Example: construct lambda() + map()

# list_word = ['dnA','RnA']
# print(list_word)
# upper_letter = lambda one_word: one_word.upper()
# result_lambda = map(upper_letter, list_word)  # equivalent to map(lambda one_word: one_word.upper(), list_word)
# print('Result: ', list(result_lambda))

##### Function zip()##########################################################################
# zip() creates pair of elements (tuples) from two list
# zip() tworzy za to listę tupli z podanych elementów

######### Example
# list1 = [1,3,5]
# list2 = [2,4,6]
# resultZip = zip(list1, list2)
# print(list(resultZip))

##### Function reduce()######################################################################
## Funkcja reduce() pobiera dane z sekwencji i zwraca na ich podstawie pojedynczą
## wartość np. sumę liczb. Struktura: functools.reduce(function0, sequence, [initial_value]);
## reduce() realizuje operacje zdeklarowane w function0 na pierwszych dwóch elementów sekwencji, następnie
## wykonuje function0 dla wyniku i trzeciego elementu, aż do wyczerpania elementów sekwencji
## Znajduje się w pakiecie functools

## The reduce(fun,seq) function is used to apply a particular function passed
## in its argument to all of the list elements mentioned in the sequence passed along.
## This function is defined in “functools” module.

######## Example
# import functools, operator
# resultLambda1 = lambda x, y: x + y
# list1 = [1,2,3,4]
# resultReduce1 = functools.reduce(resultLambda1, list1,0)
# print(resultReduce1)

######## Example
## np.można wykorzystywać szereg operacji z użyciem wbudowanych funkcji
## You can use the following operations available as a function:
## Math operations: add(), sub(), mul(), floordiv(), abs()
## Logical operations: not_(), truth()
## Bitwise operations: and_(), or_(), invert()
## Comparisons: eq() -> equal to, ne() -> not equal, lt()->less than,
## le()-less or equal, gt() -> greater than, and ge() -> greater or equal
## Object identity: is_(), is_not()

# import functools, operator
# list2 = [1,2,3,4]
# resultReduce2 = functools.reduce(operator.mul, list2, 1)
# print(resultReduce2)


##### Function filter()########################################################
##Funkcja filter filtruje elementy sekwencji przy użyciu podanej funkcji,
## która musi zwracać wartość True lub False:

## The filter() method filters the given sequence with the help of a function
## that tests each element in the sequence to be true or not.
## Syntax: filter(function, sequence)

######### Example
# list1 = [1,2,3,4]
# def even(x):
#  if x%2 == 0:
#     return True
#  else:
#     return False
#
# resultFilter = filter(even, list1)
# print(list(resultFilter))

########### Function enumerate
## Enumerate() adds a counter to an iterable and returns it in the form of the enumerating object.
##
# def main():
#     print("#### function enumerate ###")
#     a = ['a', 'b', 'c']
##    b = [(0, 'a'), (1, 'b')] # sprawdź poniższe również dla zmiennej b
#
#     for i in enumerate(a):
#         print(i)        # [(0, 'a'), (1, 'b')]
#
#     print("#######")
#     for i in enumerate(a):
#         for j in i:
#             print('j element:', j)
#     print("#######")
#     for i in enumerate(a):
#         for j in i[1]:
#             print('j element:', j)
#
# if __name__ == '__main__':
#     main()











# ################################ Task 1
# Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
##### calculate multiplication x*y. The program stops working if x or y is equal to 0.
# Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
# a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
# program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
# liczbach całkowitych (wstaw odpowiedni warunek).

while True:
    x = int(input('Podaj x: '))
    y = int(input('Podaj y: '))
    print(x*y)
    if(x == 0 or y == 0):
        print('Jedna liczba to 0')
        break
    else:
        continue


# # ################################ Task 2
# Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
# właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)

# Write a program that will display your name if the user enters the correct
# password (the password is stored in a variable)

data = 'Kuba Kuba'
passw = ('123', 'zaq12wsx')
ipassw = (str(input('Podaj haslo: ')))
if(passw.count(ipassw) > 0):
    print(data)
else:
   print('bledne haslo')

################################# Task 3
# Generate list with 100 random numbers (integer type)
# Ascending sort these odd numbers and print only odd numbers from list.

# Wygeneruj listę złożoną z 100 liczb całkowitych parzystych i nieparzystych
# wypisz wszystkie liczby parzyste z tablicy liczby, od najmniejszej do największej.
# Do losowania liczb wykorzystaj moduł random patrz przykład poniżej

import random
numbers = []
for i in range(1,100):
    numbers.insert(i, random.choice(range(100)))
   
numbers.sort()
print(numbers)

############## Task 4
# Uprość kod z Zadania 2 korzystając w w/w struktur
# Simplify the code from Task 2 using a one line if/else statement



print(data) if passw.count(ipassw) > 0 else print('zle haslo')
    
################### Task 5
# Write a function that calculates the quotient of 3 even numbers
# Utwórz funkcje która obliczy iloraz 3 parzystych liczb, użyj "one line statement"

iloraz = lambda a, b, c: a * b * c / 3 if(a%2==0 and b%2==0 and c%2 == 0) else None
print(iloraz(2,4,6))
########################## Task 6
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

nn = ''
name_list = ['K', 'U', 'B', 'A']
res = lambda n: nn.join(n)
print(res(name_list))

########################## Task  7
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string

nname = 'Kuba kuba'

reslam = lambda s: s.split(' ')
split_name = reslam(nname)
print(split_name)
letters = list(split_name)
print(letters)


for word in split_name:
    print(word)
    for letter in word:
        print(letter)
########################## Task 8
# Utwórz funkcję która w dowolnym wyrazie (1 argument funkcji)
# znajdzie dowolną literę (2 argument funkcji)
# użyj lammbda()

word = input('podaj slowo: ')
leterr = input('Podaj litere: ')
ind = lambda word, leterr: word.index(leterr)
print('litera wystepuje na indexie ' + str(ind(word, leterr)) + ' w slowie ' + word)


########################## Task 9
# Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
# podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
# operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
# użyj break, continue, enumerate().
# Następnie login-y i hasła zapisz do słownika (login to klucz słownika).

login = []
passwo = []

while True:
    l = input('Podaj login: ')
    if(l == 'STOP'):
        break
    else:
        login.append(l)
        print('loginy: ', list(enumerate(login)))
    p = input('Podaj haslo: ')
    if(l == 'STOP'):
        break
    else:
        passwo.append(p)
        print('hasla: ', list(enumerate(passwo)))
    
########################## Task 10  - Module in Python
# # Zmodyfikuj poprzednie zadanie, tworząc a następnie importując moduł
# #Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# #Utwórz funkcje Pion: która rysuje gwiazdeki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# obie funkcje są z modułu o nazwie stars

# Korzystając z modułu stars i funkcji Pion Poziom wypisz litery: E, L

import stars

stars.Poziom(12)
stars.Pion(3)
stars.Poziom(12)
stars.Pion(3)
stars.Poziom(12)
print('\n\n')
stars.Pion(7)
stars.Poziom(12)

########################## Task 11
# utwórz moduł o nazwie sil, w którym znajdzie się funkcja silnia (użyj lammbda), a następnie korzystając z
# modułu sil, oblicz symbol Newtona dla dowolnych 2 liczb wskazanych przez
# użytkownika(http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)

import sil
x = sil.silnia(3)
y = sil.silnia(2)
z = sil.silnia(1)
resss = x/(y*z)
print('symbol newtona dla liczb 3 nad 2 to : ' + str(resss))

########################## Task 12
# Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# using filter() and lambda functions.
#  The numbers obtained should be printed in a comma-separated sequence on a single line.

even_numbers = filter(lambda x: x % 2 == 0, range(1, 100))

result = ','.join(map(str, even_numbers))
print(result)

########################## Task 13
### Write a script, using reduce(), which will multiply elements in range (1, 100)
import functools
def multiply(x, y):
    return x * y
result = functools.reduce(multiply, range(1, 100))

print(result)

# ########################## Task 14
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)

resulttt = []
for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        resulttt.append(number)
print(resulttt)


