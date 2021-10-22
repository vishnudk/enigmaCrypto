import tkinter as tk
import mapingCharacters
r = tk.Tk()
r.geometry("250x170")
r.title('Enigma')
inputText = tk.Text(r,height=10,width=50)
outputText = tk.Text(r,height=10,width=50)

def encrypt():
    outputText.insert(tk.END, mapingCharacters.encryptFunction(inputText.get(1.0, "end-1c")))
def decrypt():
    outputText.insert(tk.END,mapingCharacters.decryptFunction(inputText.get(1.0, "end-1c")))
def mainWindow():
    encryptBtn = tk.Button(r,text = "ENCRYPT",width=10,height=5,command= encrypt)
    decryptBtn = tk.Button(r,text = "DECRYPT",width=10,height=5,command= decrypt)
    inputText.pack()
    outputText.pack()
    encryptBtn.pack()
    decryptBtn.pack()

    r.mainloop()

if __name__ == '__main__':
    mainWindow()