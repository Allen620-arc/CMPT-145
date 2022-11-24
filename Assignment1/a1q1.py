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
    f = open(input_file, 'r')  # Opens the incoming file.
    list_of_integers = []  # Initializes a list of integers.
    next(f)  # Skips over the first integer.
    for line in f:
        new_line = line.rstrip().split()  # Strips every line of whitespace and commas.
        list_of_integers.append(new_line)  # Adds the stripped line into the list of integers.
    return list_of_integers

def fnListSplicer(input_file):
    """
    Purpose:
        Takes a 9x9 sudoku puzzle and splits it into its 3x3 integers.

    Pre-Conditions:
        input_file: An input file with the sudoku puzzle.

    Post-Conditions:
        Splits the incoming 9x9 sudoku puzzle from the input file into 3x3 individual matrices.

    Return Values:
        A list of lists with the individual strings of integers from the sudoku puzzle file.
    """
    nine_by_nine_list = fnReturnList(input_file)  # Stores the input sudoku file into a 9x9 list of lists.
    three_by_three_list_top_left = []  # Initializes a 3x3 list of lists with the integers of the top left sudoku file.
    three_by_three_list_top_mid = []  # Initializes a 3x3 list of lists with the integers of the top mid sudoku file.
    three_by_three_list_top_right = []  # Initializes a 3x3 list of lists with the integers of the top right sudoku
    # file.
    three_by_three_list_mid_left = []  # Initializes a 3x3 list of lists with the integers of the mid left sudoku file.
    three_by_three_list_mid_mid = []  # Initializes a 3x3 list of lists with the integers of the mid mid sudoku file.
    three_by_three_list_mid_right = []  # Initializes a 3x3 list of lists with the integers of the mid right sudoku
    # file.
    three_by_three_list_bottom_left = []  # Initializes a 3x3 list of lists with the integers of the bottom left
    # sudoku file.
    three_by_three_list_bottom_mid = []  # Initializes a 3x3 list of lists with the integers of the bottom mid sudoku
    # file.
    three_by_three_list_bottom_right = []  # Initializes a 3x3 list of lists with the integers of the bottom right
    # sudoku file.
    i = 0  # Initializes a counter.
    for line in nine_by_nine_list:  # For every line in the 9x9 list of lists.
        i += 1 # Counts one for every iteration.
        if i <= 3:  # When the counter is less than 3, concatenate the top values of the sudoku puzzle in their
            # respective lists.
            three_by_three_list_top_left.append(line[0:3])
            three_by_three_list_top_mid.append(line[3:6])
            three_by_three_list_top_right.append(line[6:9])
        if 3 < i <= 6:  # When the counter is greater than 3 but less than 6, concatenate the top values of the
            # sudoku puzzle in their respective lists.
            three_by_three_list_mid_left.append(line[0:3])
            three_by_three_list_mid_mid.append(line[3:6])
            three_by_three_list_mid_right.append(line[6:9])
        if 6 < i <= 9: # When the counter is greater than 6 but less than 9, concatenate the top values of the
            # sudoku puzzle in their respective lists.
            three_by_three_list_bottom_left.append(line[0:3])
            three_by_three_list_bottom_mid.append(line[3:6])
            three_by_three_list_bottom_right.append(line[6:9])
        if i == 10:  # When the counter is 10, the for loop stops.
            break
    three_by_three_list = []  # The list of integers from the sudoku puzzle.
    three_by_three_TL = three_by_three_list_top_left[0] + three_by_three_list_top_left[1] + \
                        three_by_three_list_top_left[2]  # The top left corner of the sudoku puzzle.
    three_by_three_list.append(three_by_three_TL)
    if i > 3:  # If the counter is greater than three, then it takes the surrounding 3x3 sudoku puzzles.
        three_by_three_TM = three_by_three_list_top_mid[0] + three_by_three_list_top_mid[1] + \
                            three_by_three_list_top_mid[2]
        three_by_three_list.append(three_by_three_TM)
        three_by_three_MM = three_by_three_list_mid_mid[0] + three_by_three_list_mid_mid[1] + \
                            three_by_three_list_mid_mid[2]
        three_by_three_list.append(three_by_three_MM)
        three_by_three_ML = three_by_three_list_mid_left[0] + three_by_three_list_mid_left[1] + \
                            three_by_three_list_mid_left[2]
        three_by_three_list.append(three_by_three_ML)
    if i > 6: #If the counter is greater than six, then it takes the surrounding 3x3 sudoku puzzles.
        three_by_three_TR = three_by_three_list_top_right[0] + three_by_three_list_top_right[1] + \
                            three_by_three_list_top_right[2]
        three_by_three_list.append(three_by_three_TR)
        three_by_three_MR = three_by_three_list_mid_right[0] + three_by_three_list_mid_right[1] + \
                            three_by_three_list_mid_right[2]
        three_by_three_list.append(three_by_three_MR)
        three_by_three_BR = three_by_three_list_bottom_right[0] + three_by_three_list_bottom_right[1] + \
                            three_by_three_list_bottom_right[2]
        three_by_three_list.append(three_by_three_BR)
        three_by_three_BM = three_by_three_list_bottom_mid[0] + three_by_three_list_bottom_mid[1] + \
                            three_by_three_list_bottom_mid[2]
        three_by_three_list.append(three_by_three_BM)
        three_by_three_BL = three_by_three_list_bottom_left[0] + three_by_three_list_bottom_left[1] + \
                            three_by_three_list_bottom_left[2]
        three_by_three_list.append(three_by_three_BL)
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
    list_of_integers = fnListSplicer(input_file)
    for row in list_of_integers:
        for i in row:
            if int(i) < 0 or int(i) > 9:  # If the integer is less than 0 or greater than 9, then return false.
                return False
        if row[0] == row[2]:  # If the integer in the area where row at 0 is the same where row at 2, then return false.
            return False
        if row[4] == row[5]:  # If the integer in the area where row at 4 is the same where row at 5, then return false.
            return False
    return True  # Return true otherwise.
