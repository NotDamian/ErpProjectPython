from cgitb import text
from curses import window
from pickletools import long4
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import mysql.connector
import re
import time





root = Tk()
root.geometry("800x500")

mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="zaq1@WSX",
        database="projekt"
    )
#user
#userPage
def UserPage():
    oo = tk.Label( text="Tabela zamowien")
    oo.place(x=2, y=2)
    table_frame = Frame()
    table_frame.pack()
    table = ttk.Treeview(table_frame)

    table['columns'] = ('numer_klienta', 'numer_zamowienia','nazwa','dzien','opis','status')
    table.column("#0", width=0, stretch=NO)
    table.column("numer_klienta",anchor=CENTER, width=80)
    table.column("numer_zamowienia",anchor=CENTER, width=80)
    table.column("nazwa",anchor=CENTER, width=80)
    table.column("dzien",anchor=CENTER, width=80)
    table.column("opis",anchor=CENTER, width=80)
    table.column("status",anchor=CENTER, width=80)

    table.heading("#0",text="", anchor=CENTER)
    table.heading("numer_klienta",text="Numer klienta",anchor=CENTER)
    table.heading("numer_zamowienia",text="numer zamowienia",anchor=CENTER)
    table.heading("nazwa",text="nazwa",anchor=CENTER)
    table.heading("dzien",text="dzien oddania",anchor=CENTER)
    table.heading("opis",text="opis",anchor=CENTER )
    table.heading("status",text="status",anchor=CENTER )


    mycursor22 = mydb.cursor()
    mycursor22.execute("SELECT id FROM projekt.idKlienta")
    myResult22 = mycursor22.fetchall()
    print(myResult22[0])
    print(myResult22[0][0])

    mycursor = mydb.cursor()
    sss = "SELECT idorder, userId, nazwa, dataZ, opis, statusZ FROM projekt.order WHERE userId = %s"
    vv = myResult22[0][0]
    mycursor.execute(sss, (vv,))
    myResult = mycursor.fetchall()

    l=0
    for i in myResult:
        table.insert(parent="", index='end', iid=l, text="", values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        l+=1


    def wyloguj():
        oo.destroy()
        table_frame.destroy()
        table.destroy()
        B1.destroy()
        HomePage()
    B1= tk.Button(text="Wyloguj", command=wyloguj)
    B1.place(x=50, y=200)
    table.pack()

#worker
#lista zamowien
def OrderList():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT idorder, userId, nazwa, dataZ, opis, statusZ FROM projekt.order")
    myResult = mycursor.fetchall()

    oo = tk.Label(text="Tabela zamowien")
    oo.place(x=2, y=2)

    table_frame = Frame()
    table_frame.pack()
    table = ttk.Treeview(table_frame)

    table['columns'] = ('numer_klienta', 'numer_zamowienia','nazwa','dzien','opis','status')
    table.column("#0", width=0, stretch=NO)
    table.column("numer_klienta",anchor=CENTER, width=80)
    table.column("numer_zamowienia",anchor=CENTER, width=80)
    table.column("nazwa",anchor=CENTER, width=80)
    table.column("dzien",anchor=CENTER, width=80)
    table.column("opis",anchor=CENTER, width=80)
    table.column("status",anchor=CENTER, width=80)

    table.heading("#0",text="", anchor=CENTER)
    table.heading("numer_klienta",text="Numer klienta",anchor=CENTER)
    table.heading("numer_zamowienia",text="numer zamowienia",anchor=CENTER)
    table.heading("nazwa",text="nazwa",anchor=CENTER)
    table.heading("dzien",text="dzien oddania",anchor=CENTER)
    table.heading("opis",text="opis",anchor=CENTER )
    table.heading("status",text="status",anchor=CENTER )


    l=0
    for i in myResult:
        table.insert(parent="", index='end', iid=l, text="", values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        l+=1

    table.pack()

    def back():
        oo.destroy()
        table.destroy()
        table_frame.destroy()
        B1.destroy()
        WorkerPage()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=50)

#ulista klientow
def UserList():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT userId, name, password, phone, address, emeil, status FROM projekt.user")
    myResult = mycursor.fetchall()


    oo = tk.Label(text="Tabela uzytkownikow")
    oo.place(x=2, y=2)

    table_frame = Frame()
    table_frame.pack()
    table = ttk.Treeview(table_frame)

    table['columns'] = ('userId', 'name','password','phone','address', 'emeil')
    table.column("#0", width=0, stretch=NO)
    table.column("userId",anchor=CENTER, width=80)
    table.column("name",anchor=CENTER, width=80)
    table.column("password",anchor=CENTER, width=80)
    table.column("phone",anchor=CENTER, width=80)
    table.column("address",anchor=CENTER, width=80)
    table.column("emeil",anchor=CENTER, width=80)


    table.heading("#0",text="", anchor=CENTER)
    table.heading("userId",text="Numer klienta",anchor=CENTER)
    table.heading("name",text="nazwa",anchor=CENTER)
    table.heading("password",text="haslo",anchor=CENTER)
    table.heading("phone",text="telefon",anchor=CENTER)
    table.heading("address",text="address",anchor=CENTER )
    table.heading("emeil",text="emeil",anchor=CENTER )

    l=0
    for i in myResult:
        table.insert(parent="", index='end', iid=l, text="", values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        l+=1

    table.pack()

    def back():
        oo.destroy()
        table.destroy()
        table_frame.destroy()
        B1.destroy()
        WorkerPage()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=50)

#tworzenie klienta
def UserCreate():
    #register
    l1 = tk.Label(text="nazwa")
    l1.place(x=10, y=10)
    t1=tk.Entry(width=30)
    t1.place(x=200, y=10)

    l2 = tk.Label(text="haslo")
    l2.place(x=10, y=60)
    t2=tk.Entry(width=30, show="*")
    t2.place(x=200, y=60)

    l3 = tk.Label(text="telefon")
    l3.place(x=10, y=110)
    t3=tk.Entry(width=30)
    t3.place(x=200, y=110)

    l4 = tk.Label(text="emeil")
    l4.place(x=10, y=160)
    t4=tk.Entry(width=30)
    t4.place(x=200, y=160)

    l5 = tk.Label(text="address")
    l5.place(x=10, y=210)
    t5=tk.Entry(width=30)
    t5.place(x=200, y=210)

    def create():
        if t1.get()!="" or t2.get()!="" or t3.get()!="":
            #pobieranie ostatniego nr Id klienta
            myId = mydb.cursor()
            myId.execute("SELECT userId FROM projekt.user ORDER BY userId DESC")
            myR = myId.fetchall()
            t6 = myR[0]

            mycursor = mydb.cursor()
            sql = "INSERT INTO `projekt`.`user` (userId, name, password, phone,address, emeil) VALUES (%s, %s, %s, %s, %s, %s)"
            val=(int(t6[0])+1, t1.get(), t2.get(),t3.get(), t5.get(),t4.get())
            mycursor.execute(sql, val)
            mydb.commit()

            l1.destroy()
            l2.destroy()
            l3.destroy()
            l4.destroy()
            l5.destroy()
            t1.destroy()
            t2.destroy()
            t3.destroy()
            t4.destroy()
            t5.destroy()
            b1.destroy()
            B1.destroy()
            WorkerPage()

    def check():
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex1 = '^[0-9]+$'
        if(re.search(regex, str(t4.get()))== None):
            messagebox.showinfo("Error","Zly emeil")
        elif(re.search(regex1, str(t3.get()))== None or len(str(t3.get())) !=9 ):
            messagebox.showinfo("Error","Zly enumer telefonu")
        else:
            create()
    b1=tk.Button(text="Sign in", command=check)
    b1.place(x=200, y=310)

    def back():
            l1.destroy()
            l2.destroy()
            l3.destroy()
            l4.destroy()
            l5.destroy()
            t1.destroy()
            t2.destroy()
            t3.destroy()
            t4.destroy()
            t5.destroy()
            b1.destroy()
            B1.destroy()
            WorkerPage()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=360)

#tworzenie zamowienia
def OrderCreate():
    l1 = tk.Label(text="numer klienta")
    l1.place(x=10, y=10)
    t1=tk.Entry(width=30)
    t1.place(x=200, y=10)

    # l2 = tk.Label(text="numer zamowienia")
    # l2.place(x=10, y=60)
    # t2=tk.Entry(width=30)
    # t2.place(x=200, y=60)

    l3 = tk.Label(text="nazwa sprzetu")
    l3.place(x=10, y=60)
    t3=tk.Entry(width=30)
    t3.place(x=200, y=60)

    # l4 = tk.Label(text="dzien oddania")
    # l4.place(x=10, y=160)
    # t4=tk.Entry(width=30)
    # t4.place(x=200, y=160)
    t4 = time.strftime("%Y-%m-%d", time.localtime())

    l5 = tk.Label(text="opis usterki")
    l5.place(x=10, y=110)
    t5=tk.Entry(width=30)
    t5.place(x=200, y=110)

    l6 = tk.Label(text="status")
    l6.place(x=10, y=160)
    t6=tk.Entry(width=30)
    t6.insert(0,"Przyjete")
    t6.place(x=200, y=160)

    def check():
        if t1.get()!="" or t3.get()!="" or t5.get()!="" or t6.get()!="":
            #pobieranie ostatniego nr Id zamowienia
            myId = mydb.cursor()
            myId.execute("SELECT idorder FROM projekt.order ORDER BY idorder DESC")
            myR = myId.fetchall()
            t2 = myR[0]
            mycursor = mydb.cursor()
            sql = "INSERT INTO `projekt`.`order` (idorder, userId, nazwa, dataZ,opis, statusZ) VALUES (%s, %s, %s, %s, %s, %s)"
            val=(int(t2[0])+1, t1.get(), t3.get(), t4, t5.get(),t6.get())
            mycursor.execute(sql, val)
            mydb.commit()

            l1.destroy()
            l3.destroy()
            l5.destroy()
            l6.destroy()
            t1.destroy()
            t3.destroy()
            t5.destroy()
            t6.destroy()
            t3.destroy()
            b1.destroy()
            B1.destroy()
            WorkerPage()

    b1=tk.Button(text="Sign in", command=check)
    b1.place(x=200, y=210)
    def back():
        l1.destroy()
        l3.destroy()
        l5.destroy()
        l6.destroy()
        t1.destroy()
        t3.destroy()
        t5.destroy()
        t6.destroy()
        t3.destroy()
        b1.destroy()
        B1.destroy()
        WorkerPage()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=230)

#editOrder
def editOrder():
    l1 = tk.Label(text="id zamowienia")
    l1.place(x=10, y=10)
    t1=tk.Entry(width=30)
    t1.place(x=200, y=10)

    l2 = tk.Label(text="opis")
    l2.place(x=10, y=60)
    t2=tk.Entry(width=30)
    t2.place(x=200, y=60)

    l3 = tk.Label(text="status")
    l3.place(x=10, y=110)
    t3=tk.Entry(width=30)
    t3.place(x=200, y=110)



    def zmien():

        #jesli puste pola uzupelnij starymi danymi
        mycursor1 = mydb.cursor()
        ss="SELECT idorder, opis, statusZ FROM projekt.order WHERE idorder = %s"
        v = (str(t1.get()))
        mycursor1.execute(ss,(v,))
        myResult = mycursor1.fetchall()

        for i in myResult:
            if t2.get()!="":
                tt2 = str(t2.get())
            else:
                t2.insert(0,i[1])

            if t3.get()!="":
                tt3 = str(t3.get())
            else:
                t3.insert(0,i[2])

        mycursor = mydb.cursor()
        sql = "UPDATE projekt.order SET opis = %s, statusZ = %s  WHERE idorder = %s"
        val = (str(t2.get()), str(t3.get()), str(t1.get()))
        mycursor.execute(sql, val)
        mydb.commit()

        l1.destroy()
        l2.destroy()
        l3.destroy()
        t1.destroy()
        t2.destroy()
        t3.destroy()
        b1.destroy()
        B1.destroy()
        WorkerPage()
    b1= tk.Button(text="zmien", command=zmien )
    b1.place(x=50, y=170)

    def back():
        l1.destroy()
        l2.destroy()
        l3.destroy()
        t1.destroy()
        t2.destroy()
        t3.destroy()
        b1.destroy()
        B1.destroy()
        WorkerPage()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=200)

#panelPracownka
def WorkerPage():
    L1 = tk.Label(text="Panel pracownika")
    L1.place(x=50, y=20)

    def checkZamowienia():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        OrderList()
    B1= tk.Button(text="lista zamowien", command=checkZamowienia )
    B1.place(x=50, y=50)

    def checkUser():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        UserList()
    B2= tk.Button(text="lista uzytkownikow", command=checkUser )
    B2.place(x=50, y=80)

    def createUser():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        UserCreate()
    B3= tk.Button(text="stwoz urzytkownika", command=createUser )
    B3.place(x=50, y=110)

    def createOrder():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        OrderCreate()
    B4= tk.Button(text="stworz zamowienie", command=createOrder )
    B4.place(x=50, y=140)

    def editOrderr():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        editOrder()
    B5= tk.Button(text="edytuj zamowienie", command=editOrderr )
    B5.place(x=50, y=170)

    def back():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        B6.destroy()
        HomePage()
    B6= tk.Button(text="Wyloguj", command=back )
    B6.place(x=50, y=200)

#admin
#tworzenie pracownika
def WorkerCreate():
    #register
    l1 = tk.Label(text="nazwa")
    l1.place(x=10, y=10)
    t1=tk.Entry(width=30)
    t1.place(x=200, y=10)

    l2 = tk.Label(text="haslo")
    l2.place(x=10, y=60)
    t2=tk.Entry(width=30, show="*")
    t2.place(x=200, y=60)

    l3 = tk.Label(text="telefon")
    l3.place(x=10, y=110)
    t3=tk.Entry(width=30)
    t3.place(x=200, y=110)

    l4 = tk.Label(text="emeil")
    l4.place(x=10, y=160)
    t4=tk.Entry(width=30)
    t4.place(x=200, y=160)

    l5 = tk.Label(text="address")
    l5.place(x=10, y=210)
    t5=tk.Entry(width=30)
    t5.place(x=200, y=210)


    def createAdmin():
        if t1.get()!="" or t2.get()!="" or t3.get()!="":
            #pobieranie ostatniego nr Id pracownika
            myId = mydb.cursor()
            myId.execute("SELECT idworker FROM projekt.worker ORDER BY idworker DESC")
            myR = myId.fetchall()
            t6 = myR[0]

            mycursor = mydb.cursor()
            sql = "INSERT INTO `projekt`.`worker` (idworker, name, password, phone,address, emeil) VALUES (%s, %s, %s, %s, %s, %s)"
            val=(int(t6[0])+1, t1.get(), t2.get(),t3.get(), t5.get(),t4.get())
            mycursor.execute(sql, val)
            mydb.commit()

            l1.destroy()
            l2.destroy()
            l3.destroy()
            l4.destroy()
            l5.destroy()
            t1.destroy()
            t2.destroy()
            t3.destroy()
            t4.destroy()
            t5.destroy()
            B1.destroy()
            b1.destroy()
            AdminPagee()

    def check():
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex1 = '^[0-9]+$'
        if(re.search(regex, str(t4.get()))== None):
            messagebox.showinfo("Error","Zly emeil")
        elif(re.search(regex1, str(t3.get()))== None or len(str(t3.get())) !=9 ):
            messagebox.showinfo("Error","Zly enumer telefonu")
        else:
            createAdmin()


    b1=tk.Button(text="Sign in", command=check)
    b1.place(x=200, y=310)
    def back():
        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()
        t5.destroy()
        B1.destroy()
        b1.destroy()
        AdminPagee()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=310)

#edycja pracownikow
def WorkerEdit():
    l1 = tk.Label(text="id pracownika")
    l1.place(x=10, y=10)
    t1=tk.Entry(width=30)
    t1.place(x=200, y=10)

    l2 = tk.Label(text="name")
    l2.place(x=10, y=60)
    t2=tk.Entry(width=30)
    t2.place(x=200, y=60)

    l3 = tk.Label(text="password")
    l3.place(x=10, y=110)
    t3=tk.Entry(width=30)
    t3.place(x=200, y=110)

    l4 = tk.Label(text="phone")
    l4.place(x=10, y=160)
    t4=tk.Entry(width=30)
    t4.place(x=200, y=160)

    l5 = tk.Label(text="address")
    l5.place(x=10, y=210)
    t5=tk.Entry(width=30)
    t5.place(x=200, y=210)

    l6 = tk.Label(text="emel")
    l6.place(x=10, y=260)
    t6=tk.Entry(width=30)
    t6.place(x=200, y=260)



    def zmien():

        #jesli puste pola uzupelnij starymi danymi
        mycursor1 = mydb.cursor()
        ss="SELECT idworker, name, password, phone, address, emeil, status FROM projekt.worker WHERE idworker = %s"
        v = (str(t1.get()))
        mycursor1.execute(ss,(v,))
        myResult = mycursor1.fetchall()

        for i in myResult:
            if t2.get()!="":
                tt2 = str(t2.get())
            else:
                t2.insert(0,i[1])

            if t3.get()!="":
                tt3 = str(t3.get())
            else:
                t3.insert(0,i[2])

            if t4.get()!="":
                tt4 = str(t4.get())
            else:
                t4.insert(0,i[3])

            if t5.get()!="":
                tt5 = str(t5.get())
            else:
                t5.insert(0,i[4])

            if t6.get()!="":
                tt6= str(t6.get())
            else:
                t6.insert(0,i[5])
        mycursor = mydb.cursor()
        sql = "UPDATE projekt.worker SET name = %s, password = %s, phone = %s, address = %s, emeil = %s  WHERE idworker = %s"
        # val = (tt2, tt3, tt4, tt5, tt6, str(t1.get()))
        val = (str(t2.get()), str(t3.get()), str(t4.get()), str(t5.get()), str(t6.get()), str(t1.get()))
        mycursor.execute(sql, val)
        mydb.commit()

        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        l6.destroy()
        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()
        t5.destroy()
        t6.destroy()
        B1.destroy()
        b1.destroy()
        AdminPagee()
    b1= tk.Button(text="zmien", command=zmien )
    b1.place(x=50, y=310)

    def back():
        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        l6.destroy()
        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()
        t5.destroy()
        t6.destroy()
        B1.destroy()
        b1.destroy()
        AdminPagee()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=360)

#listaPracowbnikow
def WorkerList():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT idworker, name, password, phone, address, emeil FROM projekt.worker")
    myResult = mycursor.fetchall()


    oo = tk.Label(text="Tabela pracownikow")
    oo.place(x=2, y=2)

    table_frame = Frame()
    table_frame.pack()
    table = ttk.Treeview(table_frame)

    table['columns'] = ('idworker', 'name','password','phone','address', 'emeil')
    table.column("#0", width=0, stretch=NO)
    table.column("idworker",anchor=CENTER, width=80)
    table.column("name",anchor=CENTER, width=80)
    table.column("password",anchor=CENTER, width=80)
    table.column("phone",anchor=CENTER, width=80)
    table.column("address",anchor=CENTER, width=80)
    table.column("emeil",anchor=CENTER, width=80)


    table.heading("#0",text="", anchor=CENTER)
    table.heading("idworker",text="Numer pracownika",anchor=CENTER)
    table.heading("name",text="nazwa",anchor=CENTER)
    table.heading("password",text="haslo",anchor=CENTER)
    table.heading("phone",text="telefon",anchor=CENTER)
    table.heading("address",text="address",anchor=CENTER )
    table.heading("emeil",text="emeil",anchor=CENTER )

    l=0
    for i in myResult:
        table.insert(parent="", index='end', iid=l, text="", values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        l+=1

    table.pack()

    def back():
        oo.destroy()
        table_frame.destroy()
        B1.destroy()
        AdminPagee()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=50)

#lista klientow
def checkUserAdmin():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT userId, name, password, phone, address, emeil, status FROM projekt.user")
    myResult = mycursor.fetchall()


    oo = tk.Label(text="Tabela uzytkownikow")
    oo.place(x=2, y=2)

    table_frame = Frame()
    table_frame.pack()
    table = ttk.Treeview(table_frame)

    table['columns'] = ('userId', 'name','password','phone','address', 'emeil')
    table.column("#0", width=0, stretch=NO)
    table.column("userId",anchor=CENTER, width=80)
    table.column("name",anchor=CENTER, width=80)
    table.column("password",anchor=CENTER, width=80)
    table.column("phone",anchor=CENTER, width=80)
    table.column("address",anchor=CENTER, width=80)
    table.column("emeil",anchor=CENTER, width=80)


    table.heading("#0",text="", anchor=CENTER)
    table.heading("userId",text="Numer klienta",anchor=CENTER)
    table.heading("name",text="nazwa",anchor=CENTER)
    table.heading("password",text="haslo",anchor=CENTER)
    table.heading("phone",text="telefon",anchor=CENTER)
    table.heading("address",text="address",anchor=CENTER )
    table.heading("emeil",text="emeil",anchor=CENTER )

    l=0
    for i in myResult:
        table.insert(parent="", index='end', iid=l, text="", values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        l+=1

    table.pack()

    def back():
        table_frame.destroy()
        oo.destroy()
        B1.destroy()
        AdminPagee()
    B1= tk.Button(text="back", command=back )
    B1.place(x=50, y=50)

#panel adnina
def AdminPagee():
    L1 = tk.Label(text="Panel admina")
    L1.place(x=50, y=20)

    def createWorker():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        WorkerCreate()
    B1= tk.Button(text="stworz pracownika", command=createWorker )
    B1.place(x=50, y=50)

    def editWorker():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        WorkerEdit()
    B2= tk.Button(text="edytuj pracownika", command=editWorker )
    B2.place(x=50, y=80)

    def checkWorker():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        WorkerList()
    B3= tk.Button(text="lista pracownikow", command=checkWorker )
    B3.place(x=50, y=110)

    def checkUserAdminn():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        checkUserAdmin()
    B4= tk.Button(text="lista urzytkownikow", command=checkUserAdminn )
    B4.place(x=50, y=140)

    def wyloguj():
        L1.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        HomePage()
    B5= tk.Button(text="Wyloguj", command=wyloguj )
    B5.place(x=50, y=170)
#homePage
def HomePage():
    border=tk.LabelFrame(text="login", bd=10)
    border.pack(fill="both", expand="yes", padx=150, pady=150)

    L1 = tk.Label(border, text="Nazwa")
    L1.place(x=50, y=20)
    T1=tk.Entry(border, width=30, bd=5)
    T1.place(x=180, y=20)

    L2 = tk.Label(border, text="Haslo")
    L2.place(x=50, y=80)
    T2=tk.Entry(border, width=30, bd=5, show="*")
    T2.place(x=180, y=80)

    def verify():
         #user
        mycursor = mydb.cursor()
        mycursor.execute("SELECT userId, name, password FROM projekt.user")
        myResult = mycursor.fetchall()
        for i in myResult:
            if i[1] == T1.get() and i[2] == T2.get():
                mycursor11 = mydb.cursor()
                sql = "UPDATE projekt.idKlienta SET id = %s LIMIT 1"
                val = str(i[0])
                mycursor11.execute(sql, (val,))
                mydb.commit()
                border.destroy()
                UserPage()
        #worker
            mycursor = mydb.cursor()
            mycursor.execute("SELECT idworker, name, password FROM projekt.worker")
            myResult = mycursor.fetchall()

            for i in myResult:
                if i[1] == T1.get() and i[2] == T2.get():
                    border.destroy()
                    WorkerPage()
                    mycursor = mydb.cursor()

            #admin
            mycursor.execute("SELECT idadmin, name, password FROM projekt.admin")
            myResult = mycursor.fetchall()

            for i in myResult:
                if i[1] == T1.get() and i[2] == T2.get():
                    border.destroy()
                    AdminPagee()


    Button = tk.Button(border, text="zaloguj", command=verify)
    Button.place(x=320, y=115)



HomePage()
root.mainloop()
