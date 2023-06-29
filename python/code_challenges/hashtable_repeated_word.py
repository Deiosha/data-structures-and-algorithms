from data_structures.hashtable import Hashtable
import string

def first_repeated_word(input_string):
    words = [word.strip(string.punctuation).lower() for word in input_string.split()]
    hashtable = Hashtable()


    for word in words:
        if hashtable.has(word):
            return word
        hashtable.set(word, None)
    return None
