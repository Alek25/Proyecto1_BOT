# Proyecto #1 de Taller de Programación
# Autor: Alejandro Díaz Pereira. Carné: 2017172898

from tkinter import *
import tkinter.ttk as ttk

# Crea la ventana principal
principal = Tk()

principal.minsize(width=900, height=450)
principal.title("C.I.P.H.E.R")

# Coloca lista de comandos
comandos = open("Comandos.txt", "r").read()

lista_comandos = Label(principal,
                       text=comandos,
                       height=15,
                       width=25,
                       relief="ridge",
                       font="DejaVu_Sans_Mono",
                       justify=LEFT,
                       anchor="w")
lista_comandos.grid(row=1, column=1)

# Crea campo para escribir número de comando
L_comandos = Label(text="Escriba un número de comando (1, 2, 3...)")
L_comandos.grid(row=2,column=1)

choose_comandos = Entry(principal, bg="white", width=20)
choose_comandos.insert(0, ">>> ")
choose_comandos.grid(row=3, column=1, sticky="W")

# Detecta activación de la tecla Enter, entradas: event(tecla presionada), salidas: ninguna
def detect_enter(event):
    choose_comandos.delete(0, END)
    choose_comandos.insert(0, ">>> ")

exec_comandos = Button(text="Ejecutar", command=detect_enter)
exec_comandos.grid(row=3, column=1, sticky="E")


choose_comandos.bind("<Return>", detect_enter)

consola = Text(principal, width=90, height=11, bg="white", relief="sunken")
consola.grid(row=2, column=2, rowspan=10)

power = 90
barra_energia = ttk.Progressbar(orient="horizontal", mode="determinate", value=power, length=590)
barra_energia.place(x=264, y=7)

amount_energia = Label(text=str(power) + " %")
amount_energia.place(x=860, y=8)











principal.mainloop()