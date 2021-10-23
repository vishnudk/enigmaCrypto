import string
from typing import Literal

alp = list(string.ascii_uppercase)
alp.reverse()
rotersList = []
rtCount = [0,0,0]
for i in range(3):
    tmp = []
    tmp = alp.copy()
    rotersList.append(tmp)
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
    global alp,rotersList
    alp = list(string.ascii_uppercase)
    alp.reverse()
    rotersList = []
    rtCount = [0,0,0]
    for i in range(3):
        tmp = []
        tmp = alp.copy()
        tmp2 = tmp[:rtPos[i]]
        tmp = tmp[rtPos[i]:]
        tmp.extend(tmp2)
        rotersList.append(tmp)
    print(rotersList)
    alp.reverse()
def rotate():
    tmp = rotersList[0].pop(0)
    rotersList[0].append(tmp)
    if rotersList[0][0] == "Z":
        tmp = rotersList[1].pop(0)
        rotersList[1].append(tmp)
        if rotersList[1][0] == "Z":
            tmp = rotersList[2].pop(0)
            rotersList[2].append(tmp)
    
    
def encrypt(dir ,char , rotNo):
    if dir == "f":
        
        return rotersList[rotNo][alp.index(char)]
    else:
        
        return alp[rotersList[rotNo].index(char)]


def encryptFunction(c, rtPos):
    init(rtPos)
    global alp,rotersList
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
    global alp,rotersList
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
