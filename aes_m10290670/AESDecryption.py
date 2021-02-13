from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
import sys


def AES_decryption(keyfilepath, ivfilepath, ciphertextfilepath, resultfilepath):
    key = bytes.fromhex(open(keyfilepath).read())   #read key from file and convert it to bytes
    iv = bytes.fromhex(open(ivfilepath).read())     #read iv from file and convert it to bytes
    c = bytes.fromhex(open(ciphertextfilepath).read())  #read ciphertext from file and convert it to bytes
    CBC = AES.new(key, AES.MODE_CBC, iv) 
    m = unpad(CBC.decrypt(c), 16) #decrypt and unpad the decrypted plain text
    open(resultfilepath, 'w').write(m.decode()) #write to file
    print('Plaintext is: ' +m.decode()) #print string output


if __name__ == '__main__':
    AES_decryption(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
