from Crypto.Random import get_random_bytes
import sys


def generate_AES_key(keyfilepath):
    key = get_random_bytes(32)      #Generate random key with 32 bytes (256 bits)
    print('Key generated: ' +key.hex()) #print the hexadecimal form of this key
    f = open(keyfilepath, 'w')
    f.write(key.hex())          #write the hexadecimal form of this key to file
    f.close()


if __name__ == '__main__':
    generate_AES_key(sys.argv[1])
