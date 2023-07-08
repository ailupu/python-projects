num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 ponints to:", id(num1))
print("num2 ponints to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 ponints to:", id(num1))
print("num2 ponints to:", id(num2))

# Works like this because integers are not imutable

# Example with dictionary

#they will point to the same dictionary
dict1 = {'value' : 1}
dict2 = dict1

print("\nBefore dict2 dictionary is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 ponints to:", id(dict1))
print("dict2 ponints to:", id(dict2))

dict2['value'] = 22

print("\nAfter dict2 dictionary is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 ponints to:", id(dict1))
print("dict2 ponints to:", id(dict2))

# Both values are changed. -> they are the same -> dictionaries can be changed
