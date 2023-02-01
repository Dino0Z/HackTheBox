from PIL import Image
from zipfile import ZipFile
import os
import shutil

bild = Image.open("flag/pwd.png", "r")
#bild = Image.open("pwd.png", "r")

MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-' }


def runner():
    bild = Image.open("flag/pwd.png", "r")
    pixel = bild.load()
    width, height = bild.size
	
	#print(pixel[5, 1])
	
    password = ""
    text = ""
    morse = 0
    n = pixel[0,0]
    print(f"\nStorlek: {width} x {height} pixlar. Första pixeln är: {str(n)} med tredje värde {str(n[2])}")
    #print("Första pixel " + str(n))
    n = n[2]
	#print("tredje värdet " + str(n))
	
    for y in range(height):
	    for x in range(width):
#	        print(pixel[x, y])
	        pixx = pixel[x, y]
	        pixx = pixx[2]
#	        if n not in pixel[x, y]: 
	        if n != pixx: 
#	            print("yes")
	            morse += 1
	            pixx = pixel[x+1, y]
	            pixx = pixx[2]
#	            if n not in pixel[x+1, y]:
	            if n != pixx:
		            continue
	            else:
		            if morse == 3:
	#	                print("_")
		                text += "-" 
		            elif morse == 1:
	#	                print(".")
		                text += "." 
	            morse = 0
	#    print(text)
	    for key, value in MORSE_CODE_DICT.items():
	        if text == value:
#	            print("Morse: " + text + " Vilket är: " + key)
	            password += key
	    text = ""
    return password	
N = 998
path = "flag/"
f = open("passwordlist.txt", "w")
for num in reversed(range(N + 1)):
    password = runner()
#    print(password)
    zip_file = "flag_" + str(num) + ".zip"
    
    print("Zippar up zip: " + zip_file + " med lösenord: " + password)
    f.write("Zip: " + zip_file + " Lösenord: " + password + "\n")
    with ZipFile(path + zip_file) as zf:
      zf.extractall(pwd=bytes(password,'utf-8'))
    shutil.copyfile(path+"pwd.png", path+str(num)+".png")
#    os.rename(path+"pwd.png", path+str(num)+".png")
    os.remove(path+zip_file)
f.close()
