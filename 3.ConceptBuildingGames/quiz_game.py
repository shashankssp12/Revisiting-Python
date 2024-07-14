'''
# Questions comes--Answer Gives--Answer Saved
# Repeat--Until Over
# Show Result in % 
# Ask if want to play again 
 
'''
# Resources
questions = {
    "What is the largest mammal in the world?": "A",
    "How many continents are there on Earth?": "A",
    "What planet is known as the Red Planet?": "A",
    "What is the tallest mountain in the world?": "A"
    }

options = [
    ["A. Blue whale", "B. Elephant", "C. Giant hamster", "D. Mega squirrel"],
    ["A. 7", "B. 5", "C. 12", "D. 3 (if you squint)"],
    ["A. Mars", "B. Jupiter", "C. Vulcan", "D. Planet of the Apes"],
    ["A. Mount Everest", "B. Kilimanjaro", "C. Mount Doom", "D. The Big Rock Candy Mountain"]
    ]
#----------------------------------------------------------------------------------

def new_game(questions,options):
    guesses=[]
    score=0
    question_number=1
    for key in questions:
        print("----------------------------------------------------------------------")
        print(str(question_number)+" "+key)
        print("----------------------------------------------------------------------")
        # Show Options
        option = options[question_number-1]
        print(option)
        print("----------------------------------------------------------------------")
        # Take input and store
        counter_for_invalid_input=0
        guess=None
        while guess not in ['A','B','C','D']:
            if counter_for_invalid_input>0:
                print("Choose from options")
            guess= input("Option:").upper()
            counter_for_invalid_input+=1
            
        guesses.append(guess)
        question_number+=1
        # Check answers and Update Score
        score+=check_answer(questions.get(key),guess)
    display_answer(guesses,questions)
    # print("Score:"+str(score))
    print("Your Score:"+str(int(score/len(questions)*100))+"%")
#-----------------------------------------------------------------

def display_answer(guesses,questions):
    print("Correct Answers:")
    for key in questions:
        print(questions.get(key),end=" ")
    print()
    print("Your Answers")
    for i in guesses:
        print(i,end=" ")
    print()
#--------------------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        return 1
    else:
        return 0
    
#------------------------------------------------------------
def play_again():
    response = input("Press 'y' to play again:").lower()
    if response != 'y':
        return False
    else:   
        return True
#-----------------------------------------------------------

new_game(questions,options)

while play_again():
    new_game(questions,options)
    play_again()

print("THANKS FOR PLAYING!")