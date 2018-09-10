#!/usr/bin/python


# Open the license file, read the content into the buffer 
# then close the file descriptor

# f = open('conditions.py')
# file_content = f.read()


f = open('conditions.py')
file_content = f.readlines()

line_list =[]

for line in file_content:
    if len(line) !=0:
        line_list = line.split()
        if len(line_list) !=0:
            if line_list[0] == 'print':
                print line_list

#print file_content.type

f.close()

# lines10 = f.read(10)
# lines11_20 = f.read(10)
# f.seek(15)
# lines15_20 =f.read(15)
# #alllines = f.read()
# print (lines10,lines11_20,lines15_20)
# f.close()

# Open the license file, read the content as "lines" into the 
# buffer and close it.

# f = open('conditions.py')
# file_content = f.readlines()
# f.close()

