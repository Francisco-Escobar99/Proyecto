#import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
from time import time
import time
from random import randint
import threading
from threading import Thread, Lock
import random
import tkinter
root = Tk()

ArrayPedidos = []
ArrayMesas = []
aux = 0

root.title("ProyectPConcurrente")  # Titulo de la ventana
# root.geometry("500x450") # Dimension de la ventana
root.geometry("975x500")
label1 = Label(root, text="RESTAURANTE", bg="slate grey",
               font=("Segoe Script", 24))
label1.pack(fill=tkinter.X)
img = PhotoImage(file='images.png')
lbl_img = Label(root, image = img).pack()
lbl_img =Label(root).place(x=975,y=500)

def mesa1():  # Funcion que simula la mesa
    numMesa = 1  # Se establece el numero de mesa y se pasa como parametro
    # Hilo en el cual se hara el "proceso" del pedido
    threading.Thread(target=threading.Thread(
        target=preparar, args=(numMesa,)).start())

def mesa2():
    numMesa = 2
    threading.Thread(target=threading.Thread(target=preparar, args=(
        numMesa,)).start())  # Cada hilo es independiente al resto


def mesa3():
    numMesa = 3
    threading.Thread(target=threading.Thread(
        target=preparar, args=(numMesa,)).start())


def mesa4():
    numMesa = 4
    threading.Thread(target=threading.Thread(
        target=preparar, args=(numMesa,)).start())


def mesa5():
    numMesa = 5
    threading.Thread(target=threading.Thread(
        target=preparar, args=(numMesa,)).start())

def preparar(num):
    global window
    bandera = 0  # Simula ser el numero de pedido
    while True:  # Ciclo While para simular la realizacion de los pedidos
        time_sleep = random.randint(1, 5)  # tiempo de ejecucion (Random)
        time.sleep(time_sleep)
        if num == 1:  # Se evalua que numero de mesa es
            # Se extrae el numero de pedidos que se ingresó
            pedidos = int(entry1.get())
        if num == 2:
            pedidos = int(entry2.get())
        if num == 3:
            pedidos = int(entry3.get())
        if num == 4:
            pedidos = int(entry4.get())
        if num == 5:
            pedidos = int(entry5.get())
        # Se imprime el platillo listo y el numero de mesa que pertenece el pedido
        print("Platillo ", bandera + 1, "de mesa ", num, "listo!")
        ArrayPedidos.append(bandera+1) # Guardamos el numero de platillo listo en el Array
        ArrayMesas.append(num) # Guardamos el numero de mesa en el Array
        #threading.Thread(target=threading.Thread(target=guardar, args=(pedidos,num)).start())
        bandera += 1  # Se aumenta uno, simulando que es otro pedido
        if (bandera == pedidos):  # Se evalua la cantidad de pedidos que se van preparando con la cantidad que pidio el cliente
            # Al cumplirse la condicion significa que se ha terminado de hacer los pedidos
            print("--Pedidos de mesa ", num, "terminados!--")
            break

# VENTANA 2
def mostrar():
    # window.mainloop()
    print(ArrayPedidos)
    print(ArrayMesas)
    window = tk.Tk()
    window.resizable(width=1, height=1)
    window.geometry("975x500")
    label1 = Label(window, text="PLATILLOS LISTOS", bg="slate grey",
               font=("Segoe Script", 24))
    label1.pack(fill=tkinter.X)

    # Using treeview widget
    treev = ttk.Treeview(window, selectmode='browse')
    treev.pack()
    # Defining number of columns
    treev["columns"] = ("1", "2")
    # Defining heading
    treev['show'] = 'headings'
    # Assigning the width and anchor to  the respective columns
    treev.column("1", width=90, anchor='c')
    treev.column("2", width=90, anchor='c')
    # Assigning the heading names to the respective columns
    treev.heading("1", text=" Pedido")
    treev.heading("2", text=" Mesa")
    ListPedidos = list(reversed(ArrayPedidos))
    ListMesas = list(reversed(ArrayMesas))
    for i in range(len(ArrayPedidos)):
        treev.insert("",0, text="L1", values=(ListPedidos[i],ListMesas[i]))

# Label para la instruccion al cliente
my_label1 = Label(root, text="Ingrese numero de pedidos para la mesa 1")
my_label1.place(x=390,y=90)  # Posicionamos el label
# Entrada de texto, donde se ingresa la cantidad de pedidos
entry1 = Entry(root)
entry1.place(x=446,y=120)  # Se posiciona la entrada de texto
# Boton para realizar el pedido de la mesa correspondiente
my_button1 = Button(root, text="Hacer pedidos", command=mesa1) # llamamos a la funcion mesa1
my_button1.place(x=465,y=145)  # Posicionamos el boton

my_label2 = Label(root, text="Ingrese numero de pedidos para la mesa 2")
my_label2.place(x=390,y=176)
entry2 = Entry(root)
entry2.place(x=446,y=206)
my_button2 = Button(root, text="Hacer pedidos", command=mesa2)
my_button2.place(x=465,y=229)

my_label3 = Label(root, text="Ingrese numero de pedidos para la mesa 3")
my_label3.place(x=390,y=262) 
entry3 = Entry(root)
entry3.place(x=446,y=292)
my_button3 = Button(root, text="Hacer pedidos", command=mesa3)
my_button3.place(x=465,y=315)

my_label4 = Label(root, text="Ingrese numero de pedidos para la mesa 4")
my_label4.place(x=390,y=348) 
entry4 = Entry(root)
entry4.place(x=446,y=378)
my_button4 = Button(root, text="Hacer pedidos", command=mesa4)
my_button4.place(x=465,y=401)

my_label5 = Label(root, text="Ingrese numero de pedidos para la mesa 5")
my_label5.place(x=390,y=434) 
entry5 = Entry(root)
entry5.place(x=446,y=464)
my_button5 = Button(root, text="Hacer pedidos", command=mesa5)
my_button5.place(x=465,y=497)

boton = Button(root, text='Ver platillos listos', command=mostrar) #llamamos a la funcion mostrar
boton.place(x=459,y=530) 

root.mainloop()
