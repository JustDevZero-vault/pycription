#!/usr/bin/env python
#*.*coding:utf-8*.*

#       encriptador.py written in python2.8
#       version 0.1
#       Copyright 2010 Mephiston <meph.snake@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from random import shuffle
from string import maketrans
import sys
import exceptions

def translator(text,alphabet,key):
    trantab = maketrans(alphabet,key)
    return text.translate(trantab)

def caesar_encode(plaintext,s,alphabet):
    return translator(plaintext,alphabet,alphabet[s:]+alphabet[:s])

def caesar_decode(plaintext,s,alphabet):
    traducido=translator(plaintext,alphabet,alphabet[-s:]+alphabet[:-s])
    base_name="clear_"+((sys.argv[2]))
    print 'Archivo correctamente desencriptado como "%s"' % (base_name)
    archivo=open(base_name,"w")
    archivo.write(traducido)
    archivo.close()

def substitution_encode(plaintext,alphabet):
    randarray=range(0,len(alphabet))
    shuffle(randarray)
    key=""
    for i in range(0,len(alphabet)):
        key+=alphabet[randarray[i]]

    return translator(plaintext,alphabet,key),key



def substitution_decode(plaintext,key,alphabet):
    traducido=translator(plaintext,key,alphabet)
    base_name="clear_"+((sys.argv[2]))
    print 'Archivo correctamente desencriptado como "%s"' % (base_name)
    archivo=open(base_name,"w")
    archivo.write(traducido)
    archivo.close()


def process_substitution(plaintext,alphabet):
    base_name="criptsub_"+((sys.argv[2]))
    base1 = "".join(base_name.split(".")[0])
    clave_name="clave_"+base1+".txt"
    archivo=open(base_name,"w")
    ciphertext,key=substitution_encode(plaintext,alphabet)
    f=open(clave_name,"w")
    f.write(key)
    f.close()
    print base_name
    print "Llave usada para substitución: ", key
    #print "Texto plano:", plaintext
    #print "Texto cifrado:", ciphertext
    archivo.write(ciphertext)
    archivo.close()
    print 'El archivo con el texto encriptado ha sido llamado "%s", y se ha guardado la llave en "%s"\n' % (base_name, clave_name)

def process_cesar(plaintext,alphabet):
    base_name="criptcesar_"+((sys.argv[2]))
    archivo=open(base_name,"w")
    ciphertext=caesar_encode(plaintext,5,alphabet)
    print "Llave usada para cesar: ", 5
    #print "Texto plano:", plaintext
    #print "Texto cifrado:", ciphertext
    archivo.write(ciphertext)
    archivo.close()
    print 'El archivo con el texto encriptado ha sido llamado "%s"\n' % (base_name)
    #print "Decoded  :", caesar_decode(ciphertext,5,alphabet)

def all(plaintext,alphabet):
    print "Se encriptará con todos los metodos."
    substitution_process(plaintext,alphabet)
    process_cesar(plaintext,alphabet)

def help_f():
    print "Uso: encriptador <opciones> <documento> <alfabeto>"
    print "\t   <opciones>:"
    print "\t\t   -c / --crypt=cesar Encriptará el texto usando el Metodo Cesar"
    print "\t\t   -s / --crypt=substitute Encriptará el texto usando el Metodo por Substitución, usando una clave generada aleatoriamente."
    print "\t\t   -a / --crypt=all Encriptará usando los dos metodos"
    print "\t\t   -dc / --decrypt=cesar Desencriptará un texto encriptado por Metodo Cesar"
    print "\t\t   -ds / --decrypt=substitute Desencriptará un texto encriptado por Metodo de Substitución (el archivo debe llamarse: clave_archioadescifrar)"
    print "\t   <documento>: archivo que desea encriptar o desencriptar"
    print "\t   <alfabeto>: archivo que contiene su alfabeto que será susceptible a encriptarse"
    sys.exit(1)

def especification():
    if len(sys.argv) in [2]:
        if str.lower(sys.argv[1]) =="--help":
            help_f()
    if len(sys.argv) not in [4]:
        print "encriptador: opción incorrecta",str.lower(sys.argv[1])
        print "Pruebe `encriptador --help´ para más información."
        sys.exit(1)

    try:
        plaintext = open(sys.argv[2], "r").readlines()
        plaintext= "".join(plaintext)

    except(IOError):
        base_name=((sys.argv[2]))
        print '[-] Error: No se ha encontrado el archivo "%s"\n' % (base_name)
        sys.exit(1)
    try:
        alphabet = open(sys.argv[3], "r").readlines()
        alphabet= "".join(alphabet)
    except(IOError):
        alfa_name=((sys.argv[3]))
        print '[-] Error: No se ha encontrado el archivo alfabeto "%s"\n' % (alfa_name)
        sys.exit(1)
    if ((sys.argv[1]) in ["-ds","--decrypt=substitute"]):
        clave_name="clave_"+((sys.argv[2]))
        try:
            key = open(clave_name, "r").readlines()
            key= "".join(key)
            print "Clave: ",key
            substitution_decode(plaintext,key,alphabet)
        except(IOError):
            print '[-] Error: No se ha encontrado el archivo "%s"\n' % (clave_name)
    elif ((sys.argv[1]) in ["-dc","--decrypt=cesar"]):
        print "Clave: ",5
        caesar_decode(plaintext,5,alphabet)
    elif ((sys.argv[1]) in ["-a", "--crypt=all"]):
        all(plaintext,alphabet)
    elif ((sys.argv[1]) in ["-c", "--crypt=cesar"]):
        process_cesar(plaintext,alphabet)
    elif ((sys.argv[1]) in ["-s", "--crypt=substitute"]):
        process_substitution(plaintext,alphabet)
    elif ((sys.argv[1]) in ["-c", "-s", "-ds","--decrypt=substitute","-dc","--decrypt=cesar","-a","--help","--crypt=substitute",]):
        print "[-] Error: Opción no valida\n"
        sys.exit(1)


def main():
    especification()
if __name__=="__main__":
    main()