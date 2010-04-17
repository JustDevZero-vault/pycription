#!/usr/bin/env python
#*.*coding:utf-8*.*

#       pycription.py written in python2.8
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
    translated=translator(plaintext,alphabet,alphabet[-s:]+alphabet[:-s])
    base_name="clear_"+((sys.argv[2]))
    print 'File correctly decrypted as "%s"' % (base_name)
    filename=open(base_name,"w")
    filename.write(translated)
    filename.close()

def substitution_encode(plaintext,alphabet):
    randarray=range(0,len(alphabet))
    shuffle(randarray)
    key=""
    for i in range(0,len(alphabet)):
        key+=alphabet[randarray[i]]

    return translator(plaintext,alphabet,key),key



def substitution_decode(plaintext,key,alphabet):
    translated=translator(plaintext,key,alphabet)
    base_name="clear_"+((sys.argv[2]))
    print 'File correctly decrypted as "%s"' % (base_name)
    filename=open(base_name,"w")
    filename.write(translated)
    filename.close()


def process_substitution(plaintext,alphabet):
    base_name="criptsub_"+((sys.argv[2]))
    base1 = "".join(base_name.split(".")[0])
    key_name="key_"+base1+".txt"
    filename=open(base_name,"w")
    ciphertext,key=substitution_encode(plaintext,alphabet)
    f=open(key_name,"w")
    f.write(key)
    f.close()
    print base_name
    print "Key used for substitution: ", key
    #print "Texto plano:", plaintext
    #print "Texto cifrado:", ciphertext
    filename.write(ciphertext)
    filename.close()
    print 'File correctly encrypted as "%s", the key was saved as "%s"\n' % (base_name, key_name)

def process_cesar(plaintext,alphabet):
    base_name="criptcesar_"+((sys.argv[2]))
    filename=open(base_name,"w")
    ciphertext=caesar_encode(plaintext,5,alphabet)
    print "The key used for crypt was: ", 5
    #print "Texto plano:", plaintext
    #print "Texto cifrado:", ciphertext
    filename.write(ciphertext)
    filename.close()
    print 'File correctly encrypted as  "%s"\n' % (base_name)
    #print "Decoded  :", caesar_decode(ciphertext,5,alphabet)

def all(plaintext,alphabet):
    print "The file is going to be crypted with all methods."
    substitution_process(plaintext,alphabet)
    process_cesar(plaintext,alphabet)

def help_f():
    print "Usage: pycription.py <options> <document> <alphabet>"
    print "\t   <options>:"
    print "\t\t   -c / --crypt=cesar This will crypt the text using CESAR."
    print "\t\t   -s / --crypt=substitute This will crypt the text using RANDOM KEY SUBSTITUTION."
    print "\t\t   -a / --crypt=all This will crypt with all methots"
    print "\t\t   -dc / --decrypt=cesar This will decrypt a CESAR text"
    print "\t\t   -ds / --decrypt=substitute This will descrypt a RANDOM KEY SUBSTITUTION text, the key file, mast be started with key_"
    print "\t   <document>: the file that you want to crypt or decrypt"
    print "\t   <alphabet>: the file that contains the characters that are susceptible to being replaced"
    sys.exit(1)

def especification():
    if len(sys.argv) in [2]:
        if str.lower(sys.argv[1]) =="--help":
            help_f()
    if len(sys.argv) not in [4]:
        print "pycription.py: incorrect option",str.lower(sys.argv[1])
        print "Try `pycription.py --help´ for more information."
        sys.exit(1)

    try:
        plaintext = open(sys.argv[2], "r").readlines()
        plaintext= "".join(plaintext)

    except(IOError):
        base_name=((sys.argv[2]))
        print '[-] Error: The file "%s" was not found.\n' % (base_name)
        sys.exit(1)
    try:
        alphabet = open(sys.argv[3], "r").readlines()
        alphabet= "".join(alphabet)
    except(IOError):
        alfa_name=((sys.argv[3]))
        print '[-] Error: The alphabet "%s" was not found\n' % (alfa_name)
        sys.exit(1)
    if ((sys.argv[1]) in ["-ds","--decrypt=substitute"]):
        key_name="key_"+((sys.argv[2]))
        try:
            key = open(key_name, "r").readlines()
            key= "".join(key)
            print "Key: ",key
            substitution_decode(plaintext,key,alphabet)
        except(IOError):
            print '[-] Error: The key file "%s" was not found.\n' % (key_name)
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
        print "[-] Error: Invalid option\n"
        sys.exit(1)


def main():
    especification()
if __name__=="__main__":
    main()