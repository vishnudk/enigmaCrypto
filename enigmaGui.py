import tkinter as tk
import mapingCharacters
r = tk.Tk()
r.geometry("750x550")
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
    outputText.insert(tk.END, mapingCharacters.encryptFunction(inputText.get(1.0, "end-1c"),rtPos))
def decrypt():
    rtPos = [s1.get()-1, s2.get()-1, s3.get()-1]
    outputText.delete(1.0,tk.END)
    outputText.insert(tk.END,mapingCharacters.decryptFunction(inputText.get(1.0, "end-1c"),rtPos))
def mainWindow():
    rotersLabel = tk.Label(r,text="Rotor Adjustment")
    plainTextLabel = tk.Label(r,text = "Plain Text")
    cipherTextLabel = tk.Label(r,text ="Cipher Text")
    encryptBtn = tk.Button(r,text = "ENCRYPT/DECRYPT",width=20,height=2,command= encrypt)
    # decryptBtn = tk.Button(r,text = "DECRYPT",width=10,height=5,command= decrypt)
    rotersLabel.grid(row =0, column = 2)
    inputText.grid(row = 1,column = 0)
    outputText.grid(row = 3,column = 0)
    encryptBtn.grid(row = 4,column = 0)
    # decryptBtn.grid(row = 4,column = 1)
    s1.grid(row = 1,column =1)
    s2.grid(row = 1,column =2)
    s3.grid(row = 1,column =3)
    plainTextLabel.grid(row =0 , column =0)
    cipherTextLabel.grid(row =2 , column =0)
    r.mainloop()

if __name__ == '__main__':
    mainWindow()