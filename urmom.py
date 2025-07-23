def welcome_message():
 """Function to display welcome message"""
print("=-" * 30)
print("Welcome to the grade calculator ")
print("=-" * 30)
welcome_message()

def get_test_scores():
# GET 3 test scores and return them
 score_1 = float(input("This is your 1st test score "))
score_2 = float(input("This is your 2nd test score "))
score_3 = float(input("This is your 3rd test score "))

return score_1, score_2, score_3

def calculate_average(score_1, score_2, score_3):
# init var call average add all scores then divide by 3
 average = (score_1 + score_2 + score_3) / 3
# return average
 return average

def get_letter_grade(average):
 
 



