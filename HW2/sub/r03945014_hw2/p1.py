import numpy as np
from util import mod_inv


def decode(cipher, key):
    '''
    Decode cipher with public key.

    Arguments:
        cipher: str, cipher text
        key: str, public key

    Return:
        plain: str, plain text
    '''
    cipher = reshape_into_int_numpy_array(cipher)
    private_key = public_key_to_private_key(key)
    np_ans = np.mod(private_key @ cipher, 31)
    return reshape_numpy_array_in_int_to_plain(np_ans)

def character_mapping(c):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    return letters.index(c)

def number_mapping(i):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    return letters[i]

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


def public_key_to_private_key(key):
    '''
    Transform public key string
    into int type 3*3 numpy array.

    Arguments:
        key: str,
        public key,
        example: 25 8 25 9 9 16 28 21 18
    
    Return:
        np_private_key: NumPy.array[int],
        example: 
            [[ 5 27 19]
            [21 25  2]
            [28 27 25]]
    '''
    numpy_array = np.reshape([int(c) for c in key.split()], (3, 3))
    return mod_inv(numpy_array)

def reshape_numpy_array_in_int_to_plain(np_ans):
    '''
    Arguments:
        numpy_array: Numpy.array[int],
        example:
            [[ 8 19 19]
            [18  7 26]
            [26  0 22]]
    
    Return:
        plain: str,
        example: 
            IS_THAT_W
    '''
    return ''.join([number_mapping(i) for i in np_ans.T.reshape(-1)])
    