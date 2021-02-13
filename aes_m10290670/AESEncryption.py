from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import sys


def AES_encryption(keyfilepath, plaintextfilepath, ivfilepath, ciphertextfilepath):
    key = bytes.fromhex(open(keyfilepath).read()) #read hexadecimal key from file and convert it to bytes
    m = pad(open(plaintextfilepath).read().encode(), 16) #read text from file and pad it so that it becomes multiple of 16
    iv = get_random_bytes(16)           #generate iv of 16 bytes(128 bits)
    open(ivfilepath, 'w').write(iv.hex()) #write hexadecimal form of iv to file
    CBC = AES.new(key, AES.MODE_CBC, iv)    
    c = CBC.encrypt(m)                  #encrypt padded plain text
    open(ciphertextfilepath, 'w').write(c.hex())    #write ciphertext to file
    print('Cipher text is: '+c.hex())           #output ciphertext


if __name__ == '__main__':
    AES_encryption(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    
