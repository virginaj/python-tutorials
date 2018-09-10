#!/usr/bin/python


# Open the license file, read the content into the buffer 
# then close the file descriptor

f = open('LICENSE')
file_content = f.read()
f.close()

# Open the license file, read the content as "lines" into the 
# buffer and close it.

f = open('LICENSE')
file_content = f.readlines()
f.close()