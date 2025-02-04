import unittest
from Calc import CalculatorLogic


class TestCalculatorLogic(unittest.TestCase):

    def setUp(self):
        self.calc = CalculatorLogic()

    def test_btn_click(self):
        # Test button click functionality
        self.assertEqual(self.calc.btn_click(7), '7')
        self.assertEqual(self.calc.btn_click('+'), '7+')
        self.assertEqual(self.calc.btn_click(5), '7+5')

    def test_clear(self):
        # Test the clear functionality
        self.calc.btn_click(7)
        self.calc.btn_click('+')
        self.calc.btn_click(5)
        self.assertEqual(self.calc.clear(), '')

    def test_answer(self):
        # Test valid answers
        self.calc.btn_click(7)
        self.calc.btn_click('+')
        self.calc.btn_click(5)
        self.assertEqual(self.calc.answer(), '12')


if __name__ == '__main__':
    unittest.main()
