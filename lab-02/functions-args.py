
def myfunction(arg1, arg2,arg3="Chicago"):
    print "My Very first python function with Arguments"
    print "{},{},{}".format(arg1, arg2, arg3)
<<<<<<< HEAD
    sum = arg1+arg2+arg3
=======
    sum = arg1 + arg2 + arg3

>>>>>>> 1d68230f98b55194981a53fc7f82765d3f870d2f
    #return sum

    if arg3 == "chicago":
        second_func(arg1,arg2)
    else:
        second_func(arg1,arg2,arg3)


# # Polymorphism in Funtion names
def second_func(arg1,arg2,arg3=None):
    print("Testing optional argument")
    print (arg1,arg2,arg3)

    print third_func(arg1)

def third_func(arg1):
    return "My arg is: " + arg1


if __name__ == "__main__":
<<<<<<< HEAD
    my_return = myfunction('Hello','world','Toronto')
    print my_return
=======
    my_return = myfunction("Hello", "World","Toronto")
    print my_return
>>>>>>> 1d68230f98b55194981a53fc7f82765d3f870d2f
