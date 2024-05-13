from cipher import layered_link_cipher
from helper_functions import pretty_print


def demonstration(input, key):
    print('INPUT STRING: ', pretty_print(input))
    ciphertext = layered_link_cipher(input, 'encryption', key)
    print('ENCRYPTED STRING: ', pretty_print(ciphertext))
    plaintext = layered_link_cipher(ciphertext, 'decryption', key)
    print('DECRYPTED STRING: ', pretty_print(plaintext))

input = "This is a sample message to test encryption. Going to add random words to make this longer. Hello goodbye information security computer science encrypt decrypt feistel structure sbox . hello kitty. slay. goodbye" 
key = "91b4c5a7e32d806f"

demonstration(input, key)




