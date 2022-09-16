from tkinter import *
from tkinter import Tk
from tkinter import ttk
import pyperclip
from cryptography.fernet import Fernet
import os
import webbrowser
import random
import string

backg = '#06090f'


 #------------key generator --------------- #
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
    if len(password_entry.get()) < 1 or len(web_en.get()) < 1:
        mb.showerror("Something's missing", "You need to have generated Password and provide the Website or Program pasword is for.")
        return
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
        mb.showerror("Something's missing", "You've to select the length of the password. ")
        return
    for i in range(2):
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

    if long > 8:
        how = long - 8
        #print('how', how)
        for x in range(how):
            password.append(random.choice(string.ascii_lowercase))
    #print('lista', password)
    random.shuffle(password)
    made = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, made)


def callbackfunc(n):
    m = n.widget.get()
    choice_n.set(m)
   # print('choice_set_get:', choice_n.get())


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

def me():
    def callback(url):
        webbrowser.open_new(url)


    new=Toplevel(root)
    new.title('About Vimart')
    new.geometry('700x500')
    new.config(bg='#06090f', padx=70, pady=50,)
    new.resizable(0,0)
    napis=Label(new,text='Vimart',bg=backg, fg='white', font=('Ubuntu', 50, 'bold' )).grid(column=0, row=0)
    napis2 = Label(new, text='Password Manager & Generator', bg=backg, fg='white', font=('Ubuntu', 30, 'bold')).grid(column=0, row=1)
    napi3 = Label(new, text='1.0', bg=backg, fg='white', font=('Ubuntu', 20, 'bold')).grid(column=0, row=2)
    napi4 = Label(new, text='An open source tool to help Manage and Create secure Passwords for personal use.\n For commercial use contact: aceviu@gmail.com ', bg=backg, fg='white', font=('Ubuntu', 10)).grid(column=0, row=3)
    link1 = Label(new, text="\nWebsite", fg="red", bg=backg, cursor="hand2")
    link1.grid(column=0,row=4)
    link1.bind("<Button-1>", lambda e: callback("http://www.viteac.blogspot.com"))
    napi5 = Label(new, text='\n Copyright © 2021 Marcin Witkowski  ', bg=backg, fg='white', font=('Ubuntu', 12)).grid(column=0, row=5)

# ------------------------ UI -----------------------------

canvas = Canvas(root, width=40, height=40).grid(column=0,row=0,columnspan=1)
bgs=Button(canvas,text="Vimart 1.0\n Password Manager & Generator",
          background = '#0f2a52', foreground ="orange",
          font = ("Times New Roman", 15, 'bold'),command=me).grid(column=0,row=0, pady=10, padx=20, columnspan=2, sticky=W )
long_t = Label(text='Password Length:')
long_t.grid(column=0, row=1)
choice_n = IntVar()
choice = ttk.Combobox(width=10)
w = [x for x in range(8, 16)]
choice['values'] = w
choice.grid(row=1, column=1, sticky=W)
choice.current()
choice.bind("<<ComboboxSelected>>", callbackfunc)
password_text = Label(text='Password: ')
password_text.grid(row=2, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=2, column=1, sticky=W)
generuj = Button(text='Generate Password', command=pasw)
generuj.grid(row=3, column=1,sticky=W)
copypass = Button(text='Copy', command=copy_entry)
copypass.grid(row=2, column=2, sticky=W)
webt = Label(text="Store your password", font=('Ubuntu', 14, 'bold'))
webt.grid(column=1, row=4, columnspan=2, sticky=W)
web_t = Label(text='Website')
web_t.grid(row=5, column=0)
web_en = Entry(width=20)
web_en.grid(row=5, column=1, sticky=W)
email_t = Label(text='User')
email_t.grid(row=6, column=0)
email_en = Entry(width=20)
email_en.grid(row=6, column=1,sticky=W)
store = Button(text='Store the password', command=storeit)
store.grid(row=7, column=1)
showtext = Label(text='Show Password', font=('Ubuntu', 14, 'bold'))
showtext.grid(row=8, column=1)
web_t2 = Label(text='Website')
web_t2.grid(row=9, column=0)
web_en2 = Entry(width=20)
web_en2.grid(row=9, column=1, sticky=W)
email_t2 = Label(text='User')
email_t2.grid(row=10, column=0)
email_en2 = Entry(width=20)
email_en2.grid(row=10, column=1, sticky=W)
showp = Entry(width=20)
showp.grid(row=12,column=1, sticky=W)
show = Button(text='Show password', command=showpas)
show.grid(row=11, column=1)

root.mainloop()
