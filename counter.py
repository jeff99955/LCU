import tkinter as tk


def increase():
    value['text'] = str(int(value['text']) + 1)
def decrease():
    value['text'] = str(int(value['text']) - 1)

window = tk.Tk()

window.rowconfigure(0, minsize = 50, weight = 1)
window.columnconfigure([0,1,2], minsize = 50, weight = 1)


value = tk.Label(master=window, text = '0')
value.grid(row = 0, column = 1)


btnDecrease = tk.Button(master = window, text = '-', command = decrease)
btnDecrease.grid(row = 0, column = 0, sticky='nsew')

btnIncrease = tk.Button(master=window, text = '+', command = increase)
btnIncrease.grid(row = 0, column = 2, sticky = 'nsew')

window.mainloop()