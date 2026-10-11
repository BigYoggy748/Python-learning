# ============================================================
# CALCULATOR USING THE DICTIONARY METHOD
# ============================================================


# ---- STEP 1: CREATE THE OPERATION FUNCTIONS ----------------
# Each function below takes two numbers (a and b)
# and returns the result of the math operation

# This function adds two numbers together
def add(a, b):
    return a + b

# This function subtracts b from a
def subtract(a, b):
    return a - b

# This function multiplies two numbers together
def multiply(a, b):
    return a * b

# This function divides a by b
# We check if b is 0 first because dividing by zero is impossible
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# This function raises a to the power of b
# Example: power(2, 3) = 2**3 = 8
def power(a, b):
    return a ** b

# This function returns the remainder after dividing a by b
# Example: modulus(10, 3) = 1  because 10 / 3 = 3 remainder 1
def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot use modulus with zero!")
    return a % b


# ---- STEP 2: CREATE THE DICTIONARY -------------------------
# This dictionary links each symbol (key) to its function (value)
# When the user types "+" we look it up here and get the add function
# When the user types "-" we look it up here and get the subtract function
# ...and so on for all operators

OPERATIONS = {
    "+":  add,        # "+" points to the add function
    "-":  subtract,   # "-" points to the subtract function
    "*":  multiply,   # "*" points to the multiply function
    "/":  divide,     # "/" points to the divide function
    "**": power,      # "**" points to the power function
    "%":  modulus,    # "%" points to the modulus function
}


# ---- STEP 3: CREATE A HELPER TO GET A NUMBER FROM THE USER -
# This function keeps asking the user for a number until they type a valid one
# The "prompt" parameter is the message we show the user e.g. "First number: "
def get_number(prompt):

    # "while True" means loop forever until we manually break out with "return"
    while True:

        # "try" means: attempt the code below, and if it fails jump to "except"
        try:
            # input(prompt) shows the message and waits for the user to type
            # float(...) converts what they typed into a decimal number e.g. "5" -> 5.0
            # return sends the number back to whoever called this function and stops the loop
            return float(input(prompt))

        # If the user typed something that cant be converted to a number e.g. "abc"
        # float() will raise a ValueError and we land here instead of crashing
        except ValueError:
            print("  That's not a valid number. Try again.")


# ---- STEP 4: CREATE A HELPER TO GET AN OPERATOR FROM THE USER
# This function keeps asking the user for an operator until they pick a valid one
def get_operator():

    # list(OPERATIONS.keys()) gives us all the keys from the dictionary
    # which are the symbols: ["+", "-", "*", "/", "**", "%"]
    valid = list(OPERATIONS.keys())

    # Loop forever until the user picks a valid operator
    while True:

        # Show the valid operators in the prompt so the user knows what to type
        # .strip() removes any accidental spaces the user might have typed
        op = input(f"  Operator {valid}: ").strip()

        # Check if what the user typed exists as a key in our dictionary
        if op in OPERATIONS:
            # It's valid so return it and stop the loop
            return op

        # If we reach here the user typed something invalid so we tell them
        print(f"  Please choose one of: {valid}")


# ---- STEP 5: CREATE THE HISTORY DISPLAY FUNCTION -----------
# This function prints all past calculations to the screen
def show_history(history):

    # If the history list is empty there is nothing to show
    if not history:
        print("\n  No calculations yet.\n")
        return

    print("\n  Calculation History:")

    # Loop through the history list
    # enumerate gives us a counter (i) starting at 1 alongside each item
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")

    print()


# ---- STEP 6: THE MAIN FUNCTION -----------------------------
# This is the heart of the program, it runs the calculator loop
def main_CALC():

    print("=" * 45)
    print("      Welcome to CLI Calculator")
    print("=" * 45)
    print("  Type 'history' to view past calculations.")
    print("  Type 'quit' to leave.\n")

    # Create an empty list to store each calculation as a string
    history = []

    # Loop forever until the user types quit
    while True:

        # Ask the user what they want to do
        choice = input("  Press Enter to calculate, or type a command: ").strip().lower()

        # If the user typed quit or exit, end the program
        if choice in ("quit", "exit"):
            print("\n  Goodbye!\n")
            break  # break jumps us out of the while True loop

        # If the user typed history, show the past calculations
        if choice == "history":
            show_history(history)
            continue  # continue skips the rest of the loop and starts again from the top

        # ---- GET THE TWO NUMBERS AND THE OPERATOR FROM THE USER
        print()
        num1 = get_number("  First  number : ")  # calls our get_number helper
        op   = get_operator()                     # calls our get_operator helper
        num2 = get_number("  Second number : ")  # calls our get_number helper again

        # ---- PERFORM THE CALCULATION ---------------------------
        # "try" in case the operation raises an error e.g. dividing by zero
        try:
            # Look up the operator in the dictionary to get the function
            # then call that function with num1 and num2
            # e.g. if op is "+" this becomes: add(num1, num2)
            result = OPERATIONS[op](num1, num2)

        # If an error was raised (like divide by zero) catch it here
        except ValueError as e:
            print(f"\n  Error: {e}\n")
            continue  # skip the rest and go back to the top of the loop

        # ---- DISPLAY AND SAVE THE RESULT -----------------------
        # This small helper formats a number nicely
        # If the result is a whole number show it without decimals e.g. 4.0 -> 4
        # Otherwise show it as a decimal
        def fmt(n):
            return int(n) if n == int(n) else round(n, 10)

        # Build the expression as a readable string e.g. "10 + 5 = 15"
        expression = f"{fmt(num1)} {op} {fmt(num2)} = {fmt(result)}"

        # Print the result to the screen
        print(f"\n  Result: {expression}\n")

        # Add the expression string to our history list
        history.append(expression)


# ---- STEP 7: RUN THE PROGRAM --------------------------------
# This line means: only run main() if we are running this file directly
# If another file imports this one, main() will NOT run automatically
if __name__ == "AI_calculator":
    main_CALC()