import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_expression


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        """
        Test if the generated operator is one of '+', '-', or '*'.
        """
        operators = set(['+', '-', '*'])
        for i in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_calculate_expression(self):
        """
        Test the calculation of expressions with different operators.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (10, 6, '*', '10 * 6', 60),
            (4, 6, '-', '4 - 6', -2),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
