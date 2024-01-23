import re
class PasswordStrengthChecker:
    """
    Class to check the strength of passwords.
    """

    def __init__(self):
        """
        Initialize PasswordStrengthChecker.
        """
        self.password_history = {}

    def check_password_strength(self, password):
        """
        Check the strength of the given password.
        Args:
            password (str): The password to be checked.
        Returns:
            str: The strength rating of the password.
        """

        if self.is_common_password(password):
            return "Very Weak"
        
        length = self.check_length(password)
        case = self.check_case(password)
        number = self.check_number(password)
        special = self.check_special(password)
        strength_factors = [length, case, number, special]

        if all(factor == "Strong" for factor in strength_factors):
            return "Very Strong"

        if "Moderate" in strength_factors:
            return "Moderate"

        if "Weak" in strength_factors:
            return "Weak"

        return "Very Weak"
    
    def is_common_password(self, password):
        """
        Check if the password is common.
        Args:
            password (str): The password to be checked.
        Returns:
            bool: True if the password is common, False otherwise.
        """

        common_passwords = {"password", "123456", "qwerty", "abc123", "admin", "letmein", "welcome", "password1", "12345", "123456789"}
        return password.lower() in common_passwords
    
    def check_length(self, password):
        """
        Check the length strength of the password.
        Args:
            password (str): The password to be checked.
        Returns:
            str: The length strength rating of the password.
        """

        if len(password) >= 8:
            return "Strong"

        if 6 <= len(password) < 8:
            return "Moderate"

        return "Weak"
    
    def check_case(self, password):
        """
        Check the case strength of the password.
        Args:
            password (str): The password to be checked.
        Returns:
            str: The case strength rating of the password.
        """

        if any('a' <= char <= 'z' for char in password) and any('A' <= char <= 'Z' for char in password):
            return "Strong"

        if any('a' <= char <= 'z' for char in password) or any('A' <= char <= 'Z' for char in password):
            return "Moderate"

        return "Weak"
    
    def check_number(self, password):
        """
        Check the number strength of the password.
        Args:
            password (str): The password to be checked.
        Returns:
            str: The number strength rating of the password.
        """
        if any('0' <= char <= '9' for char in password):
            return "Strong"

        return "Weak"
    
    def check_special(self, password):
        """
        Check the special character strength of the password.
        Args:
            password (str): The password to be checked.
        Returns:
            str: The special character strength rating of the password.
        """

        has_special_char = bool(re.search('[!@#$%^&*(),.?":{}|<>]', password))
        return "Strong" if has_special_char else "Weak"

#------------MAIN CODE-----------------------

def main():
    password_checker = PasswordStrengthChecker()

    while True:
        user_input = input("Enter a password (type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            break

        strength = password_checker.check_password_strength(user_input)
        print(f"Password Strength: {strength}")
        password_checker.password_history[user_input] = strength

    print("Password History:")

    for password, strength in password_checker.password_history.items():
        print(f"{password}: {strength}")

if __name__ == "__main__":
    main()