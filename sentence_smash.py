"""
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, 
there shouldn't be a space at the beginning or the end of the sentence!
"""
# EXAMPLE: ['hello','world','this','is','great'] => 'hello world this is great 



def smash(words):
    str = ""
    for word in words: 
        str += word + " "
    return str.strip()
# strip() removes spaces at the beginning and at the end of the string:


word_list = ['hello','world','this','is','me']
result = smash(word_list)
print(result)