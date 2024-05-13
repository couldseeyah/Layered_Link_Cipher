import copy
import math

#formatting functions

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def hex_to_dec(hex_digit):
    if hex_digit.isdigit():
        return int(hex_digit)
    else:
        return ord(hex_digit.lower()) - ord('a') + 10

def dec_to_hex(dec_num):
    return format(dec_num, 'x').upper()

def padding(input):
    padding_length = (4 - len(input) % 4) % 4
    input = '0' * padding_length + input
    # input += '0' * padding_length
    return input

#used within round function to match format of fesitel strcture and internal functions
def string_to_matrix(hex_string):
    matrix = []
    for i in range(0, len(hex_string), 4):
        row = []
        for j in range(i, i + 4):
            # Take each character individually
            row.append(hex_string[j].upper())
        matrix.append(row)
    return matrix

#same comment as above
def matrix_to_string(matrix):
    hex_string = ""
    for row in matrix:
        for entry in row:
            hex_string += entry
    return hex_string

#xor for 2 strings, used in fiestel structure
def xor_hex_strings(hex_string1, hex_string2):
    int1 = int(hex_string1, 16)
    int2 = int(hex_string2, 16)
    
    result_int = int1 ^ int2
    
    result_hex_string = format(result_int, 'x')
    
    if len(result_hex_string) % 2 != 0:
        result_hex_string = '0' + result_hex_string
    if len(result_hex_string)<16: 
        padding = 16 - len(result_hex_string)
        result_hex_string = result_hex_string + ('0'*padding)
    
    return result_hex_string

#take string as input, convert ASCII to hex values, divide into blocks and page
def string_encryption(input_text):
    hex_values = [hex(ord(letter))[2:].upper() for letter in input_text] #ord -> converts to ascii, then converted to hex
    hex_string = "".join([str(item) for item in hex_values])
    number_of_blocks = math.ceil(len(hex_string)/32)
    remaining_digits = len(hex_string)%32
    padding = (32 - remaining_digits)%32
    blocks = []
    for i in range(number_of_blocks): #0,1
        start = i*32
        end = start+32
        if(end>len(hex_string)):
            end = start + remaining_digits
        blocks.append(hex_string[start:end])
    padded = '2C'*(padding//2)
    blocks[number_of_blocks-1] = blocks[number_of_blocks-1]+padded
    return blocks

#used only in decryption, since no padding required (input already has length n*32)
def divide_into_blocks(hex_string):
    number_of_blocks = math.ceil(len(hex_string) / 32)
    blocks = []
    for i in range(number_of_blocks):
        start = i * 32
        end = min(start + 32, len(hex_string))
        block = hex_string[start:end]
        blocks.append(block)
    return blocks

def string_decryption(hex_plaintext):
    #remove '2C' from end of string
    while hex_plaintext.endswith("2C"):
        hex_plaintext = hex_plaintext[:-2]

    text = ""

    for i in range(0, len(hex_plaintext)-1,2):
        num = hex_plaintext[i] + hex_plaintext[i+1]
        num = int(num, 16)
        character = chr(num)
        text += character

    return text

def print_string_matches(string1, string2):
    if len(string1) != len(string2):
        print("Strings are not of the same length")
        return
    new_string = ""
    different = 0
    for i in range(len(string1)): 
        if (string1[i] == string2[i]):
            new_string+=string1[i]
        else:
            new_string+='X'
            different+=1
    print("Matches found: ", new_string, "Number of differences: ", different)

def pretty_print(text, max_line_length=80):
    lines = []
    current_line = ""
    for word in text.split():
        if len(current_line) + len(word) + 1 <= max_line_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return "\n".join(lines)

#PERMUTATION FUNCTIONS 

def column_transposition(matrix):
    new_matrix = [["0" for col in range(4)] for row in range(4)]
    for i in range(4):
        first_value = int(matrix[0][i], 16)
        second_value = int(matrix[1][i], 16)
        third_value = int(matrix[2][i], 16)
        fourth_value = int(matrix[3][i], 16)
        shift = ((first_value + second_value) * (third_value + fourth_value)) % 4 #can change mod to 3 later
        for j in range(4):
            new_matrix[(j + shift) % 4][i] = matrix[j][i]
    return new_matrix

def tilt_rotation(matrix):
    new_matrix = copy.deepcopy(matrix)

    #internal right tilt
    new_matrix[1][2] = matrix[1][1]
    new_matrix[1][1] = matrix[2][1] 
    new_matrix[2][2] = matrix[1][2] 
    new_matrix[2][1] = matrix[2][2] 

    #external left shift
    for i in range(1,4):
        new_matrix[0][i-1] = matrix[0][i]
        new_matrix[3][i] = matrix[3][i-1]
        
    for i in range(1,4):
        new_matrix[i-1][3] = matrix[i][3]
        new_matrix[i][0] = matrix[i-1][0]

    return new_matrix

def four_element_transposition(pt_matrix):
    matrix = copy.deepcopy(pt_matrix)
    shift = 1
    for i in range(len(pt_matrix)):
        first_value = bin(int(pt_matrix[i][0], 16))[2:]
        second_value = bin(int(pt_matrix[i][1], 16))[2:]
        third_value = bin(int(pt_matrix[i][2], 16))[2:]
        fourth_value = bin(int(pt_matrix[i][3], 16))[2:]
        value = padding(first_value) + padding(second_value) + padding(third_value) + padding(fourth_value)

        shifted_string = value[shift % len(value):] + value[:shift % len(value)]
        #split binary string into four sets and convert to hex and assign to matrix
        matrix[i][0] = hex(int(shifted_string[:4], 2))[2:] 
        matrix[i][1] = hex(int(shifted_string[4:8], 2))[2:]
        matrix[i][2] = hex(int(shifted_string[8:12], 2))[2:]
        matrix[i][3] = hex(int(shifted_string[12:], 2))[2:]

    return matrix

def element_transposition(pt_matrix):
    matrix = copy.deepcopy(pt_matrix)
    shift = 1
    for i in range(len(pt_matrix)):
        for j in range(0,len(pt_matrix[i])-1, 2):
            first_value = bin(int(pt_matrix[i][j], 16))[2:]
            second_value = bin(int(pt_matrix[i][j+1], 16))[2:]
            value = padding(first_value) + padding(second_value)

            shifted_string = value[shift % len(value):] + value[:shift % len(value)]
            new_first_val = hex(int(shifted_string[:4], 2))[2:] #split binary string into two and convert to hex
            new_second_val = hex(int(shifted_string[4:], 2))[2:]

            shift += 1
            if shift == 4:
                shift = 1
            matrix[i][j] = new_first_val
            matrix[i][j+1] = new_second_val
    return matrix


#SUBSTITUTION FUNCTIONS

def sbox(x):
    x_numeric = hex_to_dec(x)
    ans = ((23 - x_numeric)^3 - 8*x_numeric)%16
    ans = dec_to_hex(ans)
    return ans

def substitution(pt_matrix):
    matrix = copy.deepcopy(pt_matrix)
    for i in range(len(pt_matrix)):
        for j in range(len(pt_matrix[i])): 
            matrix[i][j] = sbox(pt_matrix[i][j])
    return matrix

def shift_with_key(key, pt_matrix):
    new_matrix = copy.deepcopy(pt_matrix)
    for i in range(len(key)):
        for j in range(len(key[i])):
            shift_val = int(key[i][j], 16) + int(key[(i+1)%4][j], 16) + int(key[(i+2)%4][j], 16)
            new_matrix[i][j] = (int(new_matrix[i][j], 16) + shift_val) % 16 
            new_matrix[i][j] = format(new_matrix[i][j], 'x').upper()
    return new_matrix