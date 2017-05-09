# Proyecto #1 de Taller de Programación
# Autor: Alejandro Díaz Pereira. Carné: 2017172898

from tkinter import *
import tkinter.ttk as ttk
import json
import time


file_data = open("data.json")
read_data = file_data.read()
data = json.loads(read_data)

# Crea la ventana principal
principal = Tk()
principal.minsize(width=783, height=450)
principal.title("C.I.P.H.E.R")

entry_comando = StringVar()
choose_comando = Entry(principal, bg="white", width=22, textvariable=entry_comando)
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
        global entry_comando, var_comando
        entry_comando.set("Invitado: ")
        var_comando = entry_comando.get()
        ventana_usuario.destroy()
    else:
        entry_comando.set(var_nombre.get() + ": ")
        var_comando = entry_comando.get()
        ventana_usuario.destroy()


def quit_event():
    print("Works")
    global entry_comando, var_comando, ventana_usuario
    entry_comando.set("Invitado: ")
    var_comando = "Invitado: "
    ventana_usuario.destroy()

ventana_usuario.protocol("WM_DELETE_WINDOW", quit_event)


# Impide que el prompt sea borrado.
# Entradas: ign, ign2, ign3
# (estas variables existen para que la función se ejecute correctamente, no son usadas en ningún momento).
# Salidas: Ninguna


def prompt(ign, ign2, ign3):
    global var_comando
    if var_comando not in entry_comando.get():
        choose_comando.insert(END, " ")
        choose_comando.icursor(len(var_comando))
entry_comando.trace_variable("w", prompt)


# Impide que el prompt sea borrado.
# Entradas: ign
# (esta variable existe para que la función se ejecute correctamente, no es usada en ningún momento).
# Salidas: Ninguna


def prompt_2(ign):
    global var_comando
    if choose_comando.index(INSERT) in list(range(0, (len(var_comando)))):
        choose_comando.icursor(len(var_comando))


choose_comando.bind("<Key>", prompt_2)


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

consola = Text(principal, width=73, height=11, bg="white", relief="sunken", state=DISABLED)
consola.grid(row=2, column=2, rowspan=10)

barra_energia = ttk.Progressbar(orient="horizontal", mode="determinate", value=data["Energia"], length=480)
barra_energia.place(x=264, y=7)

amount_energia = Label(text=str(data["Energia"]) + " %")
amount_energia.place(x=741, y=8)


def history(info):
    consola.config(state=NORMAL)
    localtime = time.localtime(time.time())
    consola.insert(END, '\n')
    consola.insert(END, '\n')
    consola.insert(END, "[")
    consola.insert(END, localtime[1])
    consola.insert(END, "/")
    consola.insert(END, localtime[1])
    consola.insert(END, "/")
    consola.insert(END, localtime[0])
    consola.insert(END, " ")
    consola.insert(END, localtime[3])
    consola.insert(END, ":")
    consola.insert(END, localtime[4])
    consola.insert(END, ":")
    consola.insert(END, localtime[5])
    consola.insert(END, "]")
    consola.insert(END, " ")
    consola.insert(END, info)
    consola.config(state=DISABLED)


def quit_event_main():
    log_file = open("log.txt", "w")
    log_file.write(consola.get(CURRENT, END))
    principal.destroy()

principal.protocol("WM_DELETE_WINDOW", quit_event_main)


# Esta función modifica la energía al ejecutar cierto comando
# Entradas: val (cantidad de energía)
#  Salidas: Ninguna


def mod_energia(val):
    global data, barra_energia, amount_energia
    if data["Energia"] < 20:
        return print("Poca energía")
    file = open("data.json", "w")
    data["Energia"] += val
    guardar = json.dumps(data)
    file.write(guardar)
    barra_energia.config(value=data["Energia"])
    amount_energia.config(text=str(data["Energia"]) + " %")


fondo = PhotoImage(file=data["Fondo"])
triste = PhotoImage(file=data["Triste"])
sonrisa = PhotoImage(file=data["Sonrisa"])
imagen = PhotoImage(file=data["Imagen"])

sector1 = Button(principal)
sector2 = Button(principal)
sector3 = Button(principal)
sector4 = Button(principal)
sector5 = Button(principal)
sector6 = Button(principal)
sector7 = Button(principal)
sector8 = Button(principal)

sectores = [sector1, sector2, sector3, sector4, sector5, sector6, sector7, sector8]


# Se encarga de colocar los botones que conforma la cuadrícula para la imagen del bot
# con sus opciones.
# Entradas: x, y (posiciones iniciales para coocar los botones)
#           lista (variables de cada botón)
#           index (sirve para seguir la lista de variables)
#           Todo lo demás son las opciones que llevan todos los botones.
# Salidas: Ninguna


def colocar_boton(x, y, lista, index, width, height, image, bd, relief):
    if index == 3:
        lista[index].config(width=width, height=height, image=image, bd=bd, relief=relief)
        lista[index].place(x=x, y=y)
        return colocar_boton(264, y + 134, lista, index + 1, width, height, image, bd, relief)
    elif index == 7:
        lista[index].config(width=width, height=height, image=image, bd=bd, relief=relief)
        lista[index].place(x=x, y=y)
        return
    else:
        lista[index].config(width=width, height=height, image=image, bd=bd, relief=relief)
        lista[index].place(x=x, y=y)
        return colocar_boton(x + 128, y, lista, index + 1, width, height, image, bd, relief)


colocar_boton(264,
              26,
              sectores,
              0,
              128,
              128,
              imagen,
              2,
              "ridge")


# Configuración inicial de los botones de la cuadícula
# Entradas: lista (Los botones a configurar)
#           index (Se usa para seguir la lista de botones)
# Salidas: Ninguna


def init_sectores(lista, index):
    global fondo, imagen
    if index == 8:
        return
    elif index == 0:
        lista[index].config(image=imagen)
        return init_sectores(lista, index + 1)
    else:
        lista[index].config(image=fondo)
        return init_sectores(lista, index + 1)


init_sectores(sectores, 0)


def config_sectores(lista, index, place_bot):
    global fondo, imagen
    if index == 8:
        return
    elif index == place_bot:
        lista[index].config(image=imagen)
        return config_sectores(lista, index + 1, place_bot)
    else:
        lista[index].config(image=fondo)
        return config_sectores(lista, index + 1, place_bot)


# Indica el índice de la posición del bot, este índice se usará para la lista "sectores".
# Entradas: lista (Conjunto de variables de los botones que forman la cuadrícula)
#           index (Se utiliza para seguir la lista)
# Salidas: index


def where_bot(lista, index):
    global imagen
    if lista[index].cget("image") in ["pyimage4", "pyimage2", "pyimage3"]:
        return index
    else:
        return where_bot(lista, index + 1)


# Mueve la imagen del bot (adelante)
# Entradas: Ninguna
# Salidas:. Ninguna


def goahead():
    global sectores
    bot = where_bot(sectores, 0)
    if bot in [4, 5, 6, 7]:
        return config_sectores(sectores, 0, bot - 4), mod_energia(-1)


# Mueve la imagen del bot (atrás)
# Entradas: Ninguna
# Salidas:. Ninguna


def goback():
    global sectores
    bot = where_bot(sectores, 0)
    if bot in [0, 1, 2, 3]:
        return config_sectores(sectores, 0, bot + 4), mod_energia(-1)


# Mueve la imagen del bot (derecha)
# Entradas: Ninguna
# Salidas:. Ninguna


def right():
    global sectores
    bot = where_bot(sectores, 0)
    if bot not in [3, 7]:
        return config_sectores(sectores, 0, bot + 1), mod_energia(-1)


# Mueve la imagen del bot (izquierda)
# Entradas: Ninguna
# Salidas:. Ninguna


def left():
    global sectores
    bot = where_bot(sectores, 0)
    if bot not in [0, 4]:
        return config_sectores(sectores, 0, bot - 1), mod_energia(-1)


# Hace que el bot sonría.
# Entradas: Ninguna
# Salidas:. Ninguna


def smile():
    global sectores, sonrisa, imagen
    bot = where_bot(sectores, 0)
    sectores[bot].config(image=sonrisa)
    principal.update()
    time.sleep(1)
    sectores[bot].config(image=imagen)


# Hace que el bot llore.
# Entradas: Ninguna
# Salidas:. Ninguna


def cry():
    global sectores, triste, imagen
    bot = where_bot(sectores, 0)
    sectores[bot].config(image=triste)
    principal.update()
    time.sleep(1)
    sectores[bot].config(image=imagen)


def power(cant):
    return mod_energia(cant)


def hello():
    history("Hola, mi nombre es C.I.P.H.E.R, soy un Programa Emulador de Robots Con Interacción Humana.")
    file = "/home/alejo/Sonido.wav"


# Valida el comando que se le envía al bot
# Entradas: ign (variable para almacenar datos innecesarios)
# Salidas:. Ninguna


def ejec(ign):
    comandos = {"goahead": goahead,
                "goback": goback,
                "right": right,
                "left": left,
                "smile": smile,
                "cry": cry,
                "history": history,
                "hello": hello}
    tmp = choose_comando.get()
    cmd = tmp.split(" ")[1]
    if cmd in comandos:
        comandos[cmd]()


choose_comando.bind("<Return>", ejec)

exec_comandos = Button(text="Enviar")
exec_comandos.grid(row=3, column=1, sticky="E")
principal.mainloop()

