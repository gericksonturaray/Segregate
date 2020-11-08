title           : Segregate.py
description     : Implementation of Index of Dissimilarity and Schelling Model
author          : Gerickson Turaray
date_created    : 08112020
version         : 1.0
python_version  : 3.9

NOTE: Limited error trapping. Can check unittest for scenario covered
NOTE: Tried to implement multiple sub tables but run out of time

X - EXIT
L - LOAD DATA - DIR/FILE or STRING
T - ENTER 2 POINTS FOR SUB TABLE
V - VIEW TABLE
C - CLEAR
I - INDEX OF DISSIMILARIRY
S - SCHELLING MODEL

L - LOAD DATA - DIR/FILE or STRING
Can use files (.txt) or string input.
Invalid input will not raise exception BUT will return empty table

Txt file data sample:
  x ooxoxoxo
  xooxoxoxox
  x   xooxox
  oxxxoox xo
  xooxoxoxxo
  xox xxo ox
  xxooxoxoxo
  xo oxooxoo
  oxxxoo oxo
  oooooooxox

String input sample with column count 10:
xxooxoxoxoxooxoxoxoxoxx xooxoxoxxxoox xoxooxoxoxxoxox xxo oxxxooxoxoxoxo oxooxoooxxxoo oxooooooooxox


T - ENTER 2 POINTS FOR SUB TABLE
To create sub tables using the loaded table.
Will need to supply 2 points in the table point1 (x, y) and point2 (x, y)
No error trap yet.


V - VIEW TABLE
Will print the existing loaded data and sub tables


C - CLEAR
Clear loaded data and sub tables


I - INDEX OF DISSIMILARIRY
Compute of index of dissimilarity using the created sub tables
ex:
sub table contains:
  xx
  oo
  xo
  ox
output should be 0.5


S - SCHELLING MODEL
Apply schelling model to the created sub tables
ex:
sub table contains (underscore is space):
  x_o
  xoo
  x__
and threshold is 50 (50%)
output can be:
  xoo          x_o
  x_o    or    x_o
  x__          x_o


X - EXIT
