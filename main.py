import pandas as pd
import random


df = pd.read_csv("Quiz.csv")

question_row = df.to_dict('records') # 'records' mean it converts each row into a singlr dictionary, if there are 10 rows then there will be 10 sets/list of dicts stored in question_row [{dict1},{dict2}...{}]

score = 0
num_questions=10

asked_questions = [] # to keep the record of questions that are already asked to avoid repetition

print("WElcome to put quiz Program!! ")

# We use '_' as the loop variable because we don't need the index (i), we just want to repeat the loop
for _ in range(num_questions): # 0 to (10-1) range(0,10)=0 to 9

    while True:
        row = random.choice(question_row) # pick a random dict/ row from the list of dictionary(question_row)

        if row['id'] not in asked_questions:
            asked_questions.append(row['id'])
            break # breaks the while loop which is a infinite loop
                  # it breaks from the while when it finds the question that has not been asked yet

    print(f"\nQn: {row['question']}")
    print(f"A. {row['option1']}")
    print(f"B. {row['option2']}")
    print(f"C. {row['option3']}")
    print(f"D. {row['option4']}")


    # Mapping letters to numbers
    letter_to_number = {'A':1,'B':2, "C":3, "D":4}

    while True:
        
        answer = input("Enter your choice (A, B, C, D): ").upper()
        if answer in letter_to_number:
            answer = letter_to_number[answer]
            break
        else:
            print("Invalid Input. Please enter A, B, C, D")


    if answer == row['correct_option_number']:
        print("Correct!!")
        score +=1
    else:
        correct_num=row['correct_option_number']
        correct_ans=row[f"option{correct_num}"]
        print(f"Wrong! \nThe correct answer is: {correct_ans}")
    input("Press Enter to go to next question")


print(f"\nYour Final Score: {score}/{num_questions}") #like 5/10, 10/10. 2/10
print("Thank you for playing")
