from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import random
import string
import pyperclip
from cryptography.fernet import Fernet
import os


if not os.path.isfile('key.key'):
    key = Fernet.generate_key()
    with open('key.key', 'wb') as kf:
        kf.write(key)
with open('key.key', 'rb') as f:
    key = f.read()


root = Tk()

root.title('Password Generator')
root.config(padx=10, pady=10)


def storeit():
    e = Fernet(key)
    # encrypted= e.encrypt(read)

    line = f'{web_en.get()}|{email_en.get()}|{password_entry.get()}'
    line2 = e.encrypt(bytes(line, 'utf-8'))
    line2 = line2+b'\n'
    with open('savedd.txt', 'ab') as saveit:
        saveit.write(line2)


def pasw():
    password = []
    long = choice_n.get()
    if choice.current() < 0:
        mb.showerror('Wrong', 'You\'ve to select Source and renaming pattern. ')
        return
    for i in range(2):
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        spec = "*&%$!@+#<>?"
        password.append(random.choice(spec))

    if long > 8:
        how = long - 8
        print('how', how)
        for x in range(how):
            password.append(random.choice(string.ascii_lowercase))
    print('lista', password)
    random.shuffle(password)
    made = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, made)


def callbackfunc(n):
    m = n.widget.get()
    choice_n.set(m)
    print('choice_set_get:', choice_n.get())


def copy_entry():
    pyperclip.copy(password_entry.get())


def showpas():
    e = Fernet(key)
    webs = web_en2.get()
    us = email_en2.get()
    with open('savedd.txt', 'rb') as read:
        file = read.readlines()
    for li in file:
        li = li.rstrip(b'\n')
        li = str(e.decrypt(li), 'utf-8')
        dane = li.split('|')
        if len(us) > 0:
            if dane[0] == webs and dane[1] == us:
                showp.delete(0, END)
                showp.insert(0, dane[2])

        else:
            if dane[0] == webs:
                showp.delete(0, END)
                showp.insert(0, dane[2])

# ------------------------ UI -----------------------------


long_t = Label(text='Password Length:')
long_t.grid(column=0, row=0)
choice_n = IntVar()
choice = ttk.Combobox(width=10)
w = [x for x in range(8, 16)]
choice['values'] = w
choice.grid(row=0, column=1, sticky=W)
choice.current()
choice.bind("<<ComboboxSelected>>", callbackfunc)
password_text = Label(text='Password: ')
password_text.grid(row=1, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=1, column=1, sticky=W)
generuj = Button(text='Generate Password', command=pasw)
generuj.grid(row=1, column=2,)
copypass = Button(text='Copy Password', command=copy_entry)
copypass.grid(row=2, column=1)
webt = Label(text="Store your password", font=('Ubuntu', 14, 'bold'))
webt.grid(column=1, row=3, columnspan=2, sticky=W)
web_t = Label(text='Website')
web_t.grid(row=4, column=0)
web_en = Entry(width=20)
web_en.grid(row=4, column=1)
email_t = Label(text='User')
email_t.grid(row=5, column=0)
email_en = Entry(width=20)
email_en.grid(row=5, column=1)
store = Button(text='Store the password', command=storeit)
store.grid(row=6, column=1)
showtext = Label(text='Show Password', font=('Ubuntu', 14, 'bold'))
showtext.grid(row=7, column=1)
web_t2 = Label(text='Website')
web_t2.grid(row=8, column=0)
web_en2 = Entry(width=20)
web_en2.grid(row=8, column=1)
email_t2 = Label(text='User')
email_t2.grid(row=9, column=0)
email_en2 = Entry(width=20)
email_en2.grid(row=9, column=1)
showp = Entry(width=20)
showp.grid(row=10,column=1)
show = Button(text='Show password', command=showpas)
show.grid(row=10, column=2)

root.mainloop()
