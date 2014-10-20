import unittest
from week1_day2 import CashDesk


class CashDeskTest(unittest.TestCase):

    def test_total_zero_when_new_instance_made(self):
        new_cash_desk = CashDesk()
        self.assertEqual(0, new_cash_desk.total())


if __name__ == '__main__':
    unittest.main()
