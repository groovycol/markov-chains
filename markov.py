import sys

from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as f:
        file_contents = f.read()
      
    return file_contents


def make_chains(text_string, num):
    """Takes input text as string as well as an integer for dictionary key length; 
    returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2,... wordn)
    and the value would be a list of the word(s) that follow those
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita",2)
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    # chains = {}

    # words = text_string.split()

   
    # for index in range(len(words) - 2):
        
    #     word_pair_key = (words[index], words[index + 1])

    #     chains[word_pair_key] = chains.get(word_pair_key, []) + [words[index + 2]]
    
    # return chains

    chains = {}

    words = text_string.split()

   
    for index in range(len(words) - num):
        # word_key = []

        # for i in range(num):
        #     word_key.append(words[i])

        word_key = tuple(words[index:index + num]) #for i in range(num)])

        # word_key = tuple(word_key)

        chains[word_key] = chains.get(word_key, []) + [words[index + num]]
    
    return chains



def make_text(chains, num):
    """Takes dictionary of markov chains; returns random text."""

    starting_key = choice(chains.keys())
    #text = starting_key[0] + ' ' + starting_key[1]
    text = ' '.join(starting_key)
    #split here first
    split_text = text.split()

    #start while loop

    #new_key = (split_text[-2],split_text[-1])

    #while chains.get((split_text[-2],split_text[-1]), None):
    while chains.get(tuple(split_text[-num:]), None):
    #while chains.get(new_key, None):
        
        new_word = choice(chains[tuple(split_text[-num:])])

        text = text + ' ' + new_word
        split_text.append(new_word)

    return text


input_path = "green-eggs.txt"
# input_path = "gettysburg.txt"
# input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,3)
print chains

# Produce random text
random_text = make_text(chains, 3)

# print random_text


