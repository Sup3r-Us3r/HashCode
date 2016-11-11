#!/usr/bin/env python3.5
#coding: utf-8

import hashlib
import base64
from time import sleep
import os

Sair = "reset && exit"
Limpar = "reset"

def Apresentacao():
	os.system(Limpar)
	print('''\033[31m

 ▄  █ ██      ▄▄▄▄▄    ▄  █     ▄█▄    ████▄ ██▄   ▄███▄   
█   █ █ █    █     ▀▄ █   █     █▀ ▀▄  █   █ █  █  █▀   ▀  
██▀▀█ █▄▄█ ▄  ▀▀▀▀▄   ██▀▀█     █   ▀  █   █ █   █ ██▄▄    
█   █ █  █  ▀▄▄▄▄▀    █   █     █▄  ▄▀ ▀████ █  █  █▄   ▄▀ 
   █     █               █      ▀███▀        ███▀  ▀███▀   
  ▀     █               ▀                                  
       ▀                                                  \033[1;m

''')


def Escolha():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar.

\033[31m1\033[1;m) Encode - MD5
\033[31m2\033[1;m) Encode - Sha1
\033[31m3\033[1;m) Encode - Sha224
\033[31m4\033[1;m) Encode - Sha256
\033[31m5\033[1;m) Encode - Sha384
\033[31m6\033[1;m) Encode - Sha512
\033[31m7\033[1;m) Encode - Base64

\033[31mq\033[1;m) Sair
""")
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		Md5()
	elif opcao1 == "2":
		Sha1()
	elif opcao1 == "3":
		Sha224()
	elif opcao1 == "4":
		Sha256()
	elif opcao1 == "5":
		Sha384()
	elif opcao1 == "6":
		Sha512()
	elif opcao1 == "7":
		Base64()
	elif opcao1 == "q":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Md5():
		Apresentacao()
		mystring = input('\033[32mColoque o texto que queira encriptar em MD5\033[1;m: ')
		hash_object = hashlib.md5(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Sha1():
		Apresentacao()
		mystring = input('\033[32mColoque o texto que queira encriptar em Sha1\033[1;m: ')
		hash_object = hashlib.sha1(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Sha224():
		Apresentacao()
		mystring = input('\033[32mColoque o texto que queira encriptar em Sha224\033[1;m: ')
		hash_object = hashlib.sha224(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Sha256():
		Apresentacao()
		mystring = input('\033[32mColoque o texto que queira encriptar em Sha256\033[1;m: ')
		hash_object = hashlib.sha256(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Sha384():
		Apresentacao()
		mystring = input('\033[32mColoque o texto que queira encriptar em Sha384\033[1;m: ')
		hash_object = hashlib.sha384(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Sha512():
		Apresentacao()
		mystring = input('\033[32mColoque o texto que queira encriptar em Sha512\033[1;m: ')
		hash_object = hashlib.sha512(mystring.encode())
		print("")
		print(hash_object.hexdigest())
		print("")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Escolha()

def Base64():
	Apresentacao()
	digite = str(input("\033[32mColoque o texto que queira encriptar em base64\033[1;m: ")) 
	print("")
	codificar = base64.b64encode(digite.encode('utf-8', 'replace')) 
	decodificar = base64.b64decode(codificar) 
	print(codificar, " = ", decodificar)
	print("") 
	input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
	Escolha()

def ComandoNaoEncontrado():
	print("""
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado.
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor.

""")

Escolha()