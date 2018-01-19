
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
        self.assertFalse(cycle.cycle2(uut))

    def test_has_cycle(self):
        """ Both cycle detectors should return True. """
        head = cycle.build_list([1, 2, 3, 4])
        # loop 4 back to 2
        temp = head.next.next.next
        temp.next = head.next
        self.assertTrue(cycle.cycle1(head))
        self.assertTrue(cycle.cycle2(head))

    def test_singleton(self):
        """ Does not contain a cycle, only one element. """
        head = cycle.build_list(['single'])
        self.assertFalse(cycle.cycle1(head))
        self.assertFalse(cycle.cycle2(head))

    def test_singleton_cyclic(self):
        """ A singleton cycle, should return True. """
        head = cycle.build_list(['cyclic'])
        head.next = head
        self.assertTrue(cycle.cycle1(head))
        self.assertTrue(cycle.cycle2(head))


if __name__ == '__main__':
    unittest.main()
