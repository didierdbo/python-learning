while True:
    try:
        age = int(input("Enter your age: "))
        10/age
    except ValueError as value_error:
        print(f"Invalid input. Please enter a number. ({value_error})")
    except ZeroDivisionError:
        print("Age cannot be zero.")
    else:
        print(f"You are {age} years old.")
        print("Thank you for entering your age.")
        break

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"Invalid inputs. ({err})")

print(sum(10, 0))



while True:
    try:
        age = int(input("Enter your age: "))
        10/age
        raise ValueError("This is a custom error message.")
    except ValueError as value_error:
        print(f"Invalid input. Please enter a number. ({value_error})")
    except ZeroDivisionError:
        print("Age cannot be zero.")
    else:
        print(f"You are {age} years old.")
        print("Thank you for entering your age.")
        break