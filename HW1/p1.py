from scipy.sparse import *
import numpy as np


def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  0 -1  1  0  0
            1  0  1  0  0 -1  0
            2  0  0  0 -1  0  1
            3  0  0  1  0  0 -1
            4 -1  1  0  0  0  0
        The size of the matrix is (5,6)
    '''
    # return numpy_cycle_detection(sets)
    return scipy_cycle_detection(sets)
    
def scipy_cycle_detection(sets):

    # Transfer from list to scipy sparse matrix
    m = csr_matrix(sets)

    # If only one edge left, termiate the while loop
    while m.get_shape()[0] >= 1:

        # Find the value 1 position in first row
        first_row = m[0]
        col_index = first_row.argmax()

        # Find the value -1 rows indexes on found col
        # Append the addition of first row and founded rows to matrix
        selected_row_indexes = m.getcol(col_index)
        selected_row_indexes = selected_row_indexes.toarray().flatten()
        for row in [idx for idx, value in enumerate(selected_row_indexes) if value == -1]:
            m = vstack([m, first_row + m.getrow(row)])

        # Remove first row
        m = m[1:]

        # Termiate the calculate if ALL 0 rows is found
        # By compare if nonzero rows length equals to matrix row number 
        r, c = m.nonzero()
        if set(r.tolist()) != set(range(m.get_shape()[0])): return True

    return False

def numpy_cycle_detection(sets):

    # Transfer from list to numpy array
    m = np.array(sets)

    # If only one edge left, termiate the while loop
    while len(m) >= 1:

        # Find the value 1 position in first row
        first_row = m[0]
        col_index = np.where(first_row == 1)

        # Find the value -1 rows indexes on found col
        # Append the addtion of first row and founded rows
        selected_row_indexes = np.where(m[:, col_index[0][0]] == -1)
        for row in selected_row_indexes[0]:
            m = np.vstack((m, [first_row + m[row]]))
        
        # Remove first row
        m = m[1:]

        # Termiate the calculate if ALL 0 rows is found
        if np.any(np.all((m == 0), axis=1)): return True 

    return False

if __name__ == '__main__':
    print(p1_has_cycle([
        [0, 1, -1, 0],
        [1, -1, 0, 0],
        [-1, 0, 1, 0],
        [0, -1, 0, 1],
    ]))