import string
from typing import Literal

alp = list(string.ascii_uppercase)
alp.reverse()
rotorsList = []
rtCount = [0,0,0]
for i in range(3):
    tmp = []
    tmp = alp.copy()
    rotorsList.append(tmp)
alp.reverse()
def preProcess(txt):
    global alp
    txt = txt.upper()
    txt = list(txt.split())
    txt = "".join(txt)
    # print(txt)
    res = []
    for t in txt:
        if t in alp:
            res.append(t)
    return "".join(res)
def init(rtPos):
    global alp,rotorsList
    alp = list(string.ascii_uppercase)
    alp.reverse()
    rotorsList = []
    rtCount = [0,0,0]
    for i in range(3):
        tmp = []
        tmp = alp.copy()
        tmp2 = tmp[:rtPos[i]]
        tmp = tmp[rtPos[i]:]
        tmp.extend(tmp2)
        rotorsList.append(tmp)
    # print(rotorsList)
    alp.reverse()
def rotate():
    tmp = rotorsList[0].pop(0)
    rotorsList[0].append(tmp)
    if rotorsList[0][0] == "Z":
        tmp = rotorsList[1].pop(0)
        rotorsList[1].append(tmp)
        if rotorsList[1][0] == "Z":
            tmp = rotorsList[2].pop(0)
            rotorsList[2].append(tmp)
    
    
def encrypt(dir ,char , rotNo):
    if dir == "f":
        
        return rotorsList[rotNo][alp.index(char)]
    else:
        
        return alp[rotorsList[rotNo].index(char)]


def encryptFunction(c, rtPos):
    init(rtPos)
    global alp,rotorsList
    c = preProcess(c)
    ciplist = []
    for ch in c:
        tmp = ch
        for i in range(3):
            tmp = encrypt('f',tmp,i)
        for i in range(2):
            tmp = encrypt('b',tmp,1-i)

        rotate()
        ciplist.append(tmp)
    return ("".join(ciplist))
    
def decryptFunction(cipheText,rtPos):
    cipheText = preProcess(cipheText)
    global alp,rotorsList
    init(rtPos)
    plainText = []
    for ch in cipheText:
        tmp = ch
        for i in range(2):
            tmp = encrypt('f',tmp,i)
        for i in range(3):
            tmp = encrypt('b',tmp,2-i)
        rotate()
        plainText.append(tmp)
    return ("".join(plainText))
