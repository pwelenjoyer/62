lista = []
with open("liczby2.txt", "r") as plik1:
    for i in plik1.readlines():
        lista.append(i.strip())

def horner(liczba, x):
    dziesietny = int(liczba[0])
    for i in range(1, len(liczba)):
        dziesietny = dziesietny * x + int(liczba[i])
    return dziesietny

def decToALL(liczba, system):
    wynik = ""
    while liczba > 0:
        remainder = liczba % system
        if remainder >= 10:
            wynik = chr(55 + remainder) + wynik
        else:
            wynik = str(remainder) + wynik
        liczba = liczba // system
    return wynik

najdluzszy_ciag = 0
aktualny_ciag = 1
pierwszy_element = lista[0]
aktualny_pierwszy = lista[0]

for i in range(1, len(lista)):
    if lista[i] >= lista[i - 1]:
        aktualny_ciag += 1
    else:
        if aktualny_ciag > najdluzszy_ciag:
            najdluzszy_ciag = aktualny_ciag
            pierwszy_element = aktualny_pierwszy
        aktualny_ciag = 1
        aktualny_pierwszy = lista[i]
if aktualny_ciag > najdluzszy_ciag:
    najdluzszy_ciag = aktualny_ciag
    pierwszy_element = aktualny_pierwszy
print("pierwszy element:", pierwszy_element, "dlugosc ciagu:", najdluzszy_ciag)
