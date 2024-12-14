lista1 = []
with open("liczby1.txt", "r") as plik1:
    for i in plik1.readlines():
        lista1.append(int(i.strip(), 8))
lista2 = []
with open("liczby2.txt", "r") as plik2:
    for i in plik2.readlines():
        lista2.append(int(i.strip()))

takie_same = 0
wieksza_w_1 = 0

for i1, i2 in zip(lista1, lista2):
    if i1 == i2:
        takie_same += 1
    elif i1 > i2:
        wieksza_w_1 += 1
print("takie same:", takie_same, "w liczby1 wieksza niz w liczb2:", wieksza_w_1)