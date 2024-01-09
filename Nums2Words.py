"""
When provided with a number between 0-9, return it in words.
Input :: 1
Output :: "One".
If your language supports it, try using a switch statement.
"""


def number_to_words (number):
    words_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    return words_dict.get(number)


input_number = 5  # Reoplace this valuie with the number you want to convert
result = number_to_words(input_number)
print(result)