# Proyecto #1 de Taller de Programación
# Autor: Alejandro Díaz Pereira. Carné: 2017172898

from tkinter import *
import tkinter.ttk as ttk

# Crea la ventana principal
principal = Tk()
principal.minsize(width=900, height=450)
principal.title("C.I.P.H.E.R")

# Coloca lista de comandos
file_comandos = open("Comandos.txt", "r")
comandos = file_comandos.read()
lista_comandos = Label(principal,
                       bd=4,
                       text=comandos,
                       height=15,
                       width=25,
                       relief="ridge",
                       font="DejaVu_Sans_Mono",
                       justify=LEFT,
                       anchor="w")
lista_comandos.grid(row=1, column=1)

L_comandos = Label(text="Escriba un número de comando (1, 2, 3...)")
L_comandos.grid(row=2, column=1)

comando = StringVar()

choose_comando = Entry(principal, bg="white", width=20, textvariable=comando)
choose_comando.insert(0, ">>> ")
choose_comando.grid(row=3, column=1, sticky="W")

# Impide que el prompt sea borrado. Entradas: ign, ign2, ign3 (datos innecesarios e ignorados). Salidas: Ninguna
def prompt(ign, ing2, ing3):
    var = comando.get()
    if ">>> " not in var:
        choose_comando.insert(3, " ")
        choose_comando.icursor(4)
comando.trace_variable("w", prompt)


exec_comandos = Button(text="Ejecutar")
exec_comandos.grid(row=3, column=1, sticky="E")

consola = Text(principal, width=90, height=11, bg="white", relief="sunken")
consola.grid(row=2, column=2, rowspan=10)

power = 90
barra_energia = ttk.Progressbar(orient="horizontal", mode="determinate", value=power, length=590)
barra_energia.place(x=264, y=7)

amount_energia = Label(text=str(power) + " %")
amount_energia.place(x=860, y=8)


b01 = Button(principal, height=3, width=3, relief="groove", bd=5)
b01.grid(row=1, column=2)


principal.mainloop()