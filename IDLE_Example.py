## This is a new python file
## I can add all my lines of code here

AnswerKey=['Process', 'Growth', 'Urgency']

print('What are the key ingredients that the Training and Evaluation Program is looking for in its developers?')
guess=input('Take a guess \n')
while(len(AnswerKey)!=0):
    if guess in AnswerKey:
            print("That's correct!")
            del AnswerKey[AnswerKey.index(guess)]
            if (len(AnswerKey)==0): break
            guess=input("What else? \n")
            

    else:
        print("Nope, incorrect. Now I will beat you")
        guess=input("Try again \n")
    
           
print("That's correct, Process, Growth and Urgency are the keys to success in the program")

