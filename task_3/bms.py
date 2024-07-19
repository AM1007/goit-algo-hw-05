# Boyer-Moore algorithm

def build_shift_table(pattern):
    """Build a shift table for the Boyer-Moore algorithm."""
    table = {}  # Initialize an empty shift table
    length = len(pattern)  # Determine the length of the pattern
    # For each character in the pattern except the last one, set the shift equal to the length of the pattern minus the current index minus 1
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # If a character is not in the table, the shift will be equal to the length of the pattern
    table.setdefault(pattern[-1], length)
    return table  # Return the shift table

def boyer_moore_search(text, pattern):
    # Create a shift table for the pattern (substring)
    shift_table = build_shift_table(pattern)
    i = 0  # Initialize the initial index for the main text

    # Traverse the main text, comparing it with the pattern
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Start from the end of the pattern

        # Compare the characters from the end of the pattern to its beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Move towards the beginning of the pattern

        # If the entire pattern matches, return its position in the text
        if j < 0:
            return i  # Pattern found

        # Adjust the index i based on the shift table
        # This allows "skipping" over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # If the pattern is not found, return -1
    return -1