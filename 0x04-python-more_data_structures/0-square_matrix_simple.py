#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []

    # iterate over each row in the given matrix

    for row in matrix:
        # create a new row to store squared values
        squared_row = []

        for element in row:
            squared_row.append(element ** 2)

        # append the squared row to the squared_matrix
        squared_matrix.append(squared_row)

    return (squared_matrix)
