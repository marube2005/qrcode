# a dictionary which stores questions and answers.
# A variable which stores the Users marks/score
#loop through the dictionaries for key and value pairs
# Ask the questions to the users and allow them to answer.
#Tell them if they are right or wrong.
#dISPLAY THEIR SCORES WHEN QUIZ IS COMPLETED.


quiz = {
    "question1":{
       "question":"What is the Capital City of the Country Located in the Horn of Africa?",
       "answer": "Mogadishu"
    },
     "question2":{
       "question":"What is the Capital City of the Spain?",
       "answer": "Madrid"
    },
    "question3":{
       "question":"When did USA get independence?",
       "answer": "1776"
    },
    "question4":{
       "question":"What is the most impact of COVID-19 in Kenya and the world?",
       "answer": "Economic Crisis"
    },
    "question5":{
       "question":"Who pleaded on God to add him 15 more years to his ruling?",
       "answer": "King Hezekiah"
    },
    "question6":{
       "question":"Name the verse in the Bible which speaks of Agape Love?",
       "answer": "John 3:16"
    },
    "question7":{
       "question":"How Many countries are Located in Africa?",
       "answer": "55"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input(" Answer:")
    
    if answer.lower() == value['answer'].lower():
        print('Correct.')
        score += 1
        print("Your score is " + str(score))
        print("")
        print("")

    else:
        print("Wrong answer")
        print("The answer is: " + (value['answer']))
        print("Your score is " + str(score))
        print("")
        print("")

print("Your score is " + str(score) +" out of 7 questions")
print("Your Percentage is  " + str(int(score/7 * 100)+ "%"))