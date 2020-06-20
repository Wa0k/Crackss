# Crackss
Created by: Louis ONILLON/@Wa0k

Inspired by: Crunch

Published on : 20/06/2020

Version 1.0.0

# Description
This script is a Python word generator, it allows the users to print to the console all possible words that can be generated according to the values of arguments used.

# Usage
To use the script you must use the command line, the syntax is : `python Crackss.py [-h] minimum maximum string [-p PATH]`

## Positionnal arguments
* minimum : minimum size of generated words
* maximum : maximum size of generated words
* string : all characters that will be used, 

## Optionnal arguments
* -h : show the help message and exit
* -p PATH : redirect the result and save it to the path  

**More details about the path** : if the path to the directory is only specified so the default file name will be 'word_list.txt', and if only file name is specified so the default directory will be current directory. The extension file must be always '.txt', it isn't necesseary to specified the extension after the file name because it is added automatically.

## Arguments preconditions
* minimum : must be less than or equal to the maximum
* maximum : must be greater than or equal to the minimum
* string : must contain characters that must not be repeated more than once
* PATH : valid path

# Example :
`python Crackss.py 3 5 abcd` : will generate all words with a minimal size of 3 characters until 5 characters containing the characters "abcd". None file will be created after the process because no path has benn specified.

`python Crackss.py 3 5 abcd -p list` : will create a file whose name will be "list" inside the current directory.

`python Crackss.py 3 5 abcd -p C:\Users\Wa0k\My_directory\` : now, this command will create a file with default file name so "word_list.txt" but inside of my directory named "My_directory".

`python Crackss.py 3 5 abcd -p C:\Users\Wa0k\My_directory\list` : this command use the full syntax of the script, it will generate a file named "list" inside of my directory named "My_directory".

You can find in "Example of file" directory, a file that created with the third syntax.


Have fun with my script !
