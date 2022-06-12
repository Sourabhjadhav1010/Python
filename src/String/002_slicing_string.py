name="Sourabh Jadhav" #declaring string variable
print(name)           #priting value od String
print(len(name))      #printing length of string
print(name[1])        #getting charater at index -> index start from 0 and ends len-1
print(name[1:])       #getting string from index till end
print(name[:12])      #getting string form start to specified index
print(name[8:14])     #getting string between two index

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])