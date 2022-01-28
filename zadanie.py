#Projekt
#Szkielet systemu ERP dla serwisu komputerowego
#W połączeniu z SQL ewentualnie z operacjami na plikach

#file = open("<ścierzkę_do_pliku>", "r") |r-read odczyt
#file = open("<ścierzkę_do_pliku>", "w") |w-write zapis

#print(file.read()) -> wyświetlenie zawartości pliku
#print(file.readline()) -> wyświetla nam pierwszą linijkę
#file.write("test który chcemy zapisać")

#Na końcu każdego otwartego pliku musi się znaleść zamknięcie go poprzez file.close()

#Logowanie:
#Klienta - sprawdzić status
#Pracownika - dodać zamówienie, utworzyć konto klienta, edytować dane zamówienia
#Administratora - utworzyć konto pracownika, edytować dane pracownika, lista klientów, lista pracowników

#Rejestracja:
#Pracownik - może założyć konto dla klienta poprzez podanie danych: Numer Klienta, Imię, Nazwisko, Email, Telefon, Adres (hasło generowane automatycznie)
#Administrator - - może założyć konto dla pracownika poprzez podanie danych: Numer Pracownika, Imię, Nazwisko, Email, Telefon, Adres (hasło generowane automatycznie)
#?pierwsze logowanie wymuszenie zmiany hasła?

#Sprawdzić status:
#Klient może sprawdzić swoje zamówienie gdzie wypisany będą dane sprzętu oraz jego aktualny status naprawy

#Dodanie zamówienia:
#numer klienta, numer zamówienia, nazwę sprzętu, dzień oddania, opis usterki, status (przed naprawą, w naprawie, po naprawie)

#Edytowanie danych zamówienia:
#Dzień odbioru, opis usterki, status


#Jest to projekt nakłatki na bazę danych jako podstawowy szkielet systemu erp. Może być zrobiony konsolowo, w GUI z wykorzystaniem biblioteki (thinter),
#lub w formie aplikacji internetowej z wykorzystaniem DJango.
#Oddanie projektu w formie omówienia pracy.

