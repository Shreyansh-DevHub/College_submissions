class InvalidAgeError(Exception):
    """Custom exception for invalid age."""


def verify_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return True


try:
    age = int(input("Enter age: "))
    if verify_age(age):
        print("Access granted!")
except InvalidAgeError as e:
    print(f"Custom Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("Verification process complete.")



print("name: shreyansh singh")
print("prn no.: 26013010907")
