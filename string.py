# # 1. Write a program to input a string and display its length without using the len() function.
# str=input("enter a string: ")
# print("length of string is :",len(str))

# #   2. Count the number of vowels, consonants, digits, spaces, and special characters in a given
# #  string
# str=input("enter a string: ").lower()
# vowels=0
# consonants=0
# digits=0
# spaces=0
# special_characters=0
# for i in str:
#     if i.isalpha():
#         if i in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     elif i.isdigit():
#         digits += 1
#     elif i == " ":
#         spaces += 1
#     else:
#         special_characters += 1

# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)
# print("Number of digits:", digits)
# print("Number of spaces:", spaces)
# print("Number of special characters:", special_characters)

# # 3. Reverse the given string without using built-in reverse functions.
# str=input("enter a string: ").lower()
# rev=""
# for i in str:
#     rev=i+rev
# print("Reversed string:", rev)

# # 4. Check whether the entered string is a palindrome.
# str=input("enter a string: ").lower()
# rev=""
# for i in str:
#     rev=i+rev
# if str==rev:
#     print("the string is palindrome")
# else:
#     print("string is not palindrome")

# # 5. Count the number of uppercase and lowercase letters in a string.
# str=input("enter a string:")
# upper=0
# lower=0
# for i in str:
#     if i.upper()==i:
#         upper = upper + 1
#     elif i.lower()==i:
#         lower= lower + 1
# print("uppers: ",upper)
# print("lowers: ",lower)

# # 6. Replace all occurrences of a given character with another character.
# str=input("enter a string:")
# old=input("enter the character to be replaced:")
# new=input("enter the new character:")
# str=str.replace(old, new)
# print("string after replacement:", str)

# # 7. Remove all spaces from the input string.
str=input("enter a string:")
str=str.replace(" ", "")
print(str)

# # 8. Find the number of times a specified character appears in a string.
# str=input("enter a string: ")
# char=input("enter the character to count: ")
# count=0
# for i in str:
#     if i==char:
#         count= count + 1
# print(char, " : ", count)

# # 9.  Print the first and last character of a string.
# str=input("enter a string: ")
# print("first character :",str[0])
# print("last character :",str[-1])

# # 10.  Display each character of a string along with its ASCII value.
# str=input("enter a string: ")
# for i in str:
#     print(i, " : ", ord(i))

# # 11. Count the total number of words in a sentence.
# sent=input(" enter a sentence:")
# count=0
# for i in sent:
#     if i==" ":
#         count+=1
# print("total number of words in the sentence:", count+1)

# # 12. Find the longest word in a given sentence.
# sent=input("enter a sentence: ")
# words=sent.split()
# longest_word=""
# for w in words:
#     if len(w) > len(longest_word):
#         longest_word = w
# print("The longest word is:", longest_word)

# # 13. Find the shortest word in a sentence.
# sent=input("enter a sentence: ")
# words=sent.split()
# shortest_word=words[0]
# for w in words:
#     if len(w) < len(shortest_word):
#         shortest_word = w
# print("The shortest word is:", shortest_word)

# # 14. Convert the first letter of every word to uppercase.
# sent=input("enter a sentence: ")
# words= sent.split()
# for i in range(len(words)):
#     words[i]=words[i].capitalize()
# print(" ".join(words))

# # 15. Print all duplicate characters in a string.
# str=input("enter a string: ")
# duplicates=""
# for i in str:
#     if str.count(i) > 1 and i not in duplicates:
#         duplicates += i
# print("Duplicate characters:", duplicates)

