def get_char_frequency(text):
    frequency = {}
    
    # Iterate through every character in the string
    for char in text.lower():
        if 'a' <= char <= 'z': # Only count alphabetic characters
            # If the character is already in the dictionary, increment count
            if char in frequency:
                frequency[char] += 1
            # Otherwise, initialize count to 1
            else:
                frequency[char] = 1
                
    return frequency

# --- Example Usage ---
sentence = "Programming is Fun"
freq = get_char_frequency(sentence)
print(f"Character Frequency: {freq}")
# Expected output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
