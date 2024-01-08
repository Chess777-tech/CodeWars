"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

"""

import string

def high(x):
    letter_positions = {char: index + 1 for index, char in enumerate(string.ascii_lowercase)}
    highest = 0 
    result = ""
    
    x = x.split()
    
    for word in x:
        word_sum = sum([letter_positions.get(character, 0) for character in word])
        
        if word_sum > highest:
            highest = word_sum
            result = word 
    
    print("Word with highest alphabetical value:", result)
    print("Score:", highest)

# Example usage
input_string = "Hello my name is colby "
high(input_string)