#!/usr/bin/python
import sys
import csv

def sudoku_display(sudoku):
    for row in sudoku:
        print ",".join(map(str,row))

def sudoku_try(sudoku, i, j, candidate):
    # Check row for dupilcates
    for row in xrange(0, 9):
        if (sudoku[row][j] == candidate):
            return False
    # Check Column for duplicates
    for column in xrange(0, 9):
        if (sudoku[i][column] == candidate):
            return False
    # Check 9-grid for duplicates
    row = i/3*3;
    column = j/3*3;
    for r in xrange(row, row+3):
        for c in xrange(column, column+3):
            if (sudoku[r][c] == candidate):
                return False
    return True 

# Try searching top to bottom, left to right
def sudoku_solve(sudoku, i, j):
    # Skip to the next zero position
    # if current position is given
    while(sudoku[i][j] != 0):
        if j != 8:
            j = j+1
        else:
            j = 0
            i = i+1
            if i == 9:
                # Every position is filled. Done.
                return True

    # sudoku[i][j] must now be zero 
    # we need to try 
    for candidate in xrange(1, 10):
       # if candidate is OK, keep searching
       if sudoku_try(sudoku, i, j, candidate):
           sudoku[i][j] = candidate
           if sudoku_solve(sudoku, i, j):
               return True
    sudoku[i][j] = 0

    return False

def sudoku_readfile(filename):
    # print 'Reading sudoku from:', filename
    sudoku_csv = csv.reader(filename, delimiter=',');

    # Empty 9x9 
    sudoku = [[0]*9 for i in range(9)]

    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=",")
        array = []
        for row in csv_reader:
            array.append(row)
        sudoku = [map(int, x) for x in array]
        return sudoku

if __name__ == "__main__":
    if (len(sys.argv) == 2): 
        sudoku = sudoku_readfile(sys.argv[1])
        # print("Input:")
        # sudoku_display(sudoku)
        solved = sudoku_solve(sudoku, 0, 0)
        sudoku_display(sudoku)
        if not solved:
            print("Unable to solve.")
    else:
        print 'Usage: %s <sudoku file>' % sys.argv[0]
         
