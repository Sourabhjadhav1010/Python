# Global Variables
# Variables that are created outside of a function (as in all of the examples above)
# are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  y="better" # y becomes local varible as we cannot access it out of function  
  global a   # with global keyword we can access this vatiable globally
  a = "fantastic"
  print("Python is",x)
  print(y)
myfunc()
print(x)
print(a)