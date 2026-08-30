# ============================================================
# MONTH 8 - DAY 30
# TESTING PYTHON PROGRAMS
#
# Programs 151-155
#
# 151. Test a Calculator
# 152. Test a Password Validator
# 153. Test a String Utility
# 154. Test a Data-Processing Function
# 155. Complete Test Suite
#
# Library:
# unittest
#
# How to run:
# python testing_programs.py
# ============================================================

import unittest


# ============================================================
# PROGRAM FUNCTIONS TO BE TESTED
# ============================================================


# ------------------------------------------------------------
# Calculator Functions
# ------------------------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


# ------------------------------------------------------------
# Password Validator
# ------------------------------------------------------------

def validate_password(password):

    if len(password) < 8:
        return False

    has_uppercase = any(
        character.isupper()
        for character in password
    )

    has_lowercase = any(
        character.islower()
        for character in password
    )

    has_digit = any(
        character.isdigit()
        for character in password
    )

    return (
        has_uppercase
        and has_lowercase
        and has_digit
    )


# ------------------------------------------------------------
# String Utility
# ------------------------------------------------------------

def reverse_string(text):
    return text[::-1]


def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for character in text:

        if character in vowels:
            count += 1

    return count


# ------------------------------------------------------------
# Data Processing Function
# ------------------------------------------------------------

def calculate_average(numbers):

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def get_highest(numbers):

    if not numbers:
        return None

    return max(numbers)


# ============================================================
# PROGRAM 151
# TEST CALCULATOR
# ============================================================

class TestCalculator(unittest.TestCase):

    def test_addition(self):

        self.assertEqual(
            add(10, 5),
            15
        )

    def test_subtraction(self):

        self.assertEqual(
            subtract(10, 5),
            5
        )

    def test_multiplication(self):

        self.assertEqual(
            multiply(10, 5),
            50
        )

    def test_division(self):

        self.assertEqual(
            divide(10, 5),
            2
        )

    def test_decimal_division(self):

        self.assertEqual(
            divide(5, 2),
            2.5
        )

    def test_division_by_zero(self):

        with self.assertRaises(ValueError):

            divide(10, 0)


# ============================================================
# PROGRAM 152
# TEST PASSWORD VALIDATOR
# ============================================================

class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):

        self.assertTrue(
            validate_password(
                "Python123"
            )
        )

    def test_short_password(self):

        self.assertFalse(
            validate_password(
                "Py12"
            )
        )

    def test_password_without_uppercase(self):

        self.assertFalse(
            validate_password(
                "python123"
            )
        )

    def test_password_without_lowercase(self):

        self.assertFalse(
            validate_password(
                "PYTHON123"
            )
        )

    def test_password_without_digit(self):

        self.assertFalse(
            validate_password(
                "PythonTest"
            )
        )


# ============================================================
# PROGRAM 153
# TEST STRING UTILITY
# ============================================================

class TestStringUtility(unittest.TestCase):

    def test_reverse_string(self):

        self.assertEqual(
            reverse_string("Python"),
            "nohtyP"
        )

    def test_reverse_empty_string(self):

        self.assertEqual(
            reverse_string(""),
            ""
        )

    def test_vowel_count(self):

        self.assertEqual(
            count_vowels("Hello"),
            2
        )

    def test_vowel_count_uppercase(self):

        self.assertEqual(
            count_vowels("PYTHON"),
            1
        )

    def test_vowel_count_without_vowels(self):

        self.assertEqual(
            count_vowels("rhythm"),
            0
        )


# ============================================================
# PROGRAM 154
# TEST DATA PROCESSING
# ============================================================

class TestDataProcessing(unittest.TestCase):

    def test_average(self):

        numbers = [
            10,
            20,
            30,
            40,
            50
        ]

        self.assertEqual(
            calculate_average(numbers),
            30
        )

    def test_average_decimal(self):

        numbers = [
            10,
            20,
            25
        ]

        self.assertAlmostEqual(
            calculate_average(numbers),
            18.333333,
            places=5
        )

    def test_empty_average(self):

        self.assertEqual(
            calculate_average([]),
            0
        )

    def test_highest_value(self):

        numbers = [
            10,
            45,
            20,
            80,
            30
        ]

        self.assertEqual(
            get_highest(numbers),
            80
        )

    def test_highest_negative_value(self):

        numbers = [
            -10,
            -5,
            -20
        ]

        self.assertEqual(
            get_highest(numbers),
            -5
        )

    def test_highest_empty_list(self):

        self.assertIsNone(
            get_highest([])
        )


# ============================================================
# PROGRAM 155
# COMPLETE TEST SUITE
#
# The test classes above are combined into one complete
# test suite.
# ============================================================

def create_test_suite():

    suite = unittest.TestSuite()

    # --------------------------------------------------------
    # Calculator tests
    # --------------------------------------------------------

    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(
            TestCalculator
        )
    )

    # --------------------------------------------------------
    # Password tests
    # --------------------------------------------------------

    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(
            TestPasswordValidator
        )
    )

    # --------------------------------------------------------
    # String utility tests
    # --------------------------------------------------------

    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(
            TestStringUtility
        )
    )

    # --------------------------------------------------------
    # Data processing tests
    # --------------------------------------------------------

    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(
            TestDataProcessing
        )
    )

    return suite


# ============================================================
# RUN TEST SUITE
# ============================================================

def run_tests():

    print("\n" + "=" * 65)
    print("             PYTHON TESTING SUITE")
    print("=" * 65)

    suite = create_test_suite()

    runner = unittest.TextTestRunner(
        verbosity=2
    )

    result = runner.run(
        suite
    )

    print("\n" + "=" * 65)
    print("                  TEST SUMMARY")
    print("=" * 65)

    print(
        f"Tests Run : {result.testsRun}"
    )

    print(
        f"Failures  : {len(result.failures)}"
    )

    print(
        f"Errors    : {len(result.errors)}"
    )

    if result.wasSuccessful():

        print(
            "\nAll tests passed successfully!"
        )

    else:

        print(
            "\nSome tests failed."
        )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    run_tests()