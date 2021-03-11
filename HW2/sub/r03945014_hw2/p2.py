import numpy as np
from util import mod_inv

def get_key(cipher, plain):
    '''
    Calculate public key with cipher text and plain text.

    Arguments:
        cipher: str, cipher text
        plain: str, plain text

    Return:
        key: str, public key
    '''
    np_cipher = reshape_into_int_numpy_array(cipher)
    np_plain = reshape_into_int_numpy_array(plain)
    key = np.mod(np_cipher @ mod_inv(np_plain), 31)
    return reshape_numpy_array_into_public_key(key)

def character_mapping(c):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    return letters.index(c)

def reshape_into_int_numpy_array(cipher):
    '''
    Arguments:
        cipher: str,
        example: C!QER,YNR
    
    Return:
        key: Numpy.array[int],
        example: 
            [[ 2  4 24]
            [30 17 13]
            [16 28 17]]
    '''
    cipher = [character_mapping(c) for c in list(cipher)]
    return np.reshape(cipher, (-1, 3)).T

def reshape_numpy_array_into_public_key(numpy_array):
    '''
    Arguments:
        numpy_array: str,
        example:
            [[25  8 25]
            [ 9  9 16]
            [28 21 18]]
    
    Return:
        key: string,
        example: 
            25 8 25 9 9 16 28 21 18
    '''
    return ' '.join([str(i) for i in numpy_array.reshape(-1)])