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
def init():
    global alp,rotersList
    alp = list(string.ascii_uppercase)
    alp.reverse()
    rotersList = []
    rtCount = [0,0,0]
    for i in range(3):
        tmp = []
        tmp = alp.copy()
        rotersList.append(tmp)
    alp.reverse()
def rotate(rotNo):
    if rotNo == 0:
        rtCount[rotNo] += 1 
        tmp = rotersList[rotNo].pop(0)
        rotersList[rotNo].append(tmp)
        if rotersList[rotNo][0] == alp[0]:
            rotate(rotNo)
        
    
    
def encrypt(dir ,char , rotNo):
    if dir == "f":
        rotate(rotNo)
        return rotersList[rotNo][alp.index(char)]
    else:
        rotate(rotNo)
        return alp[rotersList[rotNo].index(char)]

# c = (input("enter the plain text : "))

def encryptFunction(c):
    init()
    global alp,rotersList
    # print(c)
    c = preProcess(c)
    # print(c)
    ciplist = []
    for ch in c:
        tmp = ch
        for i in range(3):
            tmp = encrypt('f',tmp,i)
        for i in range(2):
            tmp = encrypt('b',tmp,1-i)
        ciplist.append(tmp)
    return ("".join(ciplist))
    # cipheText = "".join(ciplist)
    # plainText = []
    # for ch in cipheText:
    #     tmp = ch
    #     for i in range(2):
    #         tmp = encrypt('f',tmp,i)
    #     for i in range(3):
    #         tmp = encrypt('b',tmp,2-i)
    #     plainText.append(tmp)
    # print("".join(plainText))

def decryptFunction(cipheText):
    cipheText = preProcess(cipheText)
    global alp,rotersList
    init()
    plainText = []
    for ch in cipheText:
        tmp = ch
        for i in range(2):
            tmp = encrypt('f',tmp,i)
        for i in range(3):
            tmp = encrypt('b',tmp,2-i)
        plainText.append(tmp)
    return ("".join(plainText))

# encryptFunction(input("enter the plain text : "))