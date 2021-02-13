import sys
from hashlib import sha256


def verification_function(targetpath, inputpath, solutionpath):
    target = open(targetpath, 'r').read() #read solution from file
    input = open(inputpath, 'r').read() #read input from file
    solution = open(solutionpath, 'r').read()   #read solution from file
    input1 = input+solution #create input + solution to test
    hex = sha256(input1.encode()).hexdigest()   #create hexadecimal from input1 using sha-256   
    binary = bin(int(hex, 16))[2:].zfill(256) #create binary from hexadecimal
    if binary <= target: #test binary with target
        print(1) #print 1 if solution is correct
    else:
        print(0) #print 0 if solution isn't correct


if __name__ == '__main__':
    verification_function(sys.argv[1], sys.argv[2], sys.argv[3])
