"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""
# White Box Testing of a1q1.

import a1q1

test_suite = [
    { "inputs": 'sudoku6.txt',
      "outputs": [['1', '2', '3', '3', '2', '1'], ['4', '5', '6', '5', '6', '4'], ['7', '8', '9', '9', '8', '7'],
                    ['1', '2', '3', '3', '2', '1'], ['4', '5', '6', '5', '6', '4'], ['7', '8', '9', '9', '8', '7']]},

    {"inputs": 'sudoku4.txt',
     "outputs": [['1', '2', '3', '3', '2', '1', '1', '2', '3'], ['4', '5', '6', '5', '6', '4', '6', '5', '4'],
                 ['7', '8', '9', '9', '8', '7', '8', '7', '9'], ['1', '2', '3', '3', '2', '1', '1', '2', '3'],
                 ['4', '5', '6', '5', '6', '4', '6', '5', '4'], ['7', '8', '9', '9', '8', '7', '8', '7', '9'],
                 ['1', '2', '3', '3', '2', '1', '1', '2', '3'], ['4', '5', '6', '5', '6', '4', '6', '5', '4'],
                 ['7', '8', '9', '9', '8', '7', '8', '7', '9']]},

    {"inputs": 'sudoku5.txt',
     "outputs": [['1', '2', '3', '3', '2', '1', '1', '2', '3'], ['4', '5', '6', '5', '6', '4', '6', '5', '4'],
                 ['7', '8', '9', '9', '8', '7', '8', '7', '9'], ['1', '2', '3', '3', '2', '1', '1', '2', '3'],
                 ['4', '5', '6', '5', '6', '4', '6', '5', '5'], ['7', '8', '9', '9', '8', '7', '8', '7', '9'],
                 ['1', '2', '3', '3', '2', '1', '1', '2', '3'], ['4', '5', '6', '5', '6', '4', '6', '5', '4'],
                 ['7', '8', '9', '9', '8', '7', '8', '7', '9']]},
]

test_suite_three_by_three = [
    {"inputs": 'sudoku6.txt',
     "outputs": [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['3', '2', '1', '5', '6', '4', '9', '8', '7'],
                 ['3', '2', '1', '5', '6', '4', '9', '8', '7'], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]},

    {"inputs": 'sudoku4.txt',
     "outputs": [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['3', '2', '1', '5', '6', '4', '9', '8', '7'],
                 ['3', '2', '1', '5', '6', '4', '9', '8', '7'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                 ['1', '2', '3', '6', '5', '4', '8', '7', '9'], ['1', '2', '3', '6', '5', '4', '8', '7', '9'],
                 ['1', '2', '3', '6', '5', '4', '8', '7', '9'], ['3', '2', '1', '5', '6', '4', '9', '8', '7'],
                 ['1', '2', '3', '4', '5', '6', '7', '8', '9']]},

    {"inputs": 'sudoku5.txt',
     "outputs": [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['3', '2', '1', '5', '6', '4', '9', '8', '7'],
                 ['3', '2', '1', '5', '6', '4', '9', '8', '7'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                 ['1', '2', '3', '6', '5', '4', '8', '7', '9'], ['1', '2', '3', '6', '5', '5', '8', '7', '9'],
                 ['1', '2', '3', '6', '5', '4', '8', '7', '9'], ['3', '2', '1', '5', '6', '4', '9', '8', '7'],
                 ['1', '2', '3', '4', '5', '6', '7', '8', '9']]},
]

test_suite_bool = [
    { "inputs"  : 'sudoku1.txt',
      "outputs" : True,
      "reason"  : "Since the integers are all less than or equal to N, the sudoku puzzle is valid." },

    { "inputs"  : 'sudoku2.txt',
      "outputs" : False,
      "reason"  : "Since one of the integers is greater than N, the sudoku puzzle is invalid." },

    { "inputs"  : 'sudoku3.txt',
      "outputs" : False,
      "reason"  : "Since the same integer occurs in the sudoku puzzle, the sudoku puzzle is invalid." },

    {"inputs"   : 'sudoku4.txt',
     "outputs"  : True,
     "reason"   : "Since there are different integers in every 3x3, the sudoku puzzle is valid."},

    {"inputs"   : 'sudoku5.txt',
     "outputs"  : False,
     "reason"   : "Since matrix [['1', '2', '3'], ['6', '5', '5'], ['8', '7', '9']] has 5 repeated in it, the sudoku "
                  "puzzle is invalid. "},
]

for test in test_suite:
    inputs = test["inputs"]
    result = a1q1.fnReturnList(inputs)
    if result != test["outputs"]:
        print("Testing fault: a1q1_betaV2.fnPrintList() returned", result, "on inputs", inputs)

for test in test_suite_three_by_three:
    inputs = test["inputs"]
    result = a1q1.fnListSplicer(inputs)
    if result != test["outputs"]:
        print("Testing fault: a1q1_betaV2.fnListSplicer() returned", result, "on inputs", inputs)

for test in test_suite_bool:
    inputs = test["inputs"]
    result = a1q1.fnRead3x3List(inputs)
    if result != test["outputs"]:
        print("Testing fault: a1q1_betaV2.fnRead3x3List() returned", result, "on inputs", inputs, "(",test["reason"],")")