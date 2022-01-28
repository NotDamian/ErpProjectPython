#SQL Connector pomaga nam na połączeniu programu z bazą danych napisaną w MySQL

#Aby zainstalować blibliotekę należy w Python Pakages wybrać i zainstalować mysql-connector-python

#Kolejnym krokiem jest podpięcie biblioteki bazy danych do projektu:

import mysql.connector

#Następnie łączymy się z nasza bazą danych:

mydb = mysql.connector.connect(     #w pierwszej kolejności musimy wskazać pod jaką nazą będziemy posługiwali się bazą danych w naszym projekcie i uaktywnić połączenie
  host="localhost",                 #W tym miejscu wskazujemy miejsce gdzie znajduje się nasza baza danych jeśli robimy to lokalnie może to być właśnie localhost lub adres 127.0.0.1 jesli robimy to na zewnętrznym serwerze wpisujemy adres serwera
  user="yourusername",              #W tym miejscu wpisujemy login administratora bazy danych
  password="yourpassword",          #W tym miejscu wpisujemy hasło administratora bazy danych
  database="mydatabase"             #Nazwa naszej bazy danych
)

print(mysql)                        #Sprawdzenie czy połaczyliśmy się z bazą danych

#Zakładam że bazę danych będziecie mieli utworzoną wczesniej dlatego skupię się na wpisaniu danych do bazy oraz wydobyciu ich

#Aby wspisać dane do bazy danych po połączeniu się z nią należy użyć

mycursor = mydb.cursor()                                          #Tak samo jak przy klasach nalezy utworzyć nowy obiekt

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"     #Zapytanie SQL pisane w stringu
val = ("John", "Highway 21")                                      #Dane które chcemy zapisać do bazy danych
mycursor.execute(sql, val)                                        #Wpisujemy kod sql i dane do bazy danych

mydb.commit()                                                     #Jest to bardzo ważna komenda, która zapisuje dane w bazie danych inaczej nic nie zostanie zapisane

#Wyciąganie informacji z bazy danych SELECT:

mycursor = mydb.cursor()                                          #Tak samo jak przy klasach nalezy utworzyć nowy obiekt

mycursor.execute("SELECT * FROM customers")                       #Wpisujemy kod sql do bazy danych

myresult = mycursor.fetchall()                                    #Dzięki tej komendzie pobieramy wszystkie ostatnie wierwsze z ostatniego polecenia execute() i wpisujemy je do zmiennej


#Wyciąganie danych za pomocą SELECT i WHERE:

mycursor = mydb.cursor()                                          #Tak samo jak przy klasach nalezy utworzyć nowy obiekt

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"     #Kod SQL aby pobrać dane z bazy

mycursor.execute(sql)                                             #Wpisujemy kod sql do bazy danych

myresult2 = mycursor.fetchall()                                   #Dzięki tej komendzie pobieramy wszystkie ostatnie wierwsze z ostatniego polecenia execute() i wpisujemy je do zmiennej


#Myślę że wiecej informacji nie potrzebujecie aby zrobić projekt za pomocą bazy danych.
