#!/usr/bin/python

my_string = "My string has many spaces let me see how many"

print my_string.split()

first_item = my_string[0]
print first_item

see_item = my_string.split[7]
print see_item

print "Lets loop through the strings"

for s in my_string.split():
    new_split = s.split('see')
    print ("String literal ", new_split)


my_string = "My,string,has,many,commas,let,me,see,how,many"

# Assignment
# Count number of , in the string
# Replace , with space
# Count the string length
# Find the index where the word many starts