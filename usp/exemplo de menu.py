#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Criado em:Sex 27/Mai/2008 hs 22:39
# Autor: MRSantos mrsantos@viaconnect.com.br

from sys import exit
from tkinter import *


def file():
    print('file'.upper())


def new():
    print('new'.upper())


def open():
    print('open'.upper())


def about():
    print("By MRSANTOS")


def tchau():
    print('Tchau...'.upper())
    exit(0)

root = Tk()

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open...", command=open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=tchau)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)

mainloop()
