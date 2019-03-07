#!/usr/bin/env python3

# Rotate Matrix: Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# (an you do this in place?)
# Hints: #51, #100

ROW = 3
COLUMN = 3


def rotate90(arr):
    ''' Rotate Matrix 90 clockwise '''
    for i in range(ROW):
        for j in range(i, COLUMN):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
    return arr


def printMatrix(arr):
    for i in range(ROW):
        for j in range(COLUMN):
            print(str(arr[i][j]), end=' ')
        print()


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate90(arr)
    printMatrix(arr)

    # [7, 4, 1]
    # [8, 5, 2]
    # [9, 6, 3]
