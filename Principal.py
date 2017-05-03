# Proyecto #1 de Taller de Programación
# Autor: Alejandro Díaz Pereira. Carné: 2017172898

from tkinter import *
import tkinter.ttk as ttk, json, time

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


barra_energia = ttk.Progressbar(orient="horizontal", mode="determinate", value=data["Energia"], length=480)
barra_energia.place(x=264, y=7)

amount_energia = Label(text=str(data["Energia"]) + " %")
amount_energia.place(x=741, y=8)

# Esta función modifica la energía al ejecutar cierto comando
# Entradas: val (cantidad de energía)
# Salidas: Ninguna
def mod_energia(val):
    global data
    file = open("data.json", "w")
    data["Energia"] += val
    guardar = json.dumps(data)
    file.write(guardar)
    barra_energia.config(value=data["Energia"])
    amount_energia.config(text=str(data["Energia"]) + " %")


cuadricula = Canvas(principal, height=260, width=515, relief="groove")
cuadricula.place(x=264, y=27)

sector2 = cuadricula.create_rectangle(128, 4, 256, 128, width=2)
sector3 = cuadricula.create_rectangle(256, 4, 384, 128, width=2)
sector4 = cuadricula.create_rectangle(384, 4, 512, 128, width=2)
sector5 = cuadricula.create_rectangle(4, 128, 128, 256, width=2)
sector6 = cuadricula.create_rectangle(128, 128, 256, 256, width=2)
sector7 = cuadricula.create_rectangle(256, 128, 384, 256, width=2)
sector8 = cuadricula.create_rectangle(384, 128, 512, 256, width=2)

fondo = PhotoImage(file=data["Fondo"])
triste = PhotoImage(file=data["Triste"])
sonrisa = PhotoImage(file=data["Sonrisa"])
imagen = PhotoImage(file=data["Imagen"])
imagen_bot = cuadricula.create_image(64, 64, image=imagen, tag="bot")

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
#           Todo lo demás son las opciones que llevan todos los botones
# Salidas: Ninguna
def colocar_boton(x, y, lista, index, width, height, image, bd, relief):
    if index == 3:
        lista[index].config(width=width, height=height, image=image, bd=bd, relief=relief)
        lista[index].place(x=x, y=y)
        return colocar_boton(264, y+134, lista, index+1, width, height, image, bd, relief)
    elif index == 7:
        lista[index].config(width=width, height=height, image=image, bd=bd, relief=relief)
        lista[index].place(x=x, y=y)
        return
    else:
        lista[index].config(width=width, height=height, image=image, bd=bd, relief=relief)
        lista[index].place(x=x, y=y)
        return colocar_boton( x+128, y, lista, index+1, width, height, image, bd, relief)
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
def config_sectores(lista, index):
    global sonrisa, triste, fondo, imagen
    if index == 8:
        return
    elif index == 0:
        lista[index].config(image=imagen)
        return config_sectores(lista, index+1)
    else:
        lista[index].config(image=fondo)
        return config_sectores(lista, index+1)
config_sectores(sectores, 0)

# Indica el índice de la posición del bot, este índice se usará para la lista "sectores".
# Entradas: lista (Conjunto de variables de los botones que forman la cuadrícula)
#           index (Se utiliza para seguir la lista)
# Salidas: index
def where_bot(lista, index):
    global imagen
    if lista[index].cget("image") == "pyimage4":
        return index
    else:
        return where_bot(lista, index+1)


# Mueve la imagen del bot (adelante)
# Entradas: Ninguna
# Salidas:. Ninguna
def goahead():
    if cuadricula.coords("bot")[1] == 64:
        cuadricula.move("bot", 0, 128)
    else:
        cuadricula.move("bot", 0, -128)
    mod_energia(-1)

# Mueve la imagen del bot (atrás)
# Entradas: Ninguna
# Salidas:. Ninguna
def goback():
    if cuadricula.coords("bot")[1] == 64:
        cuadricula.move("bot", 0, 128)
    else:
        cuadricula.move("bot", 0, -128)
    mod_energia(-1)

# Mueve la imagen del bot (derecha)
# Entradas: Ninguna
# Salidas:. Ninguna
def right():
    if cuadricula.coords("bot")[0] == 448:
        cuadricula.move("bot", -384, 0)
    else:
        cuadricula.move("bot", 128, 0)
    mod_energia(-1)

# Mueve la imagen del bot (izquierda)
# Entradas: Ninguna
# Salidas:. Ninguna
def left():
    if cuadricula.coords("bot")[0] == 64:
        cuadricula.move("bot", 384, 0)
    else:
        cuadricula.move("bot", -128, 0)
    mod_energia(-1)

# Hace que el bot sonría.
# Entradas: Ninguna
# Salidas:. Ninguna
def smile():
    global imagen
    cuadricula.itemconfigure("bot", image=data["Sonrisa"])
    principal.update()
    time.sleep(1)
    cuadricula.itemconfigure("bot", image=imagen)

# Hace que el bot llore.
# Entradas: Ninguna
# Salidas:. Ninguna
def cry():
    global imagen
    cuadricula.itemconfigure("bot", image=data["Triste"])
    principal.update()
    time.sleep(1)
    cuadricula.itemconfigure("bot", image=imagen)


comandos = {"goahead":goahead, "goback":goback, "right":right, "left":left, "smile":smile, "cry":cry}

# Valida el comando que se le envía al bot
# Entradas: Ninguna
# Salidas:. Ninguna
def ejecucion(ign):
    tmp = choose_comando.get()
    cmd = tmp.split(" ")[1]
    if cmd in comandos:
        comandos[cmd]()

choose_comando.bind("<Return>", ejecucion)
principal.mainloop()