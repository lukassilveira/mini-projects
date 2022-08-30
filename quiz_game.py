score = 0
questionsAndAnswers = [["What's the name of the instrument used by Link in N64 Zelda game? ", "ocarina"],
             ["What's the name of Link's mare? ", "epona"],
             ["What's the name of the guardian of Hyrule royal family? ", "impa"],
             ["What's the name of the instrument used by Link in Nintendo Wii Zelda game? ", "harp"],
             ["What's the name of Link's companion in N64 Zelda game? ", "navi"]]

def checkAnswer(userAnswer, correctAnswer):
    if userAnswer != correctAnswer:
        print("Incorret!")
    else:
        global score
        score += 1
        print("Correct!")

print("Welcome to the Zelda Quiz Game!")
playing = input("Do you want to play? \n")

if playing.lower() != "yes":
    quit()

print("Let's play, then...")
print
for index, item in enumerate(questionsAndAnswers):
    answer = input(str(index + 1) + "/" + str(len(questionsAndAnswers)) + " - " + item[0])
    checkAnswer(answer.lower(), item[1])
    
print("You got a total of " + str(score) + " scores in a total of " + str(len(questionsAndAnswers)) + "!")
