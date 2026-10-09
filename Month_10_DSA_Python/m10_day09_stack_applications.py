
# MONTH 10 - DAY 9
# Stack Applications
# Programs 41-45

from __future__ import annotations

import math
import re


# =========================================================
# EXPRESSION TOKENIZER
# =========================================================
TOKEN_PATTERN = re.compile(
    r"\d+(?:\.\d+)?|[A-Za-z_]\w*|//|[()+\-*/%^]"
)


def tokenize(expression: str) -> list[str]:
    tokens: list[str] = []
    position = 0

    while position < len(expression):
        if expression[position].isspace():
            position += 1
            continue

        match = TOKEN_PATTERN.match(expression, position)

        if match is None:
            raise ValueError(
                f"Invalid character: {expression[position]}"
            )

        tokens.append(match.group())
        position = match.end()

    if not tokens:
        raise ValueError("Expression cannot be empty.")

    return tokens


# =========================================================
# EXPRESSION HELPERS
# =========================================================
OPERATORS = {"+", "-", "*", "/", "//", "%", "^"}

PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "//": 2,
    "%": 2,
    "^": 3,
    "u+": 4,
    "u-": 4,
}

RIGHT_ASSOCIATIVE = {"^", "u+", "u-"}


def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False


def is_operand(token: str) -> bool:
    return is_number(token) or (
        token not in OPERATORS
        and token not in {"(", ")"}
        and token not in {"u+", "u-"}
    )


def normalize_unary(tokens: list[str]) -> list[str]:
    """Represent unary plus/minus as u+ and u-."""
    result: list[str] = []
    expect_operand = True

    for token in tokens:
        if token in {"+", "-"} and expect_operand:
            result.append("u" + token)
        else:
            result.append(token)

        if token in {"(", "+", "-", "*", "/", "//", "%", "^"}:
            expect_operand = True
        else:
            expect_operand = False

    return result


def validate_tokens(tokens: list[str]) -> None:
    """Validate basic operand/operator order and parentheses."""
    depth = 0
    expect_operand = True

    for token in tokens:
        if token == "(":
            depth += 1
            expect_operand = True

        elif token == ")":
            if depth == 0:
                raise ValueError("Mismatched parentheses.")
            if expect_operand:
                raise ValueError("Missing operand before ')'.")
            depth -= 1
            expect_operand = False

        elif token in OPERATORS or token in {"u+", "u-"}:
            if token in {"u+", "u-"}:
                if not expect_operand:
                    raise ValueError("Unexpected unary operator.")
            else:
                if expect_operand:
                    raise ValueError("Missing operand.")
                expect_operand = True

        else:
            if not is_operand(token):
                raise ValueError(f"Invalid token: {token}")
            if not expect_operand:
                raise ValueError("Missing operator between operands.")
            expect_operand = False

    if depth != 0:
        raise ValueError("Mismatched parentheses.")

    if expect_operand:
        raise ValueError("Expression ends without an operand.")


# =========================================================
# PROGRAM 41
# EVALUATE POSTFIX EXPRESSION
# =========================================================
def evaluate_postfix(expression: str) -> float:
    tokens = expression.split()

    if not tokens:
        raise ValueError("Expression cannot be empty.")

    stack: list[float] = []

    for token in tokens:
        if is_number(token):
            stack.append(float(token))

        elif token in {"u+", "u-"}:
            if not stack:
                raise ValueError("Invalid postfix expression.")
            value = stack.pop()
            stack.append(value if token == "u+" else -value)

        elif token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression.")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                if right == 0:
                    raise ValueError("Division by zero.")
                result = left / right
            elif token == "//":
                if right == 0:
                    raise ValueError("Division by zero.")
                result = left // right
            elif token == "%":
                if right == 0:
                    raise ValueError("Modulo by zero.")
                result = left % right
            else:
                result = left ** right

            if isinstance(result, complex) or not math.isfinite(result):
                raise ValueError("Expression produced an invalid result.")

            stack.append(float(result))

        else:
            raise ValueError(
                f"Invalid postfix token: {token}. "
                "Use space-separated numbers and operators."
            )

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression.")

    return stack[0]


def program_41() -> None:
    expression = input(
        "Enter postfix expression (space-separated): "
    )
    result = evaluate_postfix(expression)
    print("Postfix result:", result)


# =========================================================
# INFIX TO POSTFIX CONVERSION HELPER
# =========================================================
def infix_to_postfix(expression: str) -> list[str]:
    tokens = normalize_unary(tokenize(expression))
    validate_tokens(tokens)

    output: list[str] = []
    operators: list[str] = []

    for token in tokens:
        if is_operand(token):
            output.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())

            if not operators:
                raise ValueError("Mismatched parentheses.")

            operators.pop()

        elif token in OPERATORS or token in {"u+", "u-"}:
            while operators and operators[-1] != "(":
                top = operators[-1]

                higher_precedence = (
                    PRECEDENCE[top] > PRECEDENCE[token]
                )

                equal_left_associative = (
                    PRECEDENCE[top] == PRECEDENCE[token]
                    and token not in RIGHT_ASSOCIATIVE
                )

                if higher_precedence or equal_left_associative:
                    output.append(operators.pop())
                else:
                    break

            operators.append(token)

    while operators:
        operator = operators.pop()

        if operator == "(":
            raise ValueError("Mismatched parentheses.")

        output.append(operator)

    return output


# =========================================================
# PROGRAM 42
# INFIX TO POSTFIX
# =========================================================
def program_42() -> None:
    expression = input("Enter infix expression: ")
    postfix = infix_to_postfix(expression)
    print("Postfix expression:", " ".join(postfix))


# =========================================================
# PROGRAM 43
# INFIX TO PREFIX
# =========================================================
def infix_to_prefix(expression: str) -> list[str]:
    """
    Convert infix to prefix using a recursive parser.
    This handles precedence, parentheses, unary signs,
    and right-associative exponentiation.
    """
    tokens = tokenize(expression)
    index = 0

    def parse_expression(min_precedence: int = 0) -> list[str]:
        nonlocal index

        if index >= len(tokens):
            raise ValueError("Missing operand.")

        token = tokens[index]

        # Unary operators
        if token in {"+", "-"}:
            index += 1
            operand = parse_expression(PRECEDENCE["u+"])
            left = ["u" + token] + operand

        elif token == "(":
            index += 1
            left = parse_expression(0)

            if index >= len(tokens) or tokens[index] != ")":
                raise ValueError("Mismatched parentheses.")

            index += 1

        elif token == ")":
            raise ValueError("Unexpected closing parenthesis.")

        elif token in OPERATORS:
            raise ValueError(f"Missing operand before {token}.")

        else:
            left = [token]
            index += 1

        # Binary operators
        while index < len(tokens):
            operator = tokens[index]

            if operator not in OPERATORS:
                break

            precedence = PRECEDENCE[operator]

            if precedence < min_precedence:
                break

            index += 1

            next_min = (
                precedence
                if operator in RIGHT_ASSOCIATIVE
                else precedence + 1
            )

            right = parse_expression(next_min)
            left = [operator] + left + right

        return left

    prefix = parse_expression()

    if index != len(tokens):
        raise ValueError("Invalid expression or mismatched parentheses.")

    return prefix


def program_43() -> None:
    expression = input("Enter infix expression: ")
    prefix = infix_to_prefix(expression)

    # Display unary operators as conventional unary signs
    display_tokens = [
        token[1:] if token in {"u+", "u-"} else token
        for token in prefix
    ]

    print("Prefix expression:", " ".join(display_tokens))


# =========================================================
# PROGRAM 44
# MINIMUM STACK WITH O(1) MINIMUM RETRIEVAL
# =========================================================
class MinStack:
    def __init__(self):
        self.values: list[int] = []
        self.minimums: list[int] = []

    def push(self, value: int) -> None:
        self.values.append(value)

        if not self.minimums or value <= self.minimums[-1]:
            self.minimums.append(value)

    def pop(self) -> int | None:
        if not self.values:
            return None

        value = self.values.pop()

        if self.minimums and value == self.minimums[-1]:
            self.minimums.pop()

        return value

    def peek(self) -> int | None:
        if not self.values:
            return None
        return self.values[-1]

    def get_min(self) -> int | None:
        if not self.minimums:
            return None
        return self.minimums[-1]

    def is_empty(self) -> bool:
        return len(self.values) == 0

    def display(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
            return

        print("Stack (bottom to top):", self.values)
        print("Current minimum:", self.get_min())


def program_44() -> None:
    stack = MinStack()

    while True:
        print("\n--- MIN STACK ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Get minimum")
        print("5. Display")
        print("6. Back to main menu")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                value = int(input("Enter integer to push: "))
                stack.push(value)
                print("Pushed:", value)

            elif choice == 2:
                value = stack.pop()
                if value is None:
                    print("Stack is empty.")
                else:
                    print("Popped:", value)

            elif choice == 3:
                value = stack.peek()
                print("Stack is empty." if value is None else f"Top: {value}")

            elif choice == 4:
                value = stack.get_min()
                print(
                    "Stack is empty."
                    if value is None
                    else f"Minimum: {value}"
                )

            elif choice == 5:
                stack.display()

            elif choice == 6:
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid integer.")


# =========================================================
# PROGRAM 45
# SORT A STACK USING RECURSION
# =========================================================
def insert_sorted(stack: list[int], value: int) -> None:
    if not stack or stack[-1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insert_sorted(stack, value)
    stack.append(top)


def sort_stack_recursive(stack: list[int]) -> None:
    if not stack:
        return

    top = stack.pop()
    sort_stack_recursive(stack)
    insert_sorted(stack, top)


def program_45() -> None:
    stack = list(map(
        int,
        input("Enter stack elements (bottom to top): ").split()
    ))

    sort_stack_recursive(stack)

    print("Sorted stack (bottom to top):", stack)
    if stack:
        print("Top element:", stack[-1])


# =========================================================
# MAIN MENU
# =========================================================
def main() -> None:
    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 9: STACK APPLICATIONS")
        print("======================================")
        print("41. Evaluate postfix expression")
        print("42. Convert infix to postfix")
        print("43. Convert infix to prefix")
        print("44. Minimum stack (O(1) get_min)")
        print("45. Sort stack using recursion")
        print("46. Run all programs")
        print("47. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid menu number.")
            continue

        try:
            if choice == 41:
                program_41()

            elif choice == 42:
                program_42()

            elif choice == 43:
                program_43()

            elif choice == 44:
                program_44()

            elif choice == 45:
                program_45()

            elif choice == 46:
                print("\nProgram 41: Postfix Evaluation")
                program_41()

                print("\nProgram 42: Infix to Postfix")
                program_42()

                print("\nProgram 43: Infix to Prefix")
                program_43()

                print("\nProgram 44: Minimum Stack")
                program_44()

                print("\nProgram 45: Recursive Stack Sort")
                program_45()

            elif choice == 47:
                print("Exiting Month 10 - Day 9. Keep practicing!")
                break

            else:
                print("Invalid choice.")

        except (ValueError, OverflowError, RecursionError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
