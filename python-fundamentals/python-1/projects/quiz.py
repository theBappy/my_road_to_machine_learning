questions = (
    "What is the name of the process by which plants convert sunlight into energy?: ",
    "Which planet is known as the 'Red Planet'?: ",
    "Who painted the Mona Lisa?: ",
    "What is the chemical element with the symbol Fe?: ",
    "What is the largest lake in the world?: "
    )

options = (
    (
"A. Photosynthesis","B. Mars","C. Leonardo da Vinci","D. Iron"
), (
"A. Photosynthesis","B. Mars","C. Leonardo da Vinci","D. Iron"
), (
"A. Photosynthesis","B. Mars","C. Leonardo da Vinci","D. Iron"
), (
"A. Photosynthesis","B. Baikal","C. Leonardo da Vinci","D. Iron"
),
(
"A. Photosynthesis","B. Baikal","C. Leonardo da Vinci","D. Iron"
)
)
answers = ("A","B","C","D","B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (a, b, c, d): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"${answers[question_num]} is the correct answer")
    question_num += 1

print("-------------------")
print("--------- RESULT ----------")
print("-------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: ${score}%")