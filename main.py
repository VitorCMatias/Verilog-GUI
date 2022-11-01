# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.geometry('900x500')
#
# img_frame = Frame(root, background="blue")
# image = ImageTk.PhotoImage(Image.open("img.jpg"))
# img = Label(img_frame, image = image)
# img.place(relx=0.5, rely=0.5, anchor=CENTER)
# img_frame.pack(expand=True, fill=BOTH, side=LEFT)
#
# subframe2 = Frame(root, background="red")
# message = Label(subframe2, text="Message")
# codigo = Entry(message, width=40)
# codigo.grid()
# message.place(relx=0.5, rely=0.5, anchor=CENTER)
# subframe2.pack(expand=True, fill=BOTH, side=LEFT)
#
# root.mainloop()

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image




window = Tk()
window.title("Gerador de Código")

window.geometry("730x450")
window.configure(bg = "#FFFFFF")


nome_do_projeto = StringVar()
prefixo = StringVar()

def get_prefixo():
    print(prefixo.get())


def get_nome_do_projeto():
    print(nome_do_projeto.get())



img_frame = LabelFrame(window, width=380, height=400, text="Cyclone IV")
#img_frame.grid(row=0, column=0, padx=10, pady=5)

subframe2 = LabelFrame(window, width=350, height=400, background="white", text="Configurações do Sistema")
subframe3 = Frame(window, width=350, height=50)
subframe3.pack(fill=X, side=BOTTOM)
#subframe2.grid(row=0, column=1, padx=10, pady=5)

padding_x=30
ipad_x=15

Button(subframe3, text="Salvar Configuração").grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
Button(subframe3, text="Carregar Configuração").grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
Button(subframe3, text="Gerar", command = get_nome_do_projeto).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
Button(subframe3, text="Sair", command = get_prefixo).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)




# canvas.place(x = 0, y = 0)
# img_frame =canvas.create_rectangle(
#     8.0,
#     20.0,
#     395.0,
#     361.0,
#     fill="#01f0a0",
#     outline="")

#img_frame = Frame(window, background="blue")
image = ImageTk.PhotoImage(Image.open("assets/img.png"))
img = Label(img_frame, image = image)
img.place(relx=0.5, rely=0.5, anchor=CENTER)
img_frame.pack(fill=X, side=LEFT)









subframe2.pack(fill=X, side=LEFT)
#subframe2 = Frame(window, background="red")
#label_widget = Label(subframe2, text="A Label")
#label_widget.pack()
message = Label(subframe2, text="Nome do Projeto:", fg='#f1a').place(anchor ='nw')

codigo = Entry(subframe2, width=40, textvariable = nome_do_projeto).place(rely=0.06, anchor ='nw')


#c1 = Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)

Checkbutton(subframe2, text='CLOCK', onvalue=True, offvalue=False).place(relx=0.05, rely=0.2)
Checkbutton(subframe2, text='LED X 10', onvalue=True, offvalue=False).place(relx=0.05, rely=0.3)
Checkbutton(subframe2, text='Botão x 2', onvalue=True, offvalue=False).place(relx=0.05, rely=0.4)
Checkbutton(subframe2, text='VGA', onvalue=True, offvalue=False).place(relx=0.05, rely=0.5)
Checkbutton(subframe2, text='Arduino Header', onvalue=True, offvalue=False).place(relx=0.05, rely=0.6)


Checkbutton(subframe2, text='7-Segmentos X 6', onvalue=True, offvalue=False).place(relx=0.6, rely=0.2)
Checkbutton(subframe2, text='Switch X 10', onvalue=True, offvalue=False).place(relx=0.6, rely=0.3)
Checkbutton(subframe2, text='Acelerometro', onvalue=True, offvalue=False).place(relx=0.6, rely=0.4)
Checkbutton(subframe2, text='SDRAM, 64 MB', onvalue=True, offvalue=False).place(relx=0.6, rely=0.5)

Label(subframe2, text="Cabeçalho 2x20 GPIO", fg='#f1a').place(anchor ='sw',rely=0.8)
#w = Listbox (subframe2, option, ... )


Label(subframe2, text="Prefixo:", fg='#f1a').place(anchor ='sw',rely=0.95)

Entry(subframe2, width=20, textvariable = prefixo).place(anchor ='sw',rely=0.95,relx=0.15)


# Lb1 = ttk.Combobox(subframe2)
# Lb1['values'] = ['Nenhum', 'GPIO Default', '']
# Lb1.place(anchor ='sw',rely=0.87)


window.resizable(False, False)
window.mainloop()
