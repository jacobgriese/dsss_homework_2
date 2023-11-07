import random


def generate_random_integer(minimum, maximum):
    """
    Generates a random integer between the specified minimum and maximum values.
    
    Args:
        minimum (int): The minimum value of the random integer.
        maximum (int): The maximum value of the random integer.
        
    Returns:
        int: A random integer between minimum and maximum.
    """
    return random.randint(minimum, maximum)


def generate_random_operator():
    """
    Generates a random choice of '+', '-', or '*'.
    
    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def calculate_expression(num1, num2, operator):
    """
    Calculates the result of the given expression.
    
    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The operator ('+', '-', or '*').
        
    Returns:
        tuple: A tuple containing the formatted expression and the calculated result.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    expression = f"{num1} {operator} {num2}"
    return expression, result


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")

       # Separate try-except block for input() to handle invalid input
        try:
            user_answer_input = input("Your answer: ")
        except KeyboardInterrupt:
            # Handle KeyboardInterrupt (Ctrl+C) separately, if needed
            print("\nQuiz interrupted. Exiting.")
            break
        
        # Try to convert the user input to an integer, handle ValueError
        try:
            user_answer = int(user_answer_input)
            
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
