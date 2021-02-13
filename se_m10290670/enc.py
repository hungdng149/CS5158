from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from nltk.tokenize import word_tokenize
import sys


def decode_binary_string(s): #decode bin string to hex
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


def build_inverted_index(directory, prfkeyfilepath, indexfilepath):
    key = bytes.fromhex(open(prfkeyfilepath, 'r').read()) #get key from file
    ECB = AES.new(key, AES.MODE_ECB)  
    f = []
    s = ""
    count = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            count += 1 #get number of files in directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  
            f.append(open(directory+'/'+filename, 'r').read()) #read file contents and add to a array
    for i in f:
        s += " " + i #convert array into string
    for i in range(1):
        text_tokens = word_tokenize(s)  #create tokens from the string
    tokens = list(dict.fromkeys(text_tokens))
    dictionary = {}
    for i in range(count): #compare and create inverted index, for each key, check the array to see if key exists in said array
        check = f[i].lower() 
        for item in tokens: #iterate through tokens
            s = pad(item.encode(), 16) 
            txt = ECB.encrypt(s) #encrypt token
            txt = txt.hex() #convert token bytes to hex
            if item in check:
                if txt not in dictionary:
                    dictionary[txt] = [] #encrypted token doesn't exist in dictionary, add encrypted token
                if txt in dictionary:
                    dictionary[txt].append("c" + str(i + 1) + '.txt') #if encrypted token in dictionary, append file name to encrypted token dictionary key to create inverted index, 
    for k in dictionary.keys():  #print out dictionary
        print(k, dictionary[k])
    with open(indexfilepath, 'w') as f: #write dictionary to index file
        for k in dictionary.keys():
            print(k, dictionary[k], file=f)


def encrypt_files(filedirectory, cipherfiledirectory, aeskeyfilepath):
    key = bytes.fromhex(open(aeskeyfilepath, 'r').read()) #read key from file
    iv = get_random_bytes(16)
    CBC = AES.new(key, AES.MODE_CBC, iv)
    open("C:/Users/hungn/Documents/se_m10290670/data/iv.txt", 'w').write(iv.hex())
    count = 1
    for filename in os.listdir(filedirectory):
        open(cipherfiledirectory+'/'+'c'+str(count)+'.txt', 'w').close() #empty file
        if filename.endswith('.txt'):
            cipher = "" 
            f = (open(filedirectory+'/'+filename, 'r').read()) #read all contents of a file
            x = pad(f.encode(), 16) 
            c = CBC.encrypt(x).hex() #encrypt the string
            open(cipherfiledirectory+'/'+'c'+str(count)+'.txt', 'w').write(c) #write string variable to file
        count += 1

if __name__ == '__main__':
    build_inverted_index(sys.argv[1],sys.argv[2],sys.argv[3])
    encrypt_files(sys.argv[1], sys.argv[4], sys.argv[5])
