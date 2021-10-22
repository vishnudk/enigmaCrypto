import string
alp = list(string.ascii_uppercase)
alp.reverse()
roters = [alp.copy() for i in range(3)]
alp.reverse()
rc1 = 0
rc2 = 0
def rotateRoter():
    global rc1, rc2 
    rc1 +=1
    tmp = roters[0].pop(0)
    roters[0].append(tmp) 
    if rc1 == 26:
        rc1 = 0
        rc2 +=1
        tmp = roters[1].pop(0)
        roters[1].append(tmp)

def encrypt(rotNo, char):
    # print(alp)
    # print(roters[rotNo])
    return alp[roters[rotNo].index(char)]
def decrypt(rotNo, char):
    # print(alp)
    # print(roters[rotNo])
    return roters[rotNo][alp.index(char)]

if __name__ == "__main__":
    plaintext = input("Enter the plaintext : ")
    ciphertext = []
    for i in plaintext:
        ciphertext.append(encrypt(0,encrypt(1, encrypt(0, i))))
        rotateRoter()

    alp.reverse()
    roters = [alp.copy() for i in range(3)]
    alp.reverse()
    plaintextList = []
    print("".join(ciphertext))
    for i in ciphertext:
        plaintextList.append(decrypt(0,decrypt(1, decrypt(0, i))))
        rotateRoter()
    print("".join(plaintextList))
