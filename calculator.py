def calculator():
    try:
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        result_as_integer = int(result)
        print(f"The result is: {result_as_integer}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
