class MapMaker(object):
    """
    This class is to solve a question as below.

    QUESTION:
    --------
    There is a monkey which can walk around on a planar grid. The monkey can move one space at a time left, right, up
    or down. That is, from (x, y) the monkey can go to (x+1, y), (x-1, y), (x, y+1), and (x, y-1). Points where the
    sum of the digits of the absolute value of the x coordinate plus the sum of the digits of the absolute value of
    the y coordinate are lesser than or equal to 21 are accessible to the monkey. For example, the point (59, -79)
    is inaccessible, because 5 + 9 + 7 + 9 > 21. But the point (-113, -104) is accessible because
    1 + 1 + 3 + 1 + 0 + 4 <= 21. How many points can the monkey access if it starts at (0, 0), including (0, 0) itself?

    Version: 0.0
    Date: 180304
    Author: TLA. Tuan
    """
    def __init__(self, start_point=[(0, 0)], value_limit=21):
        """
        Parameters:
        ----------
        start_point: a Monkey's starting coordinate (x,y). ex. [(0, 0)]
        value_limit:
            if sum of the absolute value of the coordinate's digits is LESS THAN or EQUAL value_limit, it is accessible,
            else: it is inaccessible.
        self.moving_points: a list of coordinate (x,y) that Monkey can move. ex. [(0, 1), (0, -1),...]
        self.accessible_points: a set of accepted coordinates that is accessible. ex. {(0, 1), (0, -1),...}
        self.value_limit: refer to value_limit
        """
        assert isinstance(start_point, list), ("Expected a list but found %s with type: %s." \
                                               % (start_point, type(start_point)))
        assert isinstance(value_limit, int), ("Expected an integer number but found %s with type: %s." \
                                              % (value_limit, type(value_limit)))

        self.moving_points = start_point
        self.accessible_points = set()
        self.value_limit = value_limit


    @staticmethod
    def sum_digits_of_integer_number(number):
        """
        To compute the sum of digits of an integer number.

        Parameters:
        ----------
        number: an integer number

        Returns
        -------
        sum: an integer number

        Examples
        --------
        >>> _sum = sum_digits_of_integer_number(number=59)
        >>> _sum
        14
        """
        assert isinstance(number, int), ("Expected an integer number but found %s with type: %s." \
                                         % (number, type(number)))

        return sum([int(digit) for digit in str(abs(number))])


    def check_accessible_point(self, x, y):
        """
        To compute the sum of digits of an integer number x and y.
        If this sum is LESS THAN or EQUAL value_limit, return True (it is accessible),
        Else: return False (it is inaccessible).

        Parameters:
        ----------
        x: an integer number
        y: an integer number
        self.value_limit: an integer number

        Returns
        -------
        True or False

        Examples
        --------
        >>> map_maker = MapMaker(start_point=[(0, 0)], value_limit=21)
        >>> flag_check_accessible_point = map_maker.check_accessible_point(x=59, y=-79)
        >>> flag_check_accessible_point
        False

        >>> flag_check_accessible_point = map_maker.check_accessible_point(x=-113, y=-104)
        >>> flag_check_accessible_point
        True
        """
        assert isinstance(x, int), ("Expected an integer number but found %s with type: %s." % (x, type(x)))
        assert isinstance(y, int), ("Expected an integer number but found %s with type: %s." % (y, type(y)))

        if (self.sum_digits_of_integer_number(x) + self.sum_digits_of_integer_number(y) <= self.value_limit):
            return True
        else:
            return False


    def search(self):
        """
        To search all possible points that Monkey can access based on the conditions given in the question above.
        - [Current version] Version 0.0: Search all the possible cases.
        - To reduce the computational time, one may use the symmetry of the problem to search only in one quadrant with
        a consideration of the overlapping points in axes. Moreover, it is also have a symmetry in y=x line, therefore,
        the problem can reduce further to solve only in one octant.

        Parameters:
        ----------
        self.moving_points
        self.accessible_points

        Returns
        -------
        A number of accessible points.

        Examples
        --------
         >>> number_of_accessible_points = MapMaker(start_point=[(0, 0)], value_limit=0).search()
         >>> number_of_accessible_points
         1
         >>> number_of_accessible_points = MapMaker(start_point=[(0, 0)], value_limit=1).search()
         >>> number_of_accessible_points
         5
         >>> number_of_accessible_points = MapMaker(start_point=[(0, 0)], value_limit=2).search()
         >>> number_of_accessible_points
         13
         >>> number_of_accessible_points = MapMaker(start_point=[(0, 0)], value_limit=21).search()
         >>> number_of_accessible_points
         287881
        """

        while self.moving_points:
            point = self.moving_points.pop()
            if not point in self.accessible_points:
                self.accessible_points.add(point)
                _x, _y = point
                new_points = [(_x - 1, _y), (_x + 1, _y), (_x, _y - 1), (_x, _y + 1)]
                self.moving_points += [(x,y) for (x,y) in new_points if self.check_accessible_point(x,y)]
            else:
                pass
        return len(self.accessible_points)


def test_map_maker():

    print("Test class MapMaker")
    print('value_limit = 0, number of accepted point = %s' % (MapMaker(start_point=[(0, 0)], value_limit=0).search()))
    # output=1: OK <--it is a known-solution
    print('value_limit = 1, number of accepted point = %s' % (MapMaker(start_point=[(0, 0)], value_limit=1).search()))
    # output=5: OK <--it is a known-solution
    print('value_limit = 2, number of accepted point = %s' % (MapMaker(start_point=[(1, 1)], value_limit=2).search()))
    # output=13: OK <--it is a known-solution
    print('value_limit = 19, number of accepted point = %s' % (MapMaker(start_point=[(100, 100)], value_limit=19).search()))
    # output = 102485.
    print('value_limit = 21, number of accepted point = %s' % (MapMaker(start_point=[(100, 200)], value_limit=21).search()))
    # output=287881

if __name__=='__main__':
    test_map_maker()