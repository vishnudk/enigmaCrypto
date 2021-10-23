import tkinter as tk
import mapingCharacters
r = tk.Tk()
r.geometry("750x750")
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
    encryptBtn = tk.Button(r,text = "ENCRYPT",width=10,height=5,command= encrypt)
    decryptBtn = tk.Button(r,text = "DECRYPT",width=10,height=5,command= decrypt)
    inputText.pack()
    outputText.pack()
    encryptBtn.pack()
    decryptBtn.pack()
    s1.pack()
    s2.pack()
    s3.pack()
    r.mainloop()

if __name__ == '__main__':
    mainWindow()