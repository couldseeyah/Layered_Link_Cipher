# Layered_Link_Cipher 🔒
Inspired by AES and DES's Feistel Structure architecture.

## Feistel Cipher Implementation 🛡️
### Description 📝
Inspired by AES and DES's Feistel Structure architecture, this project implements a Feistel cipher with 10 rounds. The round function employs a Substitution-Permutation Network (SPN) consisting of 5 sub-steps: 
- S-box (S)
- Column Shuffle (P)
- Shift with Key (S)
- Tilt Rotation (P)
- Row Shift (S)

### Features ✨
- Converts string input to corresponding hexadecimal notation of ASCII characters, as the cipher operates on hex digits.
- Block size: 128 bits
- Key size: 64 bits
- Key generation involves a row shift, column shuffle, and a variation of row shift.
- Decryption of ciphertext to extract original plaintext.

### Usage 🚀
1. Clone the repository:
```sh
git clone https://github.com/couldseeyah/Layered_Link_Cipher.git
```
2. Navigate to the project directory:
```sh
cd Layered_Link_Cipher
```
3. Compile and run the code (test.py).

### Contributors 👥
@couldseeyah
@aleenaahmad1
