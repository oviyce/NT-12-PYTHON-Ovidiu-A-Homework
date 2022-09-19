# Tema 1. Creați un script Python care îndeplinește următoarele funcții:

### 1.1 Declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine);
lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

### 1.2 Afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă);
lista_asc = lista_initiala.copy()
lista_asc.sort()
print(lista_asc)

### 1.3 Afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă);
lista_desc = lista_asc.copy()
lista_desc.reverse()
print(lista_desc)

### 1.4 Afișează o listă ce conține numerele pare din lista ordonată (folosind slice);
lista_pare = lista_asc[1::2]
print(lista_pare)

### 1.5 Afișează o listă ce conține numerele impare din lista ordonată (folosind slice);
lista_impare = lista_desc[1::2]
print(lista_impare)

### 1.6 Afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
lista_multip3 = lista_asc[2::3]
print(lista_multip3)
