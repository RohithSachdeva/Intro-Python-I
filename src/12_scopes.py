# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

#local and global?  Think global is the only one that can be called 


# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
#Declare it global before it gets reassigned the value 

print(x)


# This nested function has a similar problem.
#nonlocal as a keyword?  
#https://www.xspdf.com/resolution/51781973.html

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
