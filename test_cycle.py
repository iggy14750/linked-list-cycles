
""" Tests for my linked list cycle detection code. """

import unittest
import cycle

class Lists(unittest.TestCase):
    """ Same as above. """
    def test_build_and_travel(self):
        """ Linked list will be built then travelled down. """
        data = [1, 2, 3, 4, 5]
        self.assertEqual(data, list(cycle.travel(cycle.build_list(data))))

if __name__ == '__main__':
    unittest.main()
