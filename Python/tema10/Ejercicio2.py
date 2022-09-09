import tkinter
from tkinter import ttk


def crearCheckList():
    for chkVar, chkText in zip(checkList, dataList):
        index = dataList.index(chkText)
        chk = ttk.Checkbutton(
            window, text=chkText, variable=chkVar, command=seleccionar)
        chk.grid(column=3, row=index+2, sticky=tkinter.N, padx=5, pady=5)


def seleccionar():
    valores = ''
    for index, valor in enumerate(checkList):
        if valor.get() == '1':
            valores += dataList[index]+'\n'

    etiquetaValor.config(text=valores)


# ventana
window = tkinter.Tk()
window.title("Lista")
window.geometry('{}x{}'.format(200, 250))

# distribucion
window.columnconfigure(0, weight=6)
window.columnconfigure(1, weight=6)
window.columnconfigure(2, weight=6)
window.columnconfigure(3, weight=6)
window.columnconfigure(4, weight=6)
window.columnconfigure(5, weight=6)
window.columnconfigure(6, weight=6)
# datos
checkList = [tkinter.StringVar(), tkinter.StringVar(),
             tkinter.StringVar(), tkinter.StringVar()]
dataList = ['Audi', 'BMW', 'Renault', 'Seat']

# etiqueta valor seleccionado
titulo = tkinter.Label(window, text='Marca Automovil', fg='black')
titulo.grid(column=3, row=1, sticky=tkinter.N, padx=5, pady=5)
etiquetaValor = tkinter.Label(window, text='', fg='black')
etiquetaValor.grid(column=3, row=6, sticky=tkinter.N, padx=5, pady=5)

# Checklist
crearCheckList()

window.mainloop()
