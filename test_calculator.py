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

    def test_delete(self):
        # Test delete functionality
        self.calc.btn_click(7)
        self.calc.btn_click('+')
        self.calc.btn_click(5)
        self.assertEqual(self.calc.delete(), '7+')
        self.assertEqual(self.calc.delete(), '7')

    def test_answer(self):
        # Test valid answers
        self.calc.btn_click(7)
        self.calc.btn_click('+')
        self.calc.btn_click(5)
        self.assertEqual(self.calc.answer(), '12')

        # Test division by zero (error case)
        self.calc.clear()
        self.calc.btn_click(7)
        self.calc.btn_click('/')
        self.calc.btn_click(0)
        self.assertEqual(self.calc.answer(), 'Error')

        # Test invalid expression (error case)
        self.calc.clear()
        self.calc.btn_click(7)
        self.calc.btn_click('/')
        self.calc.btn_click('+')
        self.assertEqual(self.calc.answer(), 'Error')


if __name__ == '__main__':
    unittest.main()
