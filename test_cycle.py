
""" Tests for my linked list cycle detection code. """

import unittest
import cycle

class Lists(unittest.TestCase):
    """ Same as above. """
    def test_build_and_travel(self):
        """ Linked list will be built then travelled down. """
        data = [1, 2, 3, 4, 5]
        self.assertEqual(data, list(cycle.travel(cycle.build_list(data))))

    def test_no_cycle(self):
        """ Both cycle detectors should return False. """
        data = [1, 2, 3, 4]
        uut = cycle.build_list(data)
        self.assertFalse(cycle.cycle1(uut))

    def test_has_cycle(self):
        """ Both cycle detectors should return True. """
        head = cycle.build_list([1, 2, 3, 4])
        # loop 4 back to 2
        temp = head.next.next.next
        temp.next = head.next
        self.assertTrue(cycle.cycle1(head))


if __name__ == '__main__':
    unittest.main()
