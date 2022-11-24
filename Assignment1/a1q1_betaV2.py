"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

def fnReturnList(input_file):
    """
    Purpose:
        Defines a function that reads the input file and executes a list of lists of strings.

    Pre-Conditions:
        input_file: An input file with the sudoku puzzle.

    Post-Conditions:
        Converts the input file to a list of strings.

    Return Values:
        A list of strings.
    """
    f = open(input_file, 'r')
    list_of_integers = []
    next(f)
    for line in f:
        new_line = line.rstrip().split()
        list_of_integers.append(new_line)
    return list_of_integers

def fnPrint3x3from9x9Matrix(input_file):
    """
    Purpose:
        Takes a 9x9 sudoku puzzle and splits it into individual 3x3 matrices.

    Pre-Conditions:
        input_file: An input file with the sudoku puzzle.

    Post-Conditions:
        Splits the incoming 9x9 sudoku puzzle from the input file into 3x3 individual matrices.

    Return Values:
        9 (3x3) Matrices of strings.
    """
    nine_by_nine_list = fnReturnList(input_file)
    three_by_three_list_top_left = []
    three_by_three_list_top_mid = []
    three_by_three_list_top_right = []
    three_by_three_list_mid_left = []
    three_by_three_list_mid_mid = []
    three_by_three_list_mid_right = []
    three_by_three_list_bottom_left = []
    three_by_three_list_bottom_mid = []
    three_by_three_list_bottom_right = []
    i = 0
    for line in nine_by_nine_list:
        i += 1
        if i <= 3:
            three_by_three_list_top_left.append(line[0:3])
            three_by_three_list_top_mid.append(line[3:6])
            three_by_three_list_top_right.append(line[6:9])
        if i > 3 and i <= 6:
            three_by_three_list_mid_left.append(line[0:3])
            three_by_three_list_mid_mid.append(line[3:6])
            three_by_three_list_mid_right.append(line[6:9])
        if i > 6 and i <= 9:
            three_by_three_list_bottom_left.append(line[0:3])
            three_by_three_list_bottom_mid.append(line[3:6])
            three_by_three_list_bottom_right.append(line[6:9])
        if i == 10:
            break
    three_by_three_list = []
    three_by_three_list.append(three_by_three_list_top_left)
    three_by_three_list.append(three_by_three_list_top_mid)
    three_by_three_list.append(three_by_three_list_top_right)
    three_by_three_list.append(three_by_three_list_mid_left)
    three_by_three_list.append(three_by_three_list_mid_mid)
    three_by_three_list.append(three_by_three_list_mid_right)
    three_by_three_list.append(three_by_three_list_bottom_left)
    three_by_three_list.append(three_by_three_list_bottom_mid)
    three_by_three_list.append(three_by_three_list_bottom_right)
    return three_by_three_list

def fnRead3x3List(input_file):
    """
    Purpose:
        Define a function that checks each 3x3 portion of the sudoku puzzle if there is any duplicates.

    Pre-Conditions:
        input_file: An input file.

    Post-Conditions:
        (None).

    Return Values:
        True or False.
    """
    list_of_integers = fnPrint3x3from9x9Matrix(input_file)
    for row in list_of_integers:
        for i in row:
            if int(i) < 0 or int(i) > 9:
                return False
    return True