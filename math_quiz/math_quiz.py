import random


def generate_random_number(minimum, maximum):
    """
    Generate a random number between two numbers.

    Args:
        minimum(int or float): the minimum value for the random number
        maximum(int or float): the maximum value for the random number

    Returns:
        int or float: a random number between min and max.
    """
    return round(random.uniform(minimum, maximum), 1)  # Generates random numbers allowing for both integer and float
    # values upto 1 decimal places


def generate_random_operation():
    """
        Generate a random operation between addition(+), subtraction(-), and multiply(*).

        Returns:
            string: a random operator between addition(+), subtraction(-), and multiply(*).
        """
    return random.choice(['+', '-', '*'])


def perform_operation(number1, number2, operator):
    """
        Perform a mathematical operation between two numbers.

        Args:
        number1 (int or float): The first number.
        number2 (int or float): The second number.
        operator (str): The operator representing the operation. Supported values are '+', '-', '*'.

        Returns:
        tuple: A tuple containing the string representation of the operation (e.g., 'number1 + number2')
        and the result of the operation.
        """
    operation_done = f"{number1} {operator} {number2}"
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return operation_done, result


def math_quiz():
    """
    A simple math quiz game where the player answers random arithmetic problems.

    The player is presented with math problems and needs to provide the correct answers. After answering each problem,
    the game displays if the answer was correct and the final score at the end.

    The game runs for a fixed number of questions and provides feedback on each answer.

    The quiz contains addition, subtraction, and multiplication problems generated randomly.

    """
    score = 0  # Initial score
    total_questions = 3  # The number of total questions should be an integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        try:
            first_number = generate_random_number(1, 10)
            second_number = generate_random_number(1, 5.5)
            operation = generate_random_operation()

            problem, actual_answer = perform_operation(first_number, second_number, operation)
            print(f"\nWhat is : {problem}")
            user_answer = input("Your answer: ")
            user_answer = float(user_answer)  # converting user input to float

            if user_answer == round(actual_answer, 1):
                print("Correct! You earned a point.")
                score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {round(actual_answer, 1)}.")

        except (ValueError, TypeError) as e:
            print(f"An error occurred: {e}. Please provide your answer as an integer or a float number.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
