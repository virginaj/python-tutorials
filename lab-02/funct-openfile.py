#!/usr/bin/python

def myfunction(var1,var2):    
    f = open(var1)
    lines = f.readlines()
    print lines
    
    if len(lines) > len(f.readlines(4)):
        print "file is over 4 bytes"

    l =[]
    for line in lines:
        if len(line) !=0:
            l = line.split()
            if len(l) !=0:
                print l

    file_output = open('testnew.csv','w')
    for line in l:
        file_output.write(line)
    
    return



if __name__ == "__main__":

    return_f = myfunction('ny-census.csv',8)

print "file is created"
f = open('testnew.csv')
wlines = f.readlines()
print wlines
