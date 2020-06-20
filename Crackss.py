#!/usr/bin/env python
# -*- coding: Utf-8 -*-

""" Crackss - Python Words generator

This script allows the users to print to the console all possible words that
can be generated according to the values of arguments used.

Usage:
======
    python Crickss.py [-h] minimum maximum string [-p PATH]

    Use -h option to get more explanations about differents arguments.
"""

from itertools import takewhile
import argparse
import sys

__author__ = "Wa0k"
__copyright__ = "Copyright (c) 2020 Wa0k"
__license__ = "MIT License"
__version__ = "1.0.0"
__contact__ = "wa0k@gmail.com"
__date__ = "20/06/2020"
__status__ = "Production"


def Crackss(min_size, max_size, string, path):
    """Calculates and generates all the words.

    Parameters
    ----------
    min_size : int
        The minimal size of generated words.
    max_size : int
        The maximal size of generated words.
    string : str
        All the differents characters that will be used.
    path : str
        The path to save the result.

    Returns
    -------
    str
        The generated word.
    """
    # Number total of possible words
    total = sum([len(string) ** k for k in range(min_size, max_size + 1)])
    # Variable to count the number of word that was generated
    counter = 0
    # Calculates the first word
    word = [string[0]]
    word = word * min_size
    # Redirects the output to the path
    if path is not None:
        original_stdout = sys.stdout
        output = open(path, mode="w")
        sys.stdout = output

    # Generates the words
    while counter != total:
        for chars in string:
            word[-1] = chars
            print("".join(word))
            counter += 1
        # List of indexes of the characters whose next character is the last one in the string
        list_index = list(takewhile(lambda k: word[k + 1] == string[-1], range(len(word) - 2, -1, -1)))
        # Go to the next word size
        if "".join(word) == string[-1] * min_size:
            min_size += 1
            word = [string[0]]
            word = word * min_size
        else:
            # Generates the root of words, root => len(word)-2
            for index in list_index:
                letter_index = string.index(word[index])
                if word[index] != string[-1]:
                    word[index] = string[letter_index + 1]
                else:
                    word[index] = string[0]

    # Redirect the output to the original output
    if path is not None:
        output.close()
        sys.stdout = original_stdout

    # Informations about process
    print("Characters used : '{}'".format(string))
    print("Words generated : {}".format(total))


if __name__ == "__main__":
    import os
    import time
    parser = argparse.ArgumentParser(usage="%(prog)s [-h] minimum maximum string [-p PATH]")
    parser.add_argument("min", metavar="minimum", type=int, action="store",
                        help="minimal size of generated words.")
    parser.add_argument("max", metavar="maximum", type=int, action="store",
                        help="maximal size of generated words.")
    parser.add_argument("str", metavar="string", type=str, action="store",
                        help="all the differents characters that will be used.")
    parser.add_argument("-p", metavar="PATH", type=str, action="store",
                        help="save the result to the path. The default\n"
                             "directory is the current directory and the\n"
                             "default file name is 'word_list.txt'. The \n"
                             "path can be just the file name and this case\n"
                             "the directory is the default directory, or it\n"
                             "can be absolute / relative with or no the\n"
                             "file name. If no file name is specified then\n"
                             "this is the default file name. The extension\n"
                             "must be always '.txt' but it is not necessary\n"
                             "to specify the extension, because it is added\n"
                             "automatically.")

    args = parser.parse_args()
    complete_path = args.path

    # Checks all values of arguments
    assert (1 <= args.min <= args.max), "The minimum must be less than or equal to the maximum."
    for characters in args.str:
        assert (args.str.count(characters) == 1), "Each caracter shouldn't be repeated more than once."
    if complete_path is not None:
        path, file = os.path.split(args.path)
        file_name, extension = os.path.splitext(file)
        if len(path) != 0 and not os.path.exists(path):
            raise FileNotFoundError("The path doesn't exist: {}".format(path))
        elif len(path) == 0:
            path = os.getcwd()
        if len(file_name) == 0:
            file_name = "word_list"
        if len(extension) != 0 and extension != '.txt':
            raise AssertionError("The extension file must be '.txt'.")
        else:
            extension = ".txt"
        complete_path = path + "\\" + file_name + extension

    start = time.time()
    Crackss(args.min, args.max, args.str, complete_path)
    end = time.time()
    print("Process finished in : {} seconds.".format(end - start))
