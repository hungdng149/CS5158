import random
import sys


def generate_new_key(key_length, newkeyfilepath):
    if 0< key_length< 129:
        key = ''.join(random.choice('10') for i in range(key_length)) #create a string of key_length length with each character randomized between 0 and 1
        print(key)
        f = open(newkeyfilepath, 'w')
        f.write(key)            #write key to file
        f.close()
    else:
        print('Invalid key length') #if key length is not between 1 and 128, print error message


if __name__ == '__main__':
    generate_new_key(int(sys.argv[1]), sys.argv[2])
