import nltk
import re

nltk.download('words', quiet = True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()

def encrypt(plain, key):
    new_string = ''
    for char in plain:
        if re.match("[A-Z]", char):
            new_char = 65 + ((ord(char)- 65) + key) % 26
            new_string += chr(new_char)
        elif re.match("[a-z]", char):
            new_char = 97 + ((ord(char) - 97) + key) %26
            new_string += chr(new_char)
        else:
            new_string += char
    return new_string


def decrypt(encrypted, key):
    return encrypt(encrypted, -key)



def crack(encrypted):
    string_list = []
    percentages = []
    for num in range(27):
        string_list.append(decrypt(encrypted, -num))
    for string in string_list:
        word_count = count_words(string)
        percentage = int(word_count / len(string.split())*100)
        percentages.append(percentage)
    return string_list[percentages.index(max(percentages))]


def count_words(text):
    candidate = text.split()

    word_count = 0

    for string in candidate:
        if string.lower() in word_list or string in name_list:
            word_count += 1
        else:
            pass
    return word_count


encrypted = encrypt("Two more days and all his problems would be solved",4)
print(encrypted)

# print(decrypt(encrypted, 2))

print(crack(encrypted))

