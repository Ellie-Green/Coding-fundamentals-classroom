# Part 1 
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = input("Enter your name and age in the format (name , age): ").split(",")
student1 = Student(student1[0], student1[1])
student2 = input("Enter your name and age in the format (name , age): ").split(",")
student2 = Student(student2[0], student2[1])

age_of_student1 = student1.age

print(f"{student1.name} is {age_of_student1} years old.")

# Part 2 
class Student():
  def __init__(self, name, age, current_class):
    self.name = name
    self.age = age
    self.current_class = current_class
    self.test_scores = []

  def add_test_scores(self, scores):
    self.test_scores = [int(score) for score in scores]

  def calculate_average_score(self):
    if not self.test_scores:
      return "NA"
    average_score = sum(self.test_scores) / len(self.test_scores)
    return average_score
  
student1 = input("Enter your name, age and current class in the format (name, age, current class): ").split(",")
student1 = Student(student1[0], student1[1], student1[2])
student1_test_scores = input("Enter 3 of your test scores in the following format (score1, score2, score3): ").split(",")
student1.add_test_scores(student1_test_scores)

student2 = input("Enter your name, age and current class in the format (name, age, current class): ").split(",")
student2 = Student(student2[0], student2[1], student2[2])

age_of_student1 = student1.age
average_score_result = student1.calculate_average_score()

print(f"{student1.name} your average score = {round(average_score_result,2)}")


# Part 3 
class Bird:
    def __init__(self, species, wingspan):
        self.species = species 
        self.wingspan = wingspan

    def fly(self):
        return (f"{self.species} is flying with a wingspan of {self.wingspan}.")

class Owl(Bird):
    def __init__ (self, species, wingspan, nocturnal = True):
        super().__init__(species, wingspan)
        self.nocturnal = nocturnal

    def fly(self):
        return (f"{self.species} is flying silently at night.")
    
    def hoot(self):
        return "Hoot Hoot"

class Dodo(Bird):
    def __init__ (self, species, wingspan, extinct = True):
        super().__init__(species, wingspan)
        self.extinct = extinct

    def description(self):
        return (f"The species {self.species} is extinct and had a wingspan of {self.wingspan}")
    

#-------MAIN CODE---------
generic_bird = Bird("Generic bird", 10)
owl = Owl("Barn owl", 20)
dodo = Dodo("Mauritius dodo", 30)

print(generic_bird.fly())
print(owl.fly())
print(owl.hoot())
print(dodo.description())

