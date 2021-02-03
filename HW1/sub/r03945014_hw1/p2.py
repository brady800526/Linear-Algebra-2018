from scipy.sparse import *
import numpy as np


def p2_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  1  0  0  0  0
            1  0  0  0  0  0  0
            2  0  0  0  1  0  0
            3  0  0  0  0  0  1
            4  0  1  0  0  0  0
            5  0  0  1  0  0  0
        The size of the matrix is (6,6)
    '''
    return scipy_cycle_detection(sets)
    return numpy_cycle_detection(sets)

def scipy_cycle_detection(sets):

    # Transfer from list to numpy array
    # m for saving original matrix, n for saving matmul result
    m = csr_matrix(sets)
    n = m

    # Multiply at most len of rows times
    for _ in range(len(sets)):
        n = m.dot(n)

        # Terminate if any diagonal value greater than 1
        if any(n.diagonal()): return True

    return False

def numpy_cycle_detection(sets):

    # Transfer from list to numpy array
    # m for saving original matrix, n for saving matmul result
    m = np.array(sets)
    n = m

    # Multiply at most len of rows times
    for _ in range(len(sets)):
        n = np.matmul(m, n)

        # Terminate if any diagonal value greater than 1
        if any(n.diagonal()): return True

    return False

if __name__ == '__main__':
    print(p2_has_cycle([
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]))