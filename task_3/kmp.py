# Knuth–Morris–Pratt algorithm

def compute_lps(pattern):
    lps = [0] * len(pattern)  # Initialize the lps list where each element is 0, with a size equal to the length of the pattern
    length = 0  # Length of the previous shortest prefix suffix
    i = 1  # Index for traversing the pattern

    while i < len(pattern):
        if pattern[i] == pattern[length]:  # If the pattern character matches the character in the prefix
            length += 1  # Increase the length of the prefix suffix
            lps[i] = length  # Assign the length to lps[i]
            i += 1  # Move to the next pattern character
        else:
            if length != 0:  # If the length is not 0
                length = lps[length - 1]  # Set length to the previous lps value
            else:
                lps[i] = 0  # If the length is 0, set lps[i] = 0
                i += 1  # Move to the next pattern character

    return lps  # Return the lps list

def kmp_search(main_string, pattern):
    M = len(pattern)  # Length of the pattern
    N = len(main_string)  # Length of the main string

    lps = compute_lps(pattern)  # Calculate the lps list for the pattern

    i = j = 0  # Indexes for traversing the main string and the pattern

    while i < N:
        if pattern[j] == main_string[i]:  # If the pattern and main string characters match
            i += 1  # Move to the next main string character
            j += 1  # Move to the next pattern character

        elif j != 0:  # If the characters do not match and j is not 0
            j = lps[j - 1]  # Set j to the previous lps value

        else:
            i += 1  # Move to the next main string character

        if j == M:  # If all pattern characters have been found
            return i - j  # Return the index of the start of the found substring

    return -1  # If the substring is not found, return -1