import copy
from round_functions import round_function

def feistel(input, round_keys, round_function, xor_function, mode):
    keys = copy.deepcopy(round_keys)
    if mode=='decryption':
        keys.reverse()
    input = input.upper()
    # Perform Feistel rounds
    for round_key in keys:
        left_half = input[:int(len(input)/2)]
        right_half = input[int(len(input)/2):]
        
        new_left_half = right_half[:] #right half becomes new left half

        # right half -> round func + XOR 
        new_right_half = round_function(right_half, round_key)
        new_right_half = xor_function(left_half, new_right_half)

        input = new_left_half + new_right_half

    output = input[int(len(input)/2):] + input[:int(len(input)/2)]
    if mode=='decryption':
        output = output.upper()
    return output