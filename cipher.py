from round_functions import *
from helper_functions import *
from feistel_structure import feistel

def layered_link_cipher(input, mode, key):
    extended_keys = []
    key_generation(key, 1, extended_keys)
    if mode=='encryption':
        blocks = string_encryption(input)
        ciphertexts = []
        for i in blocks:
            ciphertexts.append(feistel(i,extended_keys, round_function, xor_hex_strings, 'encryption'))
        ciphertext = ''.join(ciphertexts)
        return ciphertext
    
    elif mode=='decryption':
        ciphertexts = divide_into_blocks(input)
        plaintexts = []
        for i in ciphertexts:
            plaintexts.append(feistel(i,extended_keys, round_function, xor_hex_strings, 'decryption'))
            plaintext = ''.join(plaintexts)
            plaintext = string_decryption(plaintext)
        return plaintext
