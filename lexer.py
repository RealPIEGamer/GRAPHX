# For checking if file path exists
from os.path import exists

def lex(file):
    # If the file path doesn't exist, return exception
    if not exists(file):
        return print(Exception('E001 (FILE_ERR): Failed to locate file, try using an absolute file path'))

    # Create some variables for error handling
    line = -1
    pos = -1
    tokens = []

    # Open the file for reading
    with open(file, 'r') as f:

        # Read file character-by-character
        for line in f:
            for char in line:
                # Skip newlines
                if char == '\n':
                    line += 1
                # Skip whitespace
                elif char == ' ':
                    pos += 1
                # Strings
                elif char == '"' or "'":
                    # Initialize a buffer string
                    buffer = '"'

                    # While the current character does not represent a string ending character...
                    while char != '"' or char != "'":
                        # Due to tokens, will check token index before continuing
                        if line[pos] == '"' or line[pos] == "'":
                            print(buffer)
                            break

                        # Add char to buffer
                        buffer += line[pos]

                        # Increment position
                        pos += 1

                    # Print the buffer, to make sure
                    print(f'{buffer}"')

                    # Increment position again, since the string has ended
                    pos += 1
                else:
                    print(f'E002: Unimplemented at line {line}, position {pos}, character {char}')