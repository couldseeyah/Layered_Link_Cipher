import math
from helper_functions import *

#round function
def round_function(str_input, key):
    intermediate = string_to_matrix(str_input)
    intermediate = substitution(intermediate) #substitution
    intermediate = column_transposition(intermediate) #transposition
    intermediate = shift_with_key(intermediate,key) #substitution
    intermediate = tilt_rotation(intermediate) #transposition
    intermediate = four_element_transposition(intermediate) #substitution
    result = matrix_to_string(intermediate)
    return result

#KEY GENERATION
def key_generation(key, round, extendedkeys):
    if (round == 11):
        return 
    if (round==1):
        key = string_to_matrix(key)
    round_key = four_element_transposition(key) #substitution
    round_key = column_transposition(round_key) #transposition
    round_key = element_transposition(round_key) #substitution
    extendedkeys.append(round_key)
    key_generation(round_key, round+1, extendedkeys)
