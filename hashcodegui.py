#!/usr/bin/env python3.5
#coding: utf-8

'''
HashCodeGUI
'''

import os
from tkinter import *
import hashlib


janela = Tk()
Label(janela, text="HashCode", width=180, height=2, bg="#161616", fg="green").pack()


def Md5():
		mystring = (bloco1.get())
		hash_object = hashlib.md5(mystring.encode())
		janela.geometry("420x350")
		lb["text"] = hash_object.hexdigest()
		resultado = open("hash.txt", "w")
		resultado.write("Sua senha encriptada em MD5 é: " + hash_object.hexdigest())

def Sha1():
		mystring = (bloco1.get())
		hash_object = hashlib.sha1(mystring.encode())
		janela.geometry("420x350")
		lb["text"] = hash_object.hexdigest()
		resultado = open("hash.txt", "w")
		resultado.write("Sua senha encriptada em Sha1 é: " + hash_object.hexdigest())

def Sha224():
		mystring = (bloco1.get())
		hash_object = hashlib.sha224(mystring.encode())
		janela.geometry("463x350")
		lb["text"] = hash_object.hexdigest()
		resultado = open("hash.txt", "w")
		resultado.write("Sua senha encriptada em Sha224 é: " + hash_object.hexdigest())

def Sha256():
		mystring = (bloco1.get())
		hash_object = hashlib.sha256(mystring.encode())
		janela.geometry("520x350")
		lb["text"] = hash_object.hexdigest()
		resultado = open("hash.txt", "w")
		resultado.write("Sua senha encriptada em Sha256 é: " + hash_object.hexdigest())

def Sha384():
		mystring = (bloco1.get())
		hash_object = hashlib.sha384(mystring.encode())
		janela.geometry("770x350")
		lb["text"] = hash_object.hexdigest()
		resultado = open("hash.txt", "w")
		resultado.write("Sua senha encriptada em 384 é: " + hash_object.hexdigest())

def Sha512():
		mystring = (bloco1.get())
		hash_object = hashlib.sha512(mystring.encode())
		janela.geometry("1003x350")
		lb["text"] = hash_object.hexdigest()
		resultado = open("hash.txt", "w")
		resultado.write("Sua senha encriptada em Sha512 é: " + hash_object.hexdigest())

bloco1 = Entry(janela, bg="#161616", fg="#FFFFFF")
bloco1.place(x=10, y=60, width=400, height=40)

b1 = Button(janela, width=15, text="MD5", bg="#FF0000", fg="#161616", command=Md5)
b1.place(x=60, y=140)

b2 = Button(janela, width=15, text="Sha1", bg="#FF0000", fg="#161616", command=Sha1)
b2.place(x=215, y=140)

b3 = Button(janela, width=15, text="Sha224", bg="#FF0000", fg="#161616", command=Sha224)
b3.place(x=60, y=180)

b4 = Button(janela, width=15, text="Sha256", bg="#FF0000", fg="#161616", command=Sha256)
b4.place(x=215, y=180)

b4 = Button(janela, width=15, text="Sha384", bg="#FF0000", fg="#161616", command=Sha384)
b4.place(x=60, y=220)

b5 = Button(janela, width=15, text="Sha512", bg="#FF0000", fg="#161616", command=Sha512)
b5.place(x=215, y=220)

b6 = Button(janela, width=3, text="Quit", bg="#FF0000", fg="#161616", command=janela.quit)
b6.place(x=185, y=260)

lb = Label(janela, text="Encode: ", fg="green", bg="#161616")
lb.place(x= 10, y=300)


janela.geometry("420x350")
janela.mainloop()
