#/usr/bin/python3

# Basic use of arrays and definition of functions.
# TODO: demonstrate with exercises

def helloWorld():
    print("Hello, World!")

def fullName(fname = "Doe", pname = "John"):
    print("Full Name: " + pname + " "+ fname)
    return (pname + " "+ fname)
# call it as    fullName("Daniels", "Jack")
#               fullName (pname = "Jack", fname = "Daniels")

# empty function, just for testing
def void ():
    pass

def unknownNumberOfArguments(*args):
    print(args[0]) #print the first one

def unknownNumberOfKeywordArguments(**args):
    print(args[0]) #print the first one

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

def arrayLength(arr):
    for x in arr:
        print(x)

    x.append("Another element")
    x.pop(1)    # second element removed
    x.remove ("Item to delete")

    return len(arr)
