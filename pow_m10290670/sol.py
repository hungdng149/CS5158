import sys
from hashlib import sha256


def solution_generation(targetpath, inputpath, solutionpath):
    target = open(targetpath, 'r').read() #read target
    input = open(inputpath, 'r').read() #read input
    find_solution(input, target, solutionpath)


def find_solution(input, target, solution):
    i = 0
    while True:
        input1 = input + str(i) #create new string to test
        hex = sha256(input1.encode()).hexdigest() #get sha-256 hexadecimal of string
        binary = bin(int(hex, 16))[2:].zfill(256) #get binary of string
        i += 1 #increment potential solution by 1
        if binary <= target: #compare binary of string with target
            open(solution, 'w').write(input1[9:]) #if it is, write solution to file
            print(input1[9:])#print out solution
            return input1 #stop the function


if __name__ == '__main__':
    solution_generation(sys.argv[1], sys.argv[2], sys.argv[3])
