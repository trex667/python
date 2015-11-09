import sys, os, commands

if __name__=='__main__':
    file = open('blub.txt', 'w')
    print(commands.getoutput('ls -lA'))
    
    file.close()
    