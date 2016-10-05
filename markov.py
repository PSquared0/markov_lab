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
    
    random_key = choice(chains.keys()) #randomly picking key from dictionary to start
    random_words_text = list(random_key) #creating a list of our keys and binding to random words text
    next_word_choices = chains[random_key] #we are looking up key in dict and returning the value
    next_word = choice(next_word_choices) #picking item from the list(value)
    random_words_text.append(next_word) #adding new word to the list
    next_tuple = (random_words_text[-2], random_words_text[-1]) #creating next tuple to refernce to picking next value

    while next_tuple in chains: # while the key exists in dict
        next_word_choices = chains[next_tuple] #using the key to find the value
        next_word = choice(next_word_choices) #randomly picking item the list
        random_words_text.append(next_word) # adding that word to the list
        next_tuple = (random_words_text[-2], random_words_text[-1]) ##creating next tuple to refernce to picking next value

    for i in range(len(random_words_text)): #going through our list
        
        if text == "": #if the string is empty
            text = random_words_text[i] #then add randome word text
        else:
            text = text + " " + random_words_text[i] # if not add a space and the random word


    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
