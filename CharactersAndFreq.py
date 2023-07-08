"""
Input="testinnput"

Output="t3n2e1p1s1i1u1"

Scrieti un algoritm ce returneaza un string
compus din caracterele si frecventa lor, ordonate descrescator.
"""
import json

input_string = input("Please write a string: ")

frequency_dict = dict()
# Create a dictionary with the characters and verify how many times they appear.
for i in range(len(input_string)):
    if input_string[i] not in frequency_dict:
        frequency_dict[input_string[i]] = 1
    elif input_string[i] in frequency_dict:
        frequency_dict[input_string[i]] += 1

"""
    The string will be ordered in descending order by frequency.
        If the frequency is the same, the code will sort
            in a descending order by the ASCII value of the character.
"""
list_f = list(map(list,frequency_dict.items()))

list_sorted = list()
list_sorted = sorted(list_f, key = lambda s: (s[1],(ord, s[0])), reverse = True)

output = ""
flat_list = [item for sublist in list_sorted for item in sublist]

for i in flat_list:
    output += "".join(str(i))

print("Output= ", output)


"""
Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed.
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:

“Hey fellow warriors” //returns “Hey wollef sroirraw"

"This is a test" //returns "This is a test"

"This is another test" //returns "This is rehtona test"
"""

def reverse(word):
    """
    This function take a string as variable and returns the reversed string
        by adding the new character on the left side.
    """
    new_word = ""

    for i in word:
        new_word = i + new_word
        #print(new_word)

    return new_word

#Write a string in input and will return a list of the strings delimited by space.
string_input = (input("Type a string: ")).split()

#Verify every string from the list and if it has more than 5 characters it will reverse it. 
for elem in range(len(string_input)):
    if len(string_input[elem]) >= 5:
        new_string = reverse(string_input[elem])
        string_input[elem] = new_string

# Create the new string by having the words delimited with space.
# strip() is used in case we have spaces at both ends of the string.
print(" ".join(string_input).strip())
        
