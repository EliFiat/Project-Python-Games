print('Welcome to the country and capital Game')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: is the capital of cameroon Yaounde? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Is China the biggest producer of coal? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: what is the weakest and softest bone in the human body? ')
    if answer.lower()=='collar bone':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
    
    answer=input('Question 3: Round the value of pi to 2 decimal places ')
    if answer.lower()=='3.14':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software! ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thank you for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
