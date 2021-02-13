import sys


def target_generation(d, targetpath):
    target = int(d)*'0'+(256-int(d))*'1' #create target with d 0s and 256-d 1s
    print(target)   #print out target
    open(targetpath, "w").write(target) #write target to file


if __name__ == '__main__':
    target_generation(sys.argv[1], sys.argv[2])
