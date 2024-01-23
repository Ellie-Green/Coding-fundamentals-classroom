import unittest
from final_task import PasswordStrengthChecker

class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):
        self.password_checker = PasswordStrengthChecker()

    def test_common_passwords(self):
        common_passwords = ["password", "123456", "qwerty", "abc123", "admin", "letmein", "welcome", "password1", "12345", "123456789"]
        for password in common_passwords:
            with self.subTest(password=password):
                self.assertEqual(self.password_checker.check_password_strength(password), "Very Weak")

    def test_length_strength(self):
        strong_password = "StrongPassword123"
        moderate_password = "Moderate12"
        weak_password = "Weak123"
        self.assertEqual(self.password_checker.check_password_strength(strong_password), "Very Strong")
        self.assertEqual(self.password_checker.check_password_strength(moderate_password), "Moderate")
        self.assertEqual(self.password_checker.check_password_strength(weak_password), "Weak")

    def test_case_strength(self):
        strong_password = "StrongPassword123"
        moderate_password = "moderate123"
        weak_password = "weakpassword"
        self.assertEqual(self.password_checker.check_password_strength(strong_password), "Very Strong")
        self.assertEqual(self.password_checker.check_password_strength(moderate_password), "Moderate")
        self.assertEqual(self.password_checker.check_password_strength(weak_password), "Weak")

    def test_number_strength(self):
        strong_password = "StrongPassword123"
        weak_password = "NoNumbersHere"
        self.assertEqual(self.password_checker.check_password_strength(strong_password), "Very Strong")
        self.assertEqual(self.password_checker.check_password_strength(weak_password), "Weak")

    def test_special_character_strength(self):
        strong_password = "Strong@Password123"
        weak_password = "NoSpecialCharacter"
        self.assertEqual(self.password_checker.check_password_strength(strong_password), "Very Strong")
        self.assertEqual(self.password_checker.check_password_strength(weak_password), "Weak")
        
if __name__ == "__main__":
    unittest.main()







