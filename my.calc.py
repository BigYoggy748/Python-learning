def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
      raise ValueError(" dem fit divide by zero") 
    return a / b

def multiply(a, b):
    return a * b

def modulus(a, b):
    if b == 0:
        raise ValueError(" How you wan take see remainder?")
    return a % b

def power(a, b):
    return a ** b 

OPERATIONS = {
    "+": addition,
    "-": subtraction,
    "/": division,
    "*": multiply,
    "%": modulus,
    "**": power,
}

def get_number(number):
    while True:
        try:
            return(float(input(number)))
        except ValueError:
            print("\n oga na number be that? put better thing jor. \n")

def get_operator():
    correct = list(OPERATIONS.keys())
    while True:
        op = input(f"operator: {correct}: ").strip()
        if op in OPERATIONS:
            return op
        print(f"omo choose better thing jor: {correct}")

def show_history(history):
    if not history:
        print("\n  You don calculate anyting?. \n")
        return
    print("\n Calculation history:")
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry}")

def main():
    print("=" * 45)
    print("THIS IS MY FIRST CALCULATOR")
    print("=" * 45)
    print("  Type 'history' to view past calculations.")
    print("  Type 'quit' to leave.\n")

    history = []

    while True:
        choice = input("press enter to calculate, or type a command: ").strip().lower()

        if choice in ("quit", "exit"):
            print("\n Good Bye!")
            break

        if choice == "history":
            show_history(history)
            continue

        print()
        num1 = get_number("  First  number : ")
        op   = get_operator()
        num2 = get_number("  Second number : ")

        try:
            result = OPERATIONS[op](num1, num2)
        except ValueError as e:
            print(f"\n Error {e}\n")
            continue

        def fmt(n):
                return int(n) if n == int(n) else round(n, 10)

        expression = f"{fmt(num1)} {op} {fmt(num2)} = {fmt(result)}"

        print(f"\n Result: {expression}\n")

        history.append(expression)

if __name__ == "__main__":
    main()