
"""
CHALLENGE DESCRIPTION:
Microsoft Excel uses a special convention to name its column headers. The first 26 columns use the letters 'A' to 'Z'. Then, Excel names its column headers using two letters, so that the 27th and 28th column are 'AA' and 'AB'. After 'ZZ', Excel uses three letters.

Write a function that takes as input the number of the column, and returns its header. The input will not ask for a column that would be greater than 'ZZZ'.

INPUT SAMPLE:
The first argument is a path to a file. Each line of the input file contains one test case represented by one integer.
  
1
2
52
3702

OUTPUT SAMPLE:
For each test case your program must print one line containing the Excel column heading corresponding to the integer in the input.
  
1
2
AZ
ELJ

CONSTRAINTS:
1.	The number of test cases is 40.
2.	The input will not ask for a column that would be greater than 'ZZZ'.
"""