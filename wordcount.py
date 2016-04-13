import sys

def count_words(filename):
    """Return a dictionary of word counts for given file.  

    """

    #initialize our dictionary
    word_dict = {}

    #open the file to read
    working_file = open(filename)


    for line in working_file:
        line = line.rstrip()
        words_in_line = line.split()

        # long version of working for loop:
        # for word in words_in_line:
        #     count = word_dict.get(word)
        #     # add word to dict if not already present as key
        #     if count == None:
        #         word_dict[word] = 1
        #     # increase count assigned to key
        #     else:
        #         word_dict[word] = count +1

        # short version of working for loop:
        for word in words_in_line:
            word = word.strip(',?.;-":!_')
            word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict
    

def print_dict(dictionary):
    """Print key value pairs from given dictionary."""

    for word, count in dictionary.iteritems():
        print word, count


# print_dict(count_words("test.txt"))

# print_dict(count_words("twain.txt"))

input_file = sys.argv[1]

print_dict(count_words(input_file))



