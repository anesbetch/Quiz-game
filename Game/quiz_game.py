import csv

def load_questions(file_path):
    questions = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append(row)
    return questions

def play_quiz(questions):
    score = 0
    total_questions = len(questions)
    for question in questions:
        print(question['question'])
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"\nYou scored {score} out of {total_questions}.")

if __name__ == "__main__":
    questions = load_questions('data/questions.csv')
    play_quiz(questions)
