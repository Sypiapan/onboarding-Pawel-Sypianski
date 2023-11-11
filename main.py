# 16. Stwórz kod, który pobierze liczbę od użytkownika a następnie powie, czy jest parzysta,
# czy nie. Jak pobrać coś od usera? Wygooluj jeśli nie pamiętasz.

number_to_check = int(input(print("Podaj liczbe a ja sprawdzę czy jest parzysta")))
if number_to_check % 2 == 0:
    print(f"Liczba {number_to_check} jest parzysta")
else:
    print(f"Liczba {number_to_check} jest nieparzysta")

# 17. Utwórz stringa a potem zamień jego ostatnią literę z pierwszą.

text = "Litwo Ojczyzno moja"

print(text)
first_letter = text[0]
last_letter = text[-1]
first_letter= text[-1]
last_letter = text[0]
text = first_letter+text[1:-1]+last_letter
print(text)


# 1. Napisz przykłady pętli for, while. Po 3 różne.
#
x = 1
while x < 10:
    print(f"to {x} wyświetlenie, jeszce {9-x} wyświetleń")
    x += 1

book = 99
while book > 20:
    print(f"Aktualna cena {round(book, 2)} PLN - czekam na obnizkę")
    book*=0.8
    print("Przecena 20%, aktualna cena: ", round(book, 2), "PLN")
    print("— — — — — — — — — — — — — — — — — —")
print("\nIdę do księgarni!")


while True:

    x = input(print("""1-Główne Menu \n 2-Księgowość \n 3-Archiwum \n 4-Sprzedaż\n 5 -Zakończenie programu"""))
    if x == "1":
        pass
    elif x == "2":
        pass
    elif x == "3":
        pass
    elif x == "4":
        pass
    elif x == "5":
        print("Zakonczenie programu")
        break


for x in range(0, 10):
    print(f"to {x} wyświetlenie")

imiona = ["Ania", "Kasia", "Basia"]
for imie in imiona:
    print(f"Cześć {imie}")

liczby = [1, 2, 5, 6, 9]
for liczba in liczby:
    print("*" * liczba)

# 2. Napisz artykuł porównujący pętlę for z pętlą while.

"Petlę <for> wykorzystujemy jeśli wiemy ile razy chcemy ją wykonać, petli <while>  używamy gdy liczba powtórze ńest nienanana."
# 3. Do tego charakterystyka porównawcza pętli for i składania.

# 4. Napisz kod, który znajduje największą i najmniejszą liczbę na liście.



liczby = [1, 2,5,44,-3,-6,0]

min = liczby[0]
max = liczby[0]

for liczba in liczby:
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print(f"Najwieksza liczba z listy {liczby} to {max}")
print(f"Najmniejsza liczba z listy {liczby} to {min}")


# 5. Napisz kod, który zliczy wyrazy w zadanym stringu.


text ="Ala ma kota"
number_of_words = 1

for letter in text:
    if letter == ' ':
        number_of_words += 1
print(f"W tekście <{text}> liczba wyrazów to:  {number_of_words} ")


# 6. Następnie litery.
text ="Ala ma kota"
number_of_letters = 0

for letter in text:
    if not letter == ' ':
        number_of_letters += 1

print(f"W tekście <{text}> liczba liter to:  {number_of_letters} ")


# 7. I częstotliwość ich występowania.

text ="Ala ma kota"

dict_of_letters={}
for letter in text:
    letter = letter.lower()
    if not letter == ' ':
        if letter in dict_of_letters:
            dict_of_letters[letter] += 1
        else:
            dict_of_letters[letter] = 1

print(f"W tekście <{text}> częstotliwość wystepowania liter to: {dict_of_letters}")

# 8. Zbadaj czy na zadanej liście, znajdują się dwie liczby – a i b, których suma wynosi
# zadaną liczbę.

liczby = [1,23,34,56,3,6,2,4]

# 9. Napisz kod, który z dowolnej listy(same liczby) wyświetli tylko te, które są mniejsze
# od 5.

liczby = [1,23,34,56,3,6,2,4]

for liczba in liczby:
    if liczba < 5:
        print(liczba)
# 10. Poproś usera o liczbę a następnie wypisz wszystkie dzielniki tejże liczby.

liczba =int(input(print("Podaj liczbę a ja podam jej wszystkie dzielniki")))
i = 1
dzielniki = []
for x in range(2, int(liczba/2+1)):
    if liczba % x == 0:
        dzielniki.append(x)
dzielniki.append(liczba)
print(f"Wszystkie dzielniki {liczba} to {dzielniki}")

# 11. Pobierz od usera dwie liczby a następnie zwróć kwadrat ich sumy.

print("Podaj dwie liczby a ja obliczę  kwadrat ich sumy")
x = int(input(print("Podaj pierwsza liczbę")))
y = int(input(print("Podaj drugą liczbę")))
print((x+y)**2)

# 12. Napisz kod, który wczyta od użytkownika jakiegoś stringa a następnie wyświetli trzy
# pierwsze litery tego stringa, kolejno po sobie, bez nowych linii. Np. “MelonTusk” ->
# “MelMelMel”

x = input(print("Wpisz dowolny tekst, a ja wypisze trzy pierwsze znaki trzykrotnie"))
print(3*x[0:3])

# 13. Pobierz od użytkownika stringa a następnie wyświetl go w odwróconej kolejności
# liter

x = input(print("Wpisz dowolny tekst, a ja wypisze go odwrotnie"))
print(x[::-1])

