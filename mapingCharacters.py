import string

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

c = input("enter the plain text : ")
ciplist = []
for ch in c:
    tmp = ch
    for i in range(3):
        tmp = encrypt('f',tmp,i)
    for i in range(2):
        tmp = encrypt('b',tmp,1-i)
    ciplist.append(tmp)
print("".join(ciplist))
cipheText = "".join(ciplist)
alp.reverse()
rotersList = []
for i in range(3):
    tmp = []
    tmp = alp.copy()
    rotersList.append(tmp)

alp.reverse()
plainText = []
for ch in cipheText:
    tmp = ch
    for i in range(2):
        tmp = encrypt('f',tmp,i)
    for i in range(3):
        tmp = encrypt('b',tmp,2-i)
    plainText.append(tmp)
print("".join(plainText))