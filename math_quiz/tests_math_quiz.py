import unittest
from math_quiz import generate_random_number, generate_random_operation, perform_operation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def generate_random_operation(self):
        # Test if random operator generated are within the specified list
        for _ in range(1000): # Test a large number of random operations
            operation = generate_random_operation()
            self.assertIn(operation, {'+', '-', '*'}, f"Unexpected operation: {operation}")


    def perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), # Addition
                (0, 0, '+', '0 + 0', 0),
                (-3, -8, '+', '-3 + 8', 5),
                (2.5, 3.5, '+', '2.5 + 3.5', 6),

                (5, 2, '-', '5 - 2', 3), # Subtraction
                (0, 0, '-', '0 - 0', 0),
                (-3, 8, '-', '-3 - 8', -11),
                (2.5, 3.5, '-', '2.5 - 3.5', -1),

                (5, 2, '*', '5 * 2', 10), # Multiplication
                (0, 0, '*', '0 * 0', 0),
                (-3, 8, '*', '-3 * 8', -24),
                (2.5, 3.5, '*', '2.5 * 3.5', 8.75),
            ]

            for number_1, number_2, operator, expected_problem, expected_answer in test_cases:
                with self.subTest(number_1=number_1, number_2=number_2, operator=operator):
                    problem, result = perform_operation(number_1, number_2, operator)
                    self.assertEqual(problem, expected_problem)
                    self.assertEqual(result, expected_answer)


if __name__ == "__main__":
    unittest.main()
