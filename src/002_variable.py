# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.
a=4
print("type of a: ",type(a))
b=6
c=a*b
print(c)

# variables are case sensitive
a="Sourabh"
A="Jadhav"
print("type of a: ",type(a))
print(a)
print(A)

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Cases of writing variable

# 1) Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# 2) Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"

# 3) Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"