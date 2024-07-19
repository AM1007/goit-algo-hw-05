# Rabin-Karp algorithm

# Rabin-Karp algorithm

def polynomial_hash(s, base=256, modulus=101):
    """
    Returns the polynomial hash of string s.
    """
    n = len(s)  # Determine the length of string s
    hash_value = 0  # Initialize the hash value
    for i, char in enumerate(s):  # Iterate over each character in string s
        power_of_base = pow(base, n - i - 1) % modulus  # Calculate the power of base modulo modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus  # Update the hash value
    return hash_value  # Return the computed hash value

def rabin_karp_search(main_string, substring):
    # Lengths of the main string and the substring to search
    substring_length = len(substring)  # Length of the substring
    main_string_length = len(main_string)  # Length of the main string
    
    # Base number for hashing and modulus
    base = 256  # Choose the base number for hashing
    modulus = 101  # Choose the modulus for hashing
    
    # Hash values for the substring to search and the current slice in the main string
    substring_hash = polynomial_hash(substring, base, modulus)  # Compute the hash for the substring
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)  # Compute the hash for the first slice of the main string with the length of the substring
    
    # Previous value for recalculating the hash
    h_multiplier = pow(base, substring_length - 1) % modulus  # Determine the multiplier for hash recalculation

    # Iterate through the main string
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:  # If hashes match, check the substring
            if main_string[i:i+substring_length] == substring:  # Check if substrings match
                return i  # If they match, return the index of the start of the substring

        if i < main_string_length - substring_length:  # If there are still characters to check
            # Recalculate the hash for the next slice
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus  # Remove the influence of the first character of the previous slice
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus  # Add the influence of the new character
            if current_slice_hash < 0:  # If the hash is negative, correct it
                current_slice_hash += modulus

    return -1  # If the substring is not found, return -1