import sys


def decryptOTP(keyfilepath, ciphertextfilepath, plaintextfilepath):
    sk = open(keyfilepath).read()               #read key
    c = open(ciphertextfilepath).read()             #read ciphertext
    if len(sk) == len(c):     #compare ciphertext length with key length
        pt1 = ''
        pt2 = ''
        pt3 = ''
        pt4 = ''
        x = [abs(int(sk[i]) - int(c[i])) for i in range(len(sk))] #XOR operation(absolute value of the subtraction between each value in the binary string)
        for i in range(len(x)):
            if i < 8:
                pt1 += str(x[i])
            elif i < 16:
                pt2 += str(x[i])
            elif i < 24:
                pt3 += str(x[i])
            elif i < 32:
                pt4 += str(x[i])    #separate the binary string into 4 parts of 8
        m = chr(int(pt1, 2)) + chr(int(pt2, 2)) + chr(int(pt3, 2)) + chr(int(pt4, 2)) #convert binary strings to plaintext and concatenate them
        print('Plain text is: '+m)
        f = open(plaintextfilepath, 'w')
        f.write(m)           #write plaintext to file
        f.close()
    else:
        print('error: length is incorrect')


if __name__ == '__main__':
    decryptOTP(sys.argv[1], sys.argv[2], sys.argv[3])
