import tkinter

# ventana
window = tkinter.Tk()
window.geometry('{}x{}'.format(180, 180))


def seleccionar():
    seleccion = opcionSeleccionada.get()
    label.config(text=seleccion)

    if seleccion.find('Rojo') != -1:
        label.config(bg='red', fg='white')
    if seleccion.find('Amarillo') != -1:
        label.config(bg='yellow', fg='black')
    if seleccion.find('Verde') != -1:
        label.config(bg='green', fg='white')


def restablecerData(event):
    opcionSeleccionada.set(None)
    label.config(text='')
    label.config(bg=window.cget('bg'), fg='black')


# distribucion
window.columnconfigure(0, weight=6)
window.columnconfigure(1, weight=6)
window.columnconfigure(2, weight=6)
window.columnconfigure(3, weight=6)
window.columnconfigure(4, weight=6)
window.columnconfigure(5, weight=6)
window.columnconfigure(6, weight=6)
# datos
opcionSeleccionada = tkinter.StringVar()
opcionSeleccionada.set(None)

# Radio buttons
radioButton1 = tkinter.Radiobutton(
    window, text='Rojo', value='Valor seleccionado Rojo', variable=opcionSeleccionada, command=seleccionar)
radioButton1.grid(column=3, row=2, sticky=tkinter.N, padx=5, pady=5)
radioButton2 = tkinter.Radiobutton(
    window, text='Amarillo', value='Valor seleccionado Amarillo', variable=opcionSeleccionada, command=seleccionar)
radioButton2.grid(column=3, row=3, sticky=tkinter.N, padx=5, pady=5)
radioButton3 = tkinter.Radiobutton(
    window, text='Verde', value='Valor seleccionado Verde', variable=opcionSeleccionada, command=seleccionar)
radioButton3.grid(column=3, row=4, sticky=tkinter.N, padx=5, pady=5)
# etiqueta valor seleccionado
label = tkinter.Label(window, fg='black')
label.grid(column=3, row=5, sticky=tkinter.N, padx=5, pady=5)
# boton reset
buttonReset = tkinter.Button(window, text='Restablecer')
buttonReset.grid(column=3, row=6, sticky=tkinter.N, padx=5, pady=5)
buttonReset.bind('<Button-1>', restablecerData)

window.mainloop()
