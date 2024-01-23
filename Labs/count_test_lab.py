# Had to use Replit to run the code as python was playing up 

# Count task
import count_test


def test_count_with_integers():
   sequence = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2]
   item = 2
   result = count_test.count(sequence, item)
   assert result == 4, f"Expected count of {item} is 4, but got {result}"


def test_count_with_strings():
   sequence = ["apple", "orange", "banana", "apple", "grape", "apple"]
   item = "apple"
   result = count_test.count(sequence, item)
   assert result == 3, f"Expected count of '{item}' is 3, but got {result}"


# Factorial task
import count_test

def test_factorial_accepts_an_input(self):
   factorial = count_test.fact()
   self.assertEqual(factorial.add(4), 24)

def test_factorial_method_returns_numeric(self):
   factorial = count_test.fact()
   self.assertIsInstance(factorial.fact(6), 720)

# List of squares task
import count_test

def tes_list_of_squares_accepts_an_input(self):
   number = count_test.n
   self.assertEqual(number(6), 36)
