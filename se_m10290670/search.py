from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import sys


def search_function(tokenfilepath, indexfilepath, cipherdirectory, resultfilepath, aeskeyfilepath):
    key = bytes.fromhex(open(aeskeyfilepath, 'r').read()) #read key from file
    iv = bytes.fromhex(open("C:/Users/hungn/Documents/se_m10290670/data/iv.txt").read())
    token = open(tokenfilepath, 'r').read()
    indexes = open(indexfilepath, 'r').readlines()
    CBC = AES.new(key, AES.MODE_CBC, iv)
    for i in indexes: #check for index match
        s = i[33:] #get all txt files 
        c = "" 
        if token in i:
            c += s
            s = s.rstrip() 
            s = s.replace("'", "")
            s = s.replace("[", "")
            s = s.replace("]", "")
            sl = s.split(", ") #strip all to get .txt files
            for file in sl:
                c += file 
                f = bytes.fromhex(open(cipherdirectory + '/' + file, 'r').read()) #get cipher strings in files
                print(f)    
                m = unpad(CBC.decrypt(f), 16)
                c += " " + m.decode()
                c += "\n"
                open(resultfilepath, 'w').write(c)
            print(c) 

if __name__ == '__main__':
    search_function(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
