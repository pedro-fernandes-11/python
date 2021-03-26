from tkinter import *

teste = Tk()
teste.title('Teste em TKINTER')

teste.iconbitmap("images/icon.ico")

screen_height = teste.winfo_screenheight()
screen_width = teste.winfo_screenwidth()

teste_height = 300
teste_width = 500
teste_posx = screen_width / 2 - teste_width / 2
teste_posy = screen_height / 2 - teste_height / 2


teste.geometry(f"{teste_width}x{teste_height}+{int(teste_posx)}+{int(teste_posy)}")

# teste.resizable(False, False)

# teste.state("iconic")


def btn_executed(msg):
    print(msg)


label_1 = Label(teste,
                text="What's your name?",
                bg="#aabbee",
                fg="black",
                font="Arial 10",
                height="1",
                width=50,
                pady="10",
                padx="10")

text = StringVar()
text.set("What's your name?")
label_2 = Label(teste,
                textvariable=text,
                bg="#aadddd",
                font="Arial 10",
                width=50,
                padx="10",
                pady="10")

input_1 = Entry(teste)
btn = Button(teste, text="Execute", command=lambda: btn_executed('New message'))

# Pack
label_1.grid(row=0, columnspan=2)
label_2.grid(row=1, columnspan=2)
input_1.grid(row=2, column=0)
btn.grid(row=2, column=1)

print(label_1.winfo_width())
teste.mainloop()
