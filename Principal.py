# Proyecto #1 de Taller de Programación
# Autor: Alejandro Díaz Pereira. Carné: 2017172898

from tkinter import *
import tkinter.ttk as ttk, json

file_data = open("data.txt")
read_data = file_data.read()
data = json.loads(read_data)

# Crea la ventana principal
principal = Tk()
principal.minsize(width=783, height=450)
principal.title("C.I.P.H.E.R")

comando = StringVar()
choose_comando = Entry(principal, bg="white", width=22, textvariable=comando)
choose_comando.grid(row=3, column=1, sticky="W")

ventana_usuario = Toplevel(principal)
ventana_usuario.title("Nombre de usuario")
ventana_usuario.geometry("400x80")
ventana_usuario.wm_transient(principal)

var_nombre = StringVar()
var_comando = ""

# Pedir nombre de usuario
# Entradas: ign (dtos ignorados)
# Salidas: Ninguna
def nombre_usuario(ign):
    if var_nombre.get() == "":
        global comando, var_comando
        comando.set("Invitado: ")
        var_comando = comando.get()
        ventana_usuario.destroy()
    else:
        comando.set(var_nombre.get() + ": ")
        var_comando = comando.get()
        ventana_usuario.destroy()

# Impide que el prompt sea borrado.
# Entradas: ign, ign2, ign3
# (estas variables existen para que la función se ejecute correctamente, no son usadas en ningún momento).
# Salidas: Ninguna
def prompt(ign, ign2, ign3):
    global var_comando
    if var_comando not in comando.get():
        choose_comando.insert(END, " ")
        choose_comando.icursor(len(var_comando))
comando.trace_variable("w", prompt)

# Impide que el prompt sea borrado.
# Entradas: ign
# (estas variables existen para que la función se ejecute correctamente, no son usadas en ningún momento).
# Salidas: Ninguna
def prompt_2(ign):
    global var_comando
    if choose_comando.index(INSERT) in list(range(0, (len(var_comando)))):
        choose_comando.icursor(len(var_comando)+1)
choose_comando.bind("<KeyPress>", prompt_2)


instruccion1 = Label(ventana_usuario, text="Escriba su nombre")
instruccion2 = Label(ventana_usuario, text="(Déjelo en blanco para usar el nombre predeterminado)")
entrada_usuario = Entry(ventana_usuario, width=45, bg="white", textvariable=var_nombre)
instruccion1.pack()
instruccion2.pack()
entrada_usuario.place(x=18, y=50)

entrada_usuario.bind("<Return>", nombre_usuario)

# Coloca lista de comandos
file_comandos = open("Comandos.txt", "r")
comandos_data = file_comandos.read()
lista_comandos = Label(principal,
                       bd=4,
                       text=comandos_data,
                       height=15,
                       width=25,
                       relief="ridge",
                       font="DejaVu_Sans_Mono",
                       justify=LEFT,
                       anchor="w")
lista_comandos.grid(row=1, column=1)

ins_comandos = Label(text="Escriba un número de comando (1, 2, 3...)")
ins_comandos.grid(row=2, column=1)

exec_comandos = Button(text="Enviar")
exec_comandos.grid(row=3, column=1, sticky="E")

consola = Text(principal, width=73, height=11, bg="white", relief="sunken")
consola.grid(row=2, column=2, rowspan=10)

power = data["Energia"]
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


imagen = PhotoImage(file=data["Imagen"])
imagen_bot = cuadricula.create_image(64, 64, image=imagen, tag="bot")


#comandos = {"hello":,
#            "built":,
#            "status":,
#           "goahead":,
#            "goback":,
#            "right":,
#            "left":,
#            "dance":,
#            "music-on":,
#            "music-off":,
#            "smile":,
#            "cry": }





# Comando para obtener coordenadas del bot
print(cuadricula.coords("bot")[0])


principal.mainloop()