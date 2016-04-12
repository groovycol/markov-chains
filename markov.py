from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as f:
        file_contents = f.read()
        #our thought is to do this later as we iterate through the string
        #file_contents.strip('\n')

    # return "This should be a variable that contains your file text as one long string"
    return file_contents

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

   
    for index in range(len(words)):
        
        if index == len(words) - 2:
            break
        else:
            if (words[index], words[index + 1]) not in chains.keys():
                chains[(words[index], words[index + 1])] = [(words[index + 2])]
            else:
                existing_values = chains[(words[index], words[index + 1])]
                existing_values.append(words[index + 2])
                chains[(words[index], words[index + 1])] = existing_values

                # doesnt work and we dont know why:
                # chains[(words[index], words[index + 1])] = chains[(words[index], 
                #     words[index + 1])].append(words[index + 2])
            
            #old idea: word_pairs.append((words[index], words[index + 1]))
    
    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    starting_key = choice(chains.keys())
    text = starting_key[0] + ' ' + starting_key[1]
    #split here first
    split_text =text.split()

    #start while loop
    while chains.get((split_text[-2],split_text[-1]), None):
        
        text = text + ' ' + choice(chains[(split_text[-2],split_text[-1])])
        split_text =text.split()
       

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text


