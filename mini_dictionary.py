# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values
# Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

# 1st method

my_dict = dict()

for i in range(97,123) :
    my_dict[chr(i)] = i
print("Ascii value is : ", my_dict)


# 2nd method 

my_dict = dict()

ascii_value = ord('a')

for i in  ("abcdefghijklmnopqrstuvwxyz") :
    my_dict[i] = ascii_value
    ascii_value +=1
print("Ascii value is : ", my_dict)