import tkinter as tk
from tkinter.constants import COMMAND
import mapingCharacters
from typing import Literal
import string

alp = list(string.ascii_uppercase)
r = tk.Tk()
r.geometry("850x550")
r.title('Enigma')
inputText = tk.Text(r,height=10,width=50)
outputText = tk.Text(r,height=10,width=50)
s1 = tk.Scale( r, 
           from_ = 1, to = 26,
           orient = tk.VERTICAL)
s2 = tk.Scale( r, 
           from_ = 1, to = 26,
           orient = tk.VERTICAL)
s3 = tk.Scale( r, 
           from_ = 1, to = 26,
           orient = tk.VERTICAL)

def encrypt():
    rtPos = [s1.get()-1, s2.get()-1, s3.get()-1]
    outputText.delete(1.0,tk.END)
    textData = inputText.get(1.0, "end-1c")

    data = mapingCharacters.encryptFunction(textData,rtPos)
    print("===================================")
    s1.set(data[0][0]+1)
    s2.set(data[0][1]+1)
    s3.set(data[0][2]+1)
    for i in range(3):
        print(data[0][i])
    outputText.insert(tk.END, data[1])

def mainWindow():
    rotersLabel = tk.Label(r,text="Rotor Adjustment")
    plainTextLabel = tk.Label(r,text = "Plain Text")
    cipherTextLabel = tk.Label(r,text ="Cipher Text")
    encryptBtn = tk.Button(r,text = "ENCRYPT/DECRYPT",width=20,height=2,command= encrypt)
    # decryptBtn = tk.Button(r,text = "DECRYPT",width=10,height=5,command= decrypt)
    rotersLabel.grid(row =0, column = 3)
    inputText.grid(row = 1,column = 1)
    outputText.grid(row = 3,column = 1)
    encryptBtn.grid(row = 4,column = 1)
    # decryptBtn.grid(row = 4,column = 1)
    s1.grid(row = 1,column =2)
    s2.grid(row = 1,column =3)
    s3.grid(row = 1,column =4)
    plainTextLabel.grid(row =0 , column =1)
    cipherTextLabel.grid(row =2 , column =1)
    r.mainloop()

if __name__ == '__main__':
    mainWindow()
    