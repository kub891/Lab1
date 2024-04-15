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