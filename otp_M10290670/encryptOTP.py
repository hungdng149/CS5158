import sys


def encryptOTP(keyfilepath, plaintextfilepath, ciphertextfilepath):
    sk = open(keyfilepath).read()   #read key from file 
    m = open(plaintextfilepath).read()    #read plain text from file
    mb = ''
    for i in range(len(m)):
        mb += (bin(ord(m[i])).replace("b", ""))  #convert plaintext to binary
    if len(mb) == len(sk):         #compare plaintext length with key length
        x = [abs(int(sk[i]) - int(mb[i])) for i in range(len(sk))]     #XOR operation(absolute value of the subtraction between each value in the binary string)
        c = ''.join(map(str, x))    #concatenate values in the list to a binary string
        print('Ciphertext is: '+c)
        f = open(ciphertextfilepath, 'w')       #write to file
        f.write(c)
        f.close()
    else:
        print('error: length is incorrect')
		

if __name__ == '__main__':
    encryptOTP(sys.argv[1], sys.argv[2], sys.argv[3])
