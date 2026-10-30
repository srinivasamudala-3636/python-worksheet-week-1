
def validate_password(password):

    errors = []

    # Check minimum 8 characters
    if len(password) < 8:
        errors.append("Minimum 8 characters required")

    # Check uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("At least one uppercase letter required")

    # Check lowercase letter
    if not any(char.islower() for char in password):
        errors.append("At least one lowercase letter required")

    # Check digit
    if not any(char.isdigit() for char in password):
        errors.append("At least one digit required")

    # Check special character
    if not any(char in "!@#$%^&*" for char in password):
        errors.append("At least one special character required")

    # Return result
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }


# Test the passwords
print(validate_password("weak"))
print(validate_password("Weak123"))
print(validate_password("MySecure@1"))
