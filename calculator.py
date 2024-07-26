def calculator():
    try:
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        print(f"The result is: {int(result)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
