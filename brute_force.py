from feistel_structure import feistel
from round_functions import round_function, key_generation
from helper_functions import xor_hex_strings
import time

def brute_force_attack(known_plaintext, known_ciphertext):
    start_time = time.time()

    # Iterate through all possible keys (16 hexadecimal numbers)
    for i in range(16**16):
        if (i%1000==0):
          print(i, " keys checked")
        # Convert the current key index to a hexadecimal string of length 16
        current_key = format(i, 'x').zfill(16)

        # Encrypt the known plaintext using the current key
        allkeys=[]
        key_generation(current_key, 1, allkeys)
        current_ciphertext = feistel(known_plaintext, allkeys, round_function, xor_hex_strings, 'encryption')

        # Compare the resulting ciphertext with the known ciphertext
        if current_ciphertext == known_ciphertext:
            end_time = time.time()
            execution_time = end_time - start_time
            return current_key, execution_time

    return None, None  # If no match is found

# Example usage:
input = "1a2b3c4d5e6f798fabcdef1912345678"
key = '91b4c5a7e32d806f'
extendedkeys = []
key_generation(key, 1, extendedkeys)

ciphertext = feistel(input, extendedkeys, round_function, xor_hex_strings, 'encryption')
found_key, execution_time = brute_force_attack(input, ciphertext)
print("Found key:", found_key)
print("Execution time:", execution_time, "seconds")
