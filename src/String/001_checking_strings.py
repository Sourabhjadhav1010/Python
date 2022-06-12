# Strings are immutable , we an change value of string after decleration

# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
print("free" in txt)   # checking free is present in string or not, will print True

if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)  # will print True

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

for x in "banana":
  print(x)