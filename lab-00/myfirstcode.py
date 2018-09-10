#!/usr/bin/python

# print "Hello World!"

# old_list = [ "apple", "google", "amazon" ]
# new_list = [ "APPLE", "GOOGLE", "AMAZON" ]

# my_newlist = []
# for loop in old_list:
#     my_newlist.append(loop.upper())

# print my_newlist

# dict = {}

# dict ['name'] = 'Chandan'
# dict ['city'] = 'Toronto'
# dict ['number'] = 23
# dict ['Languages'] = ['c', 'c++', 'java', 'python', 'ruby']

# dict

# for k,v in dict.items():
#     print (k, len(v))

f = open("N4xFilterTier1.csv")
mylines = f.readlines()
#print mylines

ll = []
for line in mylines[1:]:
    if float(line.split(',')[0]) > 4.0:
        ll.append(line)

f = open('ouput','w')
for l in ll:
    f.write(l)
#print ll

