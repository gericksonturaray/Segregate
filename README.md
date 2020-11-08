NOTE: Limited error trapping. Can check unittest for scenario covered\
NOTE: Tried to implement multiple sub tables but run out of time\

**X - EXIT**\
**L - LOAD DATA - DIR/FILE or STRING**\
**T - ENTER 2 POINTS FOR SUB TABLE**\
**V - VIEW TABLE**\
**C - CLEAR**\
**I - INDEX OF DISSIMILARIRY**\
**S - SCHELLING MODEL**<br><br>

**L - LOAD DATA - DIR/FILE or STRING**\
Can use files (.txt) or string input\
Invalid input will not raise exception BUT will return empty table<br><br>

Txt file data sample:\
x_ooxoxoxo\
xooxoxoxox\
x___xooxox\
oxxxoox_xo\
xooxoxoxxo\
xox_xxo_ox\
xxooxoxoxo\
xo_oxooxoo\
oxxxoo_oxo\
oooooooxox<br><br>

String input sample with column count 10:\
xxooxoxoxoxooxoxoxoxoxx xooxoxoxxxoox xoxooxoxoxxoxox xxo oxxxooxoxoxoxo oxooxoooxxxoo oxooooooooxox<br><br><br>


**T - ENTER 2 POINTS FOR SUB TABLE**\
To create sub tables using the loaded table\
Will need to supply 2 points in the table point1 (x, y) and point2 (x, y)\
No error trap yet<br><br><br>


**V - VIEW TABLE**\
Will print the existing loaded data and sub tables<br><br><br>


**C - CLEAR**\
Clear loaded data and sub tables<br><br><br>


**I - INDEX OF DISSIMILARIRY**\
Compute of index of dissimilarity using the created sub tables\
ex:\
sub table contains:\
xx\
oo\
xo\
ox\
output should be 0.5<br><br><br>


**S - SCHELLING MODEL**\
Apply schelling model to the created sub tables\
ex:\
sub table contains (underscore is space):\
x_o\
xoo\
x__\
and threshold is 50 (50%)\
output can be:\
xoo\
x_o\
x__<br><br>
or<br><br>
x_o\
x_o\
x_o<br><br><br>

**X - EXIT**
