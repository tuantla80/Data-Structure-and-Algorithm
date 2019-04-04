# monkey-map-maker-question
This Python code is to solve a monkey mapmaker question.
There is a monkey which can walk around on a planar grid. The monkey can move one space at a time left, right, up
or down. That is, from (x, y) the monkey can go to (x+1, y), (x-1, y), (x, y+1), and (x, y-1). Points where the
sum of the digits of the absolute value of the x coordinate plus the sum of the digits of the absolute value of
the y coordinate are lesser than or equal to 21 are accessible to the monkey. For example, the point (59, -79)
is inaccessible, because 5 + 9 + 7 + 9 > 21. But the point (-113, -104) is accessible because
1 + 1 + 3 + 1 + 0 + 4 <= 21. How many points can the monkey access if it starts at (0, 0), including (0, 0) itself?
