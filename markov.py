from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


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

    for i in range(len(words)):
        if i < len(words) -2: 
            key = (words[i], words[i + 1])
            if key not in chains:
                value = [words[i + 2]]
                chains[key] = value
            else:
                chains[key].append(words[i + 2])

        # elif i == len(words) -2:
        #     key = (words[i], words[i + 1])
        #     value = words[0]
        #     chains[key] =  value

    return chains        

    #return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #Start with a link (key)
    #Make a new key out of the second word in the first key and the random word 
    #you pulled out from the list of words that followed it.
    #Look up that new key in the dictionary, and pull a new random word out of the new list.
    #Keep doing that until your program raises a KeyError.

    text = ""

    random_key = choice(chains.keys())
    next_word_choice = chains[random_key]
    next_word = choice(next_word_choice)

    random_words_text = list(random_key)
    random_words_text.append(next_word)
    next_tuple = tuple(random_words_text[1: ])
    next_word_choice = chains[next_tuple]
    next_word = choice(next_word_choice)
    random_words_text.append(next_word)
    print random_words_text

    # print random_words_text

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
