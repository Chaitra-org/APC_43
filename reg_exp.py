# 1. Write a Python program using regular expressions to extract all digits from a given string.
# import re

# text = input("Enter a string: ")
# digits = re.findall(r'\d', text)
# print("Digits:", digits)

# 2. Accept a sentence and display all words beginning with the letter A or a.
# import re

# sentence = input("Enter a sentence: ")

# words = re.findall(r'\b[Aa]\w*', sentence)

# print("Words:", words)

# 3. Write a program to count the occurrences of vowels in a given string using regular expressions.
# import re

# text = input("Enter a string: ")
# vowels = re.findall(r'[aeiouAEIOU]', text)
# print("Number of vowels:", len(vowels))

# 4. Write a program to extract all uppercase letters from a given string.
# import re

# text = input("Enter a string: ")
# letters = re.findall(r'[A-Z]', text)
# print("Uppercase letters:", letters)

# 5. Write a program to identify all spaces, tabs, and newline characters in a text.
import re

text = input("Enter text: ")
characters = re.findall(r'[ \t\n]', text)
print("Spaces, tabs and newlines:", characters)
print("Total occurrences:", len(characters))

# 6. Write a program to replace multiple consecutive spaces with a single space.
# 7. Accept a sentence and display all words containing exactly five characters.
# 8. Write a program to identify all words ending with the letter s.
# 9. Write a program to remove all special characters from a given string while retaining letters,
# digits, and spaces.
# 10. Write a program to count the number of words in a sentence using regular expressions.
# 11. Write a program to validate a 10-digit Indian mobile number using a regular expression.
# 12. Accept an email address and check whether it follows a reasonable email format.
# 13. Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
# 14. Write a program to identify web addresses beginning with http:// or https://.
# 15. Write a program to extract all hashtags from a social media post.
# 16. Write a program to check whether a password contains at least eight characters, one uppercase
# letter, one lowercase letter, one digit, and one special character.
# 17. Write a program to identify consecutive repeated words in a sentence, ignoring case
# differences.
# 18. Write a program to extract six-digit Indian PIN codes from a paragraph.