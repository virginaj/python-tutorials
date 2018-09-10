#!/usr/bin/python

with open('/var/log/system.log') as f:
    file_data = f.read()
    #print file_data
buffer =file_data
print buffer
f1 = open('mylogfile.log','w+')
f1.write(buffer)
f1.close

list =[]
for line in buffer.split('\n'):
    #type(buffer.split('\n')[0])
    if line is not None:
       word = len(line.split(' '))
       list.append(word)
       print list
    