from Crypto.Random import get_random_bytes
import sys


def key_generation_function(aeskeyfilepath, prfkeyfilepath):
    aeskey = get_random_bytes(32) #generate aeskey
    prfkey = get_random_bytes(32) #generate prfkey
    print('AES Key: '+aeskey.hex())
    print('PRF Key: '+prfkey.hex())
    open(aeskeyfilepath, 'w').write(aeskey.hex()) #write keys to file
    open(prfkeyfilepath, 'w').write(prfkey.hex())


if __name__ == '__main__':
    key_generation_function(sys.argv[1], sys.argv[2])
