lista = []
with open("liczby2.txt", "r") as plik:
    for i in plik.readlines():
        lista.append(int(i.strip()))

w10 = 0
w8 = 0

for i in lista:
    licznik = 0
    for j in str(i):
        if j == '6':
            licznik += 1
    w10 += licznik

    liczba_8 = ""
    temp = i
    while temp > 0:
        liczba_8 = str(temp % 8) + liczba_8
        temp //= 8

    licznik_osemkowy = 0
    for j in liczba_8:
        if j == '6':
            licznik_osemkowy += 1
    w8 += licznik_osemkowy

print("6 wystepuje", w10, "razy w systemie dziesietnym i", w8, "razy w systemie osemkowym")
