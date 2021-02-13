from Crypto.Cipher import AES
import sys
from Crypto.Util.Padding import pad, unpad
import os

def token_generation(keyword, prfkeyfilepath, tokenfilepath):
    key = bytes.fromhex(open(prfkeyfilepath, 'r').read()) #read key from file
    ECB = AES.new(key, AES.MODE_ECB)
    keypadded = pad(keyword.encode(), 16) #encrypt keyword
    token = ECB.encrypt(keypadded).hex() 
    print(token)
    open(tokenfilepath, 'w').write(token) #write encrypted keyword to file


if __name__ == '__main__':
    token_generation(sys.argv[1], sys.argv[2], sys.argv[3])
