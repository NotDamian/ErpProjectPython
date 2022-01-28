from cgitb import text
from curses import window
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import mysql.connector
import re
import time

mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="zaq1@WSX",
        database="projekt"
        )


#user
#strona klienta
class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        oo = tk.Label(self, text="Tabela zamowien")
        oo.place(x=2, y=2)

        table_frame = Frame(self)
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

        table.pack()

        def wyloguj():
            controller.show_frame(HomePage)
        B1= tk.Button(self, text="Wyloguj", command=wyloguj )
        B1.place(x=50, y=170)

#worker
#lista zamowien
class OrderList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # with open("order.txt","r") as f:
        #     info = f.readlines()
        #     i =0
        #     for e in info:
        #         nk,n,d,o,s = e.split(",")
        #         order.append([nk,i,n,d,o,s])
        #         i=i+1

        mycursor = mydb.cursor()
        mycursor.execute("SELECT idorder, userId, nazwa, dataZ, opis, statusZ FROM projekt.order")
        myResult = mycursor.fetchall()

        oo = tk.Label(self, text="Tabela zamowien")
        oo.place(x=2, y=2)

        table_frame = Frame(self)
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
            controller.show_frame(WorkerPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=50)
#lista klientow/ urzytkownjikow
class UserList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        mycursor = mydb.cursor()
        mycursor.execute("SELECT userId, name, password, phone, address, emeil, status FROM projekt.user")
        myResult = mycursor.fetchall()


        oo = tk.Label(self, text="Tabela uzytkownikow")
        oo.place(x=2, y=2)

        table_frame = Frame(self)
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
            controller.show_frame(WorkerPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=50)
#twozenie klienta/ uzytkownika
class UserCreate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #register
        l1 = tk.Label(self, text="nazwa")
        l1.place(x=10, y=10)
        t1=tk.Entry(self, width=30)
        t1.place(x=200, y=10)

        l2 = tk.Label(self, text="haslo")
        l2.place(x=10, y=60)
        t2=tk.Entry(self, width=30, show="*")
        t2.place(x=200, y=60)

        l3 = tk.Label(self, text="telefon")
        l3.place(x=10, y=110)
        t3=tk.Entry(self, width=30)
        t3.place(x=200, y=110)

        l4 = tk.Label(self, text="emeil")
        l4.place(x=10, y=160)
        t4=tk.Entry(self, width=30)
        t4.place(x=200, y=160)

        l5 = tk.Label(self, text="address")
        l5.place(x=10, y=210)
        t5=tk.Entry(self, width=30)
        t5.place(x=200, y=210)

        # l6 = tk.Label(self, text="ID klienta")
        # l6.place(x=10, y=260)
        # t6=tk.Entry(self, width=30)
        # t6.place(x=200, y=260)

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
                controller.show_frame(WorkerPage)


        def check():
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            regex1 = '^[0-9]+$'
            if(re.search(regex, str(t4.get()))== None):
                messagebox.showinfo("Error","Zly emeil")
            elif(re.search(regex1, str(t3.get()))== None or len(str(t3.get())) !=9 ):
                messagebox.showinfo("Error","Zly enumer telefonu")
            else:
                create()
    
            
            # if t1.get()!="" or t2.get()!="" or t3.get()!="":
            #     mycursor = mydb.cursor()
            #     sql = "INSERT INTO `projekt`.`user` (userId, name, password, phone,address, emeil) VALUES (%s, %s, %s, %s, %s, %s)"
            #     val=(t6.get(), t1.get(), t2.get(),t3.get(), t5.get(),t4.get())
            #     mycursor.execute(sql, val)
            #     mydb.commit()
            #     controller.show_frame(WorkerPage)

        b1=tk.Button(self, text="Sign in", command=check)
        b1.place(x=200, y=310)
        def back():
            controller.show_frame(WorkerPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=360)
#twozenie zamowienia
class OrderCreate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l1 = tk.Label(self, text="numer klienta")
        l1.place(x=10, y=10)
        t1=tk.Entry(self, width=30)
        t1.place(x=200, y=10)

        # l2 = tk.Label(self, text="numer zamowienia")
        # l2.place(x=10, y=60)
        # t2=tk.Entry(self, width=30)
        # t2.place(x=200, y=60)

        l3 = tk.Label(self, text="nazwa sprzetu")
        l3.place(x=10, y=60)
        t3=tk.Entry(self, width=30)
        t3.place(x=200, y=60)

        # l4 = tk.Label(self, text="dzien oddania")
        # l4.place(x=10, y=160)
        # t4=tk.Entry(self, width=30)
        # t4.place(x=200, y=160)
        t4 = time.strftime("%Y-%m-%d", time.localtime())

        l5 = tk.Label(self, text="opis usterki")
        l5.place(x=10, y=110)
        t5=tk.Entry(self, width=30)
        t5.place(x=200, y=110)

        l6 = tk.Label(self, text="status")
        l6.place(x=10, y=160)
        t6=tk.Entry(self, width=30)
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
                controller.show_frame(WorkerPage)

        b1=tk.Button(self, text="Sign in", command=check)
        b1.place(x=200, y=210)
        def back():
            controller.show_frame(WorkerPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=230)
#edycja zamowienia
class editOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l1 = tk.Label(self, text="id zamowienia")
        l1.place(x=10, y=10)
        t1=tk.Entry(self, width=30)
        t1.place(x=200, y=10)

        l2 = tk.Label(self, text="opis")
        l2.place(x=10, y=60)
        t2=tk.Entry(self, width=30)
        t2.place(x=200, y=60)

        l3 = tk.Label(self, text="status")
        l3.place(x=10, y=110)
        t3=tk.Entry(self, width=30)
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
            controller.show_frame(WorkerPage)
        B1= tk.Button(self, text="zmien", command=zmien )
        B1.place(x=50, y=170)

        def back():
            controller.show_frame(WorkerPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=200)
#panel pracownika
class WorkerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        L1 = tk.Label(self, text="Panel pracownika")
        L1.place(x=50, y=20)

        def checkZamowienia():
            controller.show_frame(OrderList)
        B1= tk.Button(self, text="lista zamowien", command=checkZamowienia )
        B1.place(x=50, y=50)

        def checkUser():
            controller.show_frame(UserList)
        B1= tk.Button(self, text="lista uzytkownikow", command=checkUser )
        B1.place(x=50, y=80)

        def createUser():
            controller.show_frame(UserCreate)
        B1= tk.Button(self, text="stwoz urzytkownika", command=createUser )
        B1.place(x=50, y=110)

        def createOrder():
            controller.show_frame(OrderCreate)
        B1= tk.Button(self, text="stworz zamowienie", command=createOrder )
        B1.place(x=50, y=140)

        def editOrderr():
            controller.show_frame(editOrder)
        B1= tk.Button(self, text="edytuj zamowienie", command=editOrderr )
        B1.place(x=50, y=170)

        def back():
            controller.show_frame(HomePage)
        B1= tk.Button(self, text="Wyloguj", command=back )
        B1.place(x=50, y=200)

#admin
#tworzenie pracownika
class WorkerCreate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #register
        l1 = tk.Label(self, text="nazwa")
        l1.place(x=10, y=10)
        t1=tk.Entry(self, width=30)
        t1.place(x=200, y=10)

        l2 = tk.Label(self, text="haslo")
        l2.place(x=10, y=60)
        t2=tk.Entry(self, width=30, show="*")
        t2.place(x=200, y=60)

        l3 = tk.Label(self, text="telefon")
        l3.place(x=10, y=110)
        t3=tk.Entry(self, width=30)
        t3.place(x=200, y=110)

        l4 = tk.Label(self, text="emeil")
        l4.place(x=10, y=160)
        t4=tk.Entry(self, width=30)
        t4.place(x=200, y=160)

        l5 = tk.Label(self, text="address")
        l5.place(x=10, y=210)
        t5=tk.Entry(self, width=30)
        t5.place(x=200, y=210)

        # l6 = tk.Label(self, text="ID pracownika")
        # l6.place(x=10, y=260)
        # t6=tk.Entry(self, width=30)
        # t6.place(x=200, y=260)

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
                controller.show_frame(AdminPage)

        def check():
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            regex1 = '^[0-9]+$'
            if(re.search(regex, str(t4.get()))== None):
                messagebox.showinfo("Error","Zly emeil")
            elif(re.search(regex1, str(t3.get()))== None or len(str(t3.get())) !=9 ):
                messagebox.showinfo("Error","Zly enumer telefonu")
            else:
                createAdmin()
            # if t1.get()!="" or t2.get()!="" or t3.get()!="":
            #     mycursor = mydb.cursor()
            #     sql = "INSERT INTO `projekt`.`worker` (idworker, name, password, phone,address, emeil) VALUES (%s, %s, %s, %s, %s, %s)"
            #     val=(t6.get(), t1.get(), t2.get(),t3.get(), t5.get(),t4.get())
            #     mycursor.execute(sql, val)
            #     mydb.commit()
            #     controller.show_frame(AdminPage)

        b1=tk.Button(self, text="Sign in", command=check)
        b1.place(x=200, y=310)
        def back():
            controller.show_frame(AdminPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=310)
#edycja pracownika
class WorkerEdit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l1 = tk.Label(self, text="id pracownika")
        l1.place(x=10, y=10)
        t1=tk.Entry(self, width=30)
        t1.place(x=200, y=10)

        l2 = tk.Label(self, text="name")
        l2.place(x=10, y=60)
        t2=tk.Entry(self, width=30)
        t2.place(x=200, y=60)

        l3 = tk.Label(self, text="password")
        l3.place(x=10, y=110)
        t3=tk.Entry(self, width=30)
        t3.place(x=200, y=110)

        l4 = tk.Label(self, text="phone")
        l4.place(x=10, y=160)
        t4=tk.Entry(self, width=30)
        t4.place(x=200, y=160)

        l5 = tk.Label(self, text="address")
        l5.place(x=10, y=210)
        t5=tk.Entry(self, width=30)
        t5.place(x=200, y=210)

        l6 = tk.Label(self, text="emel")
        l6.place(x=10, y=260)
        t6=tk.Entry(self, width=30)
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
            controller.show_frame(AdminPage)
        B1= tk.Button(self, text="zmien", command=zmien )
        B1.place(x=50, y=310)

        def back():
            controller.show_frame(AdminPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=360)
#lista pracownikow
class WorkerList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        mycursor = mydb.cursor()
        mycursor.execute("SELECT idworker, name, password, phone, address, emeil FROM projekt.worker")
        myResult = mycursor.fetchall()


        oo = tk.Label(self, text="Tabela pracownikow")
        oo.place(x=2, y=2)

        table_frame = Frame(self)
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
            controller.show_frame(AdminPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=50)
#lista klientow/ urzytkownjikow
class checkUserAdmin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        mycursor = mydb.cursor()
        mycursor.execute("SELECT userId, name, password, phone, address, emeil, status FROM projekt.user")
        myResult = mycursor.fetchall()


        oo = tk.Label(self, text="Tabela uzytkownikow")
        oo.place(x=2, y=2)

        table_frame = Frame(self)
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
            controller.show_frame(AdminPage)
        B1= tk.Button(self, text="back", command=back )
        B1.place(x=50, y=50)
#panel adnima
class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        L1 = tk.Label(self, text="Panel admina")
        L1.place(x=50, y=20)

        def createWorker():
            controller.show_frame(WorkerCreate)
        B1= tk.Button(self, text="stworz pracownika", command=createWorker )
        B1.place(x=50, y=50)

        def editWorker():
            controller.show_frame(WorkerEdit)
        B1= tk.Button(self, text="edytuj pracownika", command=editWorker )
        B1.place(x=50, y=80)

        def checkWorker():
            controller.show_frame(WorkerList)
        B1= tk.Button(self, text="lista pracownikow", command=checkWorker )
        B1.place(x=50, y=110)

        def checkUserAdminn():
            controller.show_frame(checkUserAdmin)
        B1= tk.Button(self, text="lista urzytkownikow", command=checkUserAdminn )
        B1.place(x=50, y=140)

        def wyloguj():
            controller.show_frame(HomePage)
        B1= tk.Button(self, text="Wyloguj", command=wyloguj )
        B1.place(x=50, y=170)



#home page and program
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        border=tk.LabelFrame(self,text="login", bd=10)
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
                    controller.show_frame(UserPage)
            #worker
            mycursor = mydb.cursor()
            mycursor.execute("SELECT idworker, name, password FROM projekt.worker")
            myResult = mycursor.fetchall()

            for i in myResult:
                if i[1] == T1.get() and i[2] == T2.get():
                    controller.show_frame(WorkerPage)
                    mycursor = mydb.cursor()

            #admin
            mycursor.execute("SELECT idadmin, name, password FROM projekt.admin")
            myResult = mycursor.fetchall()

            for i in myResult:
                if i[1] == T1.get() and i[2] == T2.get():
                    controller.show_frame(AdminPage)


        Button = tk.Button(border, text="zaloguj", command=verify)
        Button.place(x=320, y=115)

class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #create widnow
        # window = tk.StringVar()
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.frames={}
        for F in (HomePage, UserPage, WorkerPage, AdminPage, UserCreate,WorkerCreate, OrderCreate, OrderList,UserList,WorkerList,checkUserAdmin,editOrder, WorkerEdit):
            frame = F(window, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(HomePage)
    def show_frame(self, page):
        frame=self.frames[page]
        frame.tkraise()

app= Program()
app.mainloop()