import unittest
class tdd_Python(unittest.testCase):
    def test_banking_credit(self):
        bank=Banking()
        final_bal=bank.credit(1000)
        self.assertEqual(1000, final_bal)