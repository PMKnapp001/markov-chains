"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
#     chains = {
#     ('Would', 'you'): ['could', 'could', 'could', 'could', 'like'],
#     ('you,', 'could'): ['you', 'you', 'you', 'you'],
#     ('could', 'you'):  ['in', 'with', 'in', 'with'],
#     ('you', 'in'):     ['a', 'a'],
#     ('in', 'a'):       ['house?', 'box?'],
#     # ...
#     ('Sam', 'I'):      ['am?']
# }
# 
    words_list = text_string.split()
    chains = {}

    for i in range(len(words_list) - 1):
        if (i+1) != (len(words_list) -1):
            key = (words_list[i], words_list[i + 1])
            
            if chains.get(key, 0) == 0:
                chains[key] = []
                chains[key].append(words_list[i+2])
            else:
                chains[key].append(words_list[i+2])

    # for key, value in chains.items():
    #     print(f"{key}: {value}")

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    link_key = choice(list(chains.keys()))

    while chains.get(link_key, 0) != 0:
        word = choice(chains[link_key])
        words.append(word)
        link_key = (link_key[1], word)

    # print(link_key)
    # print(type(link_key))
    # print(words)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)


# Produce random text
random_text = make_text(chains)

print(random_text)
