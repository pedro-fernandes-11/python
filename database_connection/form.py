from tkinter import *
from tkinter import messagebox
import pymysql as sql

# form.py is generates a tkinter form, get given data from user and then insert that data into tb_form

connection = sql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='formdb'
)

cursor = connection.cursor()


class Form:
    def __init__(self):
        form_layout = Tk()
        mainframe = Frame(form_layout, pady="25", padx='25', background="#D9D9D9")

        mainframe.pack()

        form_layout.resizable(False, False)
        form_layout.configure(background="#fff", pady="50", padx="50")

        label_name = Label(mainframe, text="Name: ", font="Arial 15", background=mainframe['background'])
        label_name.grid(row=0, column=0, pady="10")
        input_name = Entry(mainframe, font="Arial 15", width="30")
        input_name.grid(row=0, column=1)

        label_email = Label(mainframe, text="Email: ", font="Arial 15", background=mainframe['background'])
        label_email.grid(row=1, column=0, pady="10")
        input_email = Entry(mainframe, font="Arial 15", width="30")
        input_email.grid(row=1, column=1)

        btn_submit = Button(mainframe, text="Submit", width=10, height=2, font="Arial 11", command=lambda: get_data())
        btn_submit.grid(row=2, columnspan=2, pady="20")

        def get_data():
            name = input_name.get().capitalize()
            email = input_email.get().lower()

            if '@' in email and '.com' in email:
                print(f"Name: {name} \nEmail: {email}")

                cursor.execute("INSERT INTO tb_form(name, email) VALUES (%s, %s)", (name, email))
                connection.commit()

                input_name.delete(0, END)
                input_email.delete(0, END)

            else:
                messagebox.showwarning(title='Warning', message="Invalid email")

        form_layout.mainloop()


form = Form()
