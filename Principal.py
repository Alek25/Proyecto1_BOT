# Proyecto #1 de Taller de Programación
# Autor: Alejandro Díaz Pereira. Carné: 2017172898

from tkinter import *
import tkinter.ttk as ttk, json

# Crea la ventana principal
principal = Tk()
principal.minsize(width=783, height=450)
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

# Impide que el prompt sea borrado.
# Entradas: ign, ign2, ign3
# (estas variables existen para que la función se ejecute correctamente, no son usadas en ningún momento).
# Salidas: Ninguna
def prompt(ign, ing2, ing3):
    var = comando.get()
    if ">>> " not in var:
        choose_comando.insert(3, " ")
        choose_comando.icursor(4)
comando.trace_variable("w", prompt)


exec_comandos = Button(text="Ejecutar")
exec_comandos.grid(row=3, column=1, sticky="E")

consola = Text(principal, width=73, height=11, bg="white", relief="sunken")
consola.grid(row=2, column=2, rowspan=10)


file_energia = open("data.txt")
energia = file_energia.read()

power = json.loads(energia)["Energia"]
barra_energia = ttk.Progressbar(orient="horizontal", mode="determinate", value=power, length=480)
barra_energia.place(x=264, y=7)

amount_energia = Label(text=str(power) + " %")
amount_energia.place(x=741, y=8)

cuadricula = Canvas(principal, height=260, width=515, relief="groove")
cuadricula.place(x=264, y=27)

sector1 = cuadricula.create_rectangle(4, 4, 128, 128, width=2)
sector2 = cuadricula.create_rectangle(128, 4, 256, 128, width=2)
sector3 = cuadricula.create_rectangle(256, 4, 384, 128, width=2)
sector4 = cuadricula.create_rectangle(384, 4, 512, 128, width=2)
sector5 = cuadricula.create_rectangle(4, 128, 128, 256, width=2)
sector6 = cuadricula.create_rectangle(128, 128, 256, 256, width=2)
sector7 = cuadricula.create_rectangle(256, 128, 384, 256, width=2)
sector8 = cuadricula.create_rectangle(384, 128, 512, 256, width=2)

principal.mainloop()