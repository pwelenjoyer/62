lista = []
with open("liczby1.txt", "r") as plik1:
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

maks1 = -1
min1 = float('inf')
max_liczba1 = ""
min_liczba1 = ""

for i in lista:
    liczba_dziesietna = horner(i, 8)
    if liczba_dziesietna > maks1:
        maks1 = liczba_dziesietna
        max_liczba1 = i
    if liczba_dziesietna < min1:
        min1 = liczba_dziesietna
        min_liczba1 = i

maks1 = decToALL(maks1, 8)
min1 = decToALL(min1, 8)
print("maksymalna liczba:", maks1, "minimalna liczba:", min1)
