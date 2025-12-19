def caesar(text, shift, encrypt=True):
    """
    Applies a Caesar Cipher to the given text.

    Parameters:
    text (str): The input text to encrypt or decrypt
    shift (int): Number of positions to shift the alphabet (1–25)
    encrypt (bool): True for encryption, False for decryption

    Returns:
    str: The encrypted or decrypted text
    """

    # Validate that shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate that shift is within the allowed Caesar Cipher range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Base alphabet used for the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Reverse the shift direction when decrypting
    if not encrypt:
        shift = -shift

    # Create the shifted alphabet using slicing
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create a translation table that maps:
    # lowercase → lowercase shifted
    # uppercase → uppercase shifted
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the input text using the translation table
    encrypted_text = text.translate(translation_table)

    return encrypted_text


def encrypt(text, shift):
    """
    Encrypts text using the Caesar Cipher.
    """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Decrypts text using the Caesar Cipher.
    """
    return caesar(text, shift, encrypt=False)


# Example usage
encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)
