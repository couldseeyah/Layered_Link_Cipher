from feistel_structure import feistel
from helper_functions import *
from round_functions import key_generation, round_function
import numpy as np

#ANALYSIS FUNCTIONS

def correlation_coefficient(plaintext, ciphertext):
    """Calculate the correlation coefficient between plaintext and ciphertext."""
    print("PT: ", ciphertext)
    plaintext = int(plaintext, 16)
    ciphertext = int(plaintext, 16)
    print("PT after; ", ciphertext)
    
    plaintext_bin = np.array(list(map(int, plaintext)), dtype=np.float64)
    ciphertext_bin = np.array(list(map(int, ciphertext)), dtype=np.float64)
    correlation = np.corrcoef(plaintext_bin, ciphertext_bin)[0, 1]
    return correlation

def hex_to_binary(hex_string):
    """Convert a hexadecimal string to binary."""
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def hamming_distance(ct1, ct2): #to measure diffusion
    ct1_bin = hex_to_binary(ct1)
    ct2_bin = hex_to_binary(ct2)
    xor_result = int(ct1_bin, 2) ^ int(ct2_bin, 2)
    
    # Count differing bits
    hamming_dist = bin(xor_result).count('1')
    
    return hamming_dist

def check_confusion(PT, key1, key2):
    print('_________________________')
    print('PT: ', PT)
    print('Comparing key1 and key2: ')
    print_string_matches(key1, key2)

    extendedkey1 = []
    extendedkey2 = []
    key_generation(key1, 1, extendedkey1)
    key_generation(key2, 1, extendedkey2)

    ct1 = feistel(PT, extendedkey1, round_function, xor_hex_strings, 'encryption')
    ct2 = feistel(PT, extendedkey2, round_function, xor_hex_strings, 'encryption')

    print('Comparing CT1 and CT2: ')
    print_string_matches(ct1, ct2)
    print("Hamming Distance: ")
    print(hamming_distance(ct1, ct2))
    

def check_diffusion(PT1, PT2, key):
    print('_________________________')
    print('Key: ', key)
    print('Comparing PT1 and PT2: ')
    print_string_matches(PT1, PT2)

    extended_keys = []
    key_generation(key, 1, extended_keys)
    ct1 = feistel(PT1, extended_keys, round_function, xor_hex_strings, 'encryption')
    ct2 = feistel(PT2, extended_keys, round_function, xor_hex_strings, 'encryption')
    
    print('Comparing CT1 and CT2: ')
    print_string_matches(ct1, ct2)
    print('_________________________')

    print("Number of bits changed in input: ", hamming_distance(PT1, PT2))

    print("Hamming Distance: ")
    print(hamming_distance(ct1, ct2))


# ANALYSIS
check_diffusion("1a2b3c4d5e6f798fabcdef1912345678", "1a2b3c4d5e6f798fabcdef1912345679", "91b4c5a7e32d806f") #pt1, pt2, key
check_diffusion("1a2b3c4d5e6f798fabcdef1912345678", "fa2b3c4d5e6f798fabcdef1912345679", "91b4c5a7e32d806f") #pt1, pt2, key
check_diffusion("1a2b3c4d5e6f798fabcdef1912345678", "fa2b3c4d5e6fc98fabc7ef1912345679", "91b4c5a7e32d806f") #pt1, pt2, key
check_diffusion("1a2b3c4d5e6f798fabcdef1912345678", "fa2b3c4d5e6fc98fabb7ef1912345679", "91b4c5a7e32d806f") #pt1, pt2, key


check_confusion("1a2b3c4d5e6f798fabcdef1912345679","91b4c5a7e32d803e", "91b4c5a7e32d806f") #pt, key1, key2
check_confusion("1a2b3c4d5e6f798fabcdef1912345679","91b4c5a7e12d806e", "91b4c5a7e32d806f") #pt, key1, key2
check_confusion("1a2b3c4d5e6f798fabcdef1912345679","a1b4c5a7e12d806e", "91b4c5a7e32d806f") #pt, key1, key2
check_confusion("1a2b3c4d5e6f798fabcdef1912345679","a1b4cfa7e12d806e", "91b4c5a7e32d806f") #pt, key1, key2

