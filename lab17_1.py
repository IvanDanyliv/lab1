#!/usr/bin/env python3

from lab7_9 import is_lucky_ticket
import unittest

class LabTest(unittest.TestCase):
    def test_is_lucky_ticket_12321_should_be_true(self):
        actually = is_lucky_ticket('12321')
        
        self.assertTrue(actually)

    def test_is_lucky_ticket_123321_should_be_true(self):
        actually = is_lucky_ticket('123321')

        self.assertTrue(actually)

    def test_is_lucky_ticket_123331_should_be_false(self):
        actually = is_lucky_ticket('123331')

        self.assertFalse(actually)

    def test_is_lucky_ticket_12331_should_be_false(self):
        actually = is_lucky_ticket('12331')

        self.assertFalse(actually)
