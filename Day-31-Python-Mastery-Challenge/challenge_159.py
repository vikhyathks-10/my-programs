# ============================================================
# DAY 31 - PROGRAM 159
# COMPLETE TESTING CHALLENGE
# ============================================================

import unittest


# ============================================================
# FUNCTIONS TO TEST
# ============================================================

def calculate_total(marks):

    return sum(marks)


def calculate_average(marks):

    if not marks:

        return 0

    return sum(marks) / len(marks)


def calculate_highest(marks):

    if not marks:

        return None

    return max(marks)


def calculate_lowest(marks):

    if not marks:

        return None

    return min(marks)


def calculate_grade(average):

    if average < 0 or average > 100:

        raise ValueError(
            "Average must be between 0 and 100."
        )

    if average >= 90:

        return "A"

    elif average >= 80:

        return "B"

    elif average >= 70:

        return "C"

    elif average >= 60:

        return "D"

    elif average >= 40:

        return "E"

    else:

        return "F"


def validate_marks(marks):

    for mark in marks:

        if not isinstance(
            mark,
            (int, float)
        ):

            return False

        if mark < 0 or mark > 100:

            return False

    return True


# ============================================================
# TEST CASES
# ============================================================

class TestStudentMarksAnalyzer(
    unittest.TestCase
):

    # --------------------------------------------------------
    # Normal tests
    # --------------------------------------------------------

    def test_total(self):

        self.assertEqual(
            calculate_total(
                [80, 90, 70, 60, 100]
            ),
            400
        )

    def test_average(self):

        self.assertEqual(
            calculate_average(
                [80, 90, 70, 60, 100]
            ),
            80
        )

    # --------------------------------------------------------
    # Highest / Lowest
    # --------------------------------------------------------

    def test_highest(self):

        self.assertEqual(
            calculate_highest(
                [50, 80, 90, 70]
            ),
            90
        )

    def test_lowest(self):

        self.assertEqual(
            calculate_lowest(
                [50, 80, 90, 70]
            ),
            50
        )

    # --------------------------------------------------------
    # Boundary tests
    # --------------------------------------------------------

    def test_zero_marks(self):

        self.assertEqual(
            calculate_average([0]),
            0
        )

    def test_full_marks(self):

        self.assertEqual(
            calculate_average([100]),
            100
        )

    # --------------------------------------------------------
    # Empty input tests
    # --------------------------------------------------------

    def test_empty_average(self):

        self.assertEqual(
            calculate_average([]),
            0
        )

    def test_empty_highest(self):

        self.assertIsNone(
            calculate_highest([])
        )

    def test_empty_lowest(self):

        self.assertIsNone(
            calculate_lowest([])
        )

    # --------------------------------------------------------
    # Grade tests
    # --------------------------------------------------------

    def test_grade_a(self):

        self.assertEqual(
            calculate_grade(95),
            "A"
        )

    def test_grade_b(self):

        self.assertEqual(
            calculate_grade(85),
            "B"
        )

    def test_grade_c(self):

        self.assertEqual(
            calculate_grade(75),
            "C"
        )

    def test_grade_d(self):

        self.assertEqual(
            calculate_grade(65),
            "D"
        )

    def test_grade_e(self):

        self.assertEqual(
            calculate_grade(45),
            "E"
        )

    def test_grade_f(self):

        self.assertEqual(
            calculate_grade(30),
            "F"
        )

    # --------------------------------------------------------
    # Invalid input tests
    # --------------------------------------------------------

    def test_invalid_negative_marks(self):

        self.assertFalse(
            validate_marks(
                [-10, 50, 60]
            )
        )

    def test_invalid_marks_above_100(self):

        self.assertFalse(
            validate_marks(
                [50, 101, 60]
            )
        )

    def test_invalid_text_marks(self):

        self.assertFalse(
            validate_marks(
                [50, "abc", 60]
            )
        )

    # --------------------------------------------------------
    # Unexpected input
    # --------------------------------------------------------

    def test_invalid_grade(self):

        with self.assertRaises(ValueError):

            calculate_grade(150)


# ============================================================
# RUN TESTS
# ============================================================

def run_tests():

    print("=" * 60)

    print(
        "       STUDENT MARKS TEST SUITE"
    )

    print("=" * 60)

    suite = unittest.TestLoader().loadTestsFromTestCase(
        TestStudentMarksAnalyzer
    )

    runner = unittest.TextTestRunner(
        verbosity=2
    )

    result = runner.run(suite)

    print("\n" + "=" * 60)

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
            "\nAll tests passed!"
        )

    else:

        print(
            "\nSome tests failed."
        )


if __name__ == "__main__":

    run_tests()