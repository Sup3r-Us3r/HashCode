#!/usr/bin/env python
#coding: utf-8

'''
HashCodeGUI

'''

######################################### VERIFICADOR DE VERSÃO ################################################

import sys
from platform import python_version

if sys.version_info[0] < 3:
	versao = python_version()
	print("\n\033[32m Você está usando o python na versão\033[1;m \033[1m\033[31m%s\033[1;m \033[32me ela é inferior ao python3 em diante.\033[1;m" %(versao))
	print("\033[32m Por favor rode o HashCodeGUI com a versão superior ao python2.\033[1;m\n")
	exit(1)

################################################################################################################

import os
from tkinter import *
import hashlib
from base64 import b64encode, b64decode
import binascii
import codecs


janela = Tk()
Label(janela, font="Helvetica 13 bold", text="HashCode", width=180, height=2, bg="#161616", fg="green").pack()
janela.title("HashCodeGUI.py for encode of text from hash's GUI")

def Md5():
	mystring = (bloco1.get())
	hash_object = hashlib.md5(mystring.encode())
	janela.geometry("420x550")
	lb["text"] = hash_object.hexdigest()
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA ENCRIPTADA EM MD5 É: " + hash_object.hexdigest())

def Sha1():
	mystring = (bloco1.get())
	hash_object = hashlib.sha1(mystring.encode())
	janela.geometry("420x550")
	lb["text"] = hash_object.hexdigest()
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA ENCRIPTADA EM SHA1 É: " + hash_object.hexdigest())

def Sha224():
	mystring = (bloco1.get())
	hash_object = hashlib.sha224(mystring.encode())
	janela.geometry("463x550")
	lb["text"] = hash_object.hexdigest()
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA ENCRIPTADA EM SHA224 É: " + hash_object.hexdigest())

def Sha256():
	mystring = (bloco1.get())
	hash_object = hashlib.sha256(mystring.encode())
	janela.geometry("520x550")
	lb["text"] = hash_object.hexdigest()
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA ENCRIPTADA EM SHA256 É: " + hash_object.hexdigest())

def Sha384():
	mystring = (bloco1.get())
	hash_object = hashlib.sha384(mystring.encode())
	janela.geometry("770x550")
	lb["text"] = hash_object.hexdigest()
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA ENCRIPTADA EM SHA384 É: " + hash_object.hexdigest())

def Sha512():
	mystring = (bloco1.get())
	hash_object = hashlib.sha512(mystring.encode())
	janela.geometry("1010x550")
	lb["text"] = hash_object.hexdigest()
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA ENCRIPTADA EM 512 É: " + hash_object.hexdigest())

def Base64Encode():
	mystring = (bloco1.get())
	encode = b64encode(mystring.encode('utf-8'))
	janela.geometry("420x550")
	decode = encode.decode('utf-8')
	lb["text"] = decode
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA TRANSFORMADA EM BASE64 É: " + decode)

def Base64Decode():
	mystring = (bloco1.get())
	janela.geometry("420x550")
	decode = b64decode(mystring).decode('utf-8')
	lb["text"] = decode
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA DESTRANSFORMADA EM BASE64 É: " + decode)

def BinarioEncode(encoding='utf-8', errors='surrogatepass'):
	try:	
		mystring = (bloco1.get())
		bits = bin(int(binascii.hexlify(mystring.encode(encoding, errors)), 16))[2:]
		janela.geometry("520x550")
		lb["text"] = bits.zfill(8 * ((len(bits) + 7) // 8))
		resultado = open("resultado.txt", "w")
		resultado.write("SUA SENHA TRANSFORMADA EM BINÁRIO É: " + bits.zfill(8 * ((len(bits) + 7) // 8)))
	except:
		return BinarioEncode

def BinarioDecode(encoding='utf-8', errors='surrogatepass'):
	try:
		binario = (bloco1.get())
		binario = binario.replace(" ", "")
		n = int(binario, 2)
		janela.geometry("520x550")
		lb["text"] = int2bytes(n).decode(encoding, errors)
		resultado = open("resultado.txt", "w")
		resultado.write("SUA SENHA DESTRANSFORMADA EM BINÁRIO É: " + int2bytes(n).decode(encoding, errors))
	except:
		return BinarioDecode

def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def HexadecimalEncode():
	mystring = (bloco1.get())
	janela.geometry("520x550")
	encode = binascii.hexlify(bytes(mystring, "utf-8"))
	encode = str(encode).strip("b")
	encode = encode.strip("'")
	encode = re.sub(r'(..)', r'\1 ', encode).strip()
	lb["text"] = encode
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA TRANSFORMADA EM HEXADECIMAL É: " + encode)

def HexadecimalDecode():
	mystring = (bloco1.get())
	janela.geometry("520x550")
	decode = bytes.fromhex(mystring).decode('utf-8')
	lb["text"] = decode
	resultado = open("resultado.txt", "w")
	resultado.write("SUA SENHA DESTRANSFORMADA EM BINÁRIO É: " + decode)

def TextReverseEncode():
	mystring = (bloco1.get())
	janela.geometry("420x550")
	lb["text"] = mystring[::-1]
	resultado = open("resultado.txt", "w")
	resultado.write("O RESULTADO DO REVERSE É: " + mystring[::-1])

def TextReverseDecode():
	mystring = (bloco1.get())
	janela.geometry("420x550")
	lb["text"] = mystring[::-1]
	resultado = open("resultado.txt", "w")
	resultado.write("O RESULTADO DO REVERSE É: " + mystring[::-1])

def WordsReverseEncode():
	mystring = (bloco1.get())
	janela.geometry("420x550")
	lb["text"] = ' '.join(mystring.split()[::-1])
	resultado = open("resultado.txt", "w")
	resultado.write("O RESULTADO DO REVERSE É: " + ' '.join(mystring.split()[::-1]))

def WordsReverseDecode():
	mystring = (bloco1.get())
	janela.geometry("420x550")
	lb["text"] = ' '.join(mystring.split()[::-1])
	resultado = open("resultado.txt", "w")
	resultado.write("O RESULTADO DO REVERSE É: " + ' '.join(mystring.split()[::-1]))


bloco1 = Entry(janela, bg="#161616", fg="#FFFFFF")
bloco1.place(x=10, y=60, width=400, height=40)

b1 = Button(janela, width=15, text="MD5", bg="#161616", fg="green", command=Md5)
b1.place(x=60, y=140)

b2 = Button(janela, width=15, text="SHA1", bg="#161616", fg="green", command=Sha1)
b2.place(x=215, y=140)

b3 = Button(janela, width=15, text="SHA224", bg="#161616", fg="green", command=Sha224)
b3.place(x=60, y=180)

b4 = Button(janela, width=15, text="SHA256", bg="#161616", fg="green", command=Sha256)
b4.place(x=215, y=180)

b4 = Button(janela, width=15, text="SHA384", bg="#161616", fg="green", command=Sha384)
b4.place(x=60, y=220)

b5 = Button(janela, width=15, text="SHA512", bg="#161616", fg="green", command=Sha512)
b5.place(x=215, y=220)

b6 = Button(janela, width=15, text="BASE64 ENCODE", bg="#161616", fg="green", command=Base64Encode)
b6.place(x=60, y=260)

b7 = Button(janela, width=15, text="BASE64 DECODE", bg="#161616", fg="green", command=Base64Decode)
b7.place(x=215, y=260)

b8 = Button(janela, width=15, text="BINÁRIO ENCODE", bg="#161616", fg="green", command=BinarioEncode)
b8.place(x=60, y=300)

b9 = Button(janela, width=15, text="BINÁRIO DECODE", bg="#161616", fg="green", command=BinarioDecode)
b9.place(x=215, y=300)

b10 = Button(janela, width=15, text="HEXA ENCODE", bg="#161616", fg="green", command=HexadecimalEncode)
b10.place(x=60, y=340)

b11 = Button(janela, width=15, text="HEXA DECODE", bg="#161616", fg="green", command=HexadecimalDecode)
b11.place(x=215, y=340)

b12 = Button(janela, width=15, text="REVERSE TEXT E", bg="#161616", fg="green", command=TextReverseEncode)
b12.place(x=60, y=380)

b13 = Button(janela, width=15, text="REVERSE TEXT D", bg="#161616", fg="green", command=TextReverseDecode)
b13.place(x=215, y=380)

b14 = Button(janela, width=15, text="REVERSE WORDS E", bg="#161616", fg="green", command=WordsReverseEncode)
b14.place(x=60, y=420)

b15 = Button(janela, width=15, text="REVERSE WORDS D", bg="#161616", fg="green", command=WordsReverseDecode)
b15.place(x=215, y=420)

b16 = Button(janela, width=3, text="QUIT", bg="#161616", fg="green", command=janela.quit)
b16.place(x=185, y=460)

lb = Label(janela, font="Helvetica 13 bold", text="⟫ ", fg="#161616")
lb.place(x=10, y=510)


janela.geometry("420x550")
janela.mainloop()
