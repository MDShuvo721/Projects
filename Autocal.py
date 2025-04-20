import re

pattern = r"\d+"

print("TO EXIT, Press Space Key!") # A Heading

final_result = 0
while True:
    user_input = input("=")
    if user_input.strip() == "":
        break

    result = 0

    if re.search(r"[^0-9+\-*/]", user_input):
        print("Invalid Character?!...")
        print("please enter only 0-9 and +,-,*,/", end=" ")
        continue

    ls = re.finditer(pattern, user_input)

    for match in ls:
        num = int(match.group())

        if match.start() == 0:
            result += num
            continue

        if user_input[match.start()-1] == "+":
            result += num
        elif user_input[match.start()-1] == "-":
            result -= num
        elif user_input[match.start()-1] == "*":
            result *= num
        elif user_input[match.start()-1] == "/":
            result /= num
    
    if user_input[0] == "+":
        final_result += result
    elif user_input[0] == "-":
        final_result -= result
    elif user_input[0] == "*":
        final_result *= result
    elif user_input[0] == "/":
        final_result /= result
    else:
        final_result = result

    print(final_result)


# Next Steps to Improve:
# Operator Precedence: 
# Learn and implement operator precedence and parentheses handling (this would be a game-changer for complex expressions).

# Use Data Structures: 
# Implement a stack or queue to handle expression evaluation in a structured way.

# Error Handling: 
# Start adding try/except blocks to handle edge cases, such as division by zero or incorrect input formats.

# Refactor for Clarity: 
# Consider refactoring the code to make it more modular and readable, with clearer variable names and fewer redundant checks.