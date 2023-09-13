from collections import Counter
from string import punctuation

def load_text(input_file):
    """
    Load text from a text file and return as a string.

    Parameters
    ----------
    input_file : str
        Path to the file to be read.

    Returns
    -------
    str
        Content of the file as a string.
    """
    with open(input_file, "r") as file:
        text = file.read()
    return text

def clean_text(text):
    """
    Lowercase and remove punctuation from a string.

    Parameters
    ----------
    text : str
        Input string that needs to be cleaned.

    Returns
    -------
    str
        Cleaned string with all lowercase characters and without any punctuation.
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    """
    Count unique words in a string.

    Parameters
    ----------
    input_file : str
        Path to the file whose unique words need to be counted.

    Returns
    -------
    Counter
        A Counter object containing the frequency of each unique word in the input file.
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
