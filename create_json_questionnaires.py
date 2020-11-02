import json
import ast

name = input("Questionnaire name: ")
questionNumber = input("Number of questions: ")
questions = ""

for i in range(int(questionNumber)):
    questionName = input("Question: ")
    personlaityTrait = input("Personality Trait (0-5): ")
    reverse_Logic = input("Reverse Logic (Y/N): ")
    if( reverse_Logic == "Y" or reverse_Logic =="y"):
        reverseLogic = True
    else:
        reverseLogic = False
    if (i > 0):
        questions += ", "
    newQuestions = {
        "$type": "CoreBot.QuestionTopFive, CoreBot", 
        "personalityTrait": int(personlaityTrait), 
        "reverseLogic": reverseLogic, 
        "Question": questionName
    } 
    questions += str(newQuestions)
    

data = {
    "id": name,
    "document": 
    {
        "Key": name,
        "Value":
        {
            "$type": "System.Collections.Generic.List`1[[CoreBot.QuestionTopFive, CoreBot]], System.Private.CoreLib",
            "$values":
            
                ast.literal_eval(questions)
                # {
                #     "$type": "CoreBot.QuestionTopFive, CoreBot",
                #     "personalityTrait": 3,
                #     "reverseLogic": False,
                #     "Question": "Is original, comes up with new ideas"
                # },
                # {
                #     "$type": "CoreBot.QuestionTopFive, CoreBot",
                #     "personalityTrait": 4,
                #     "reverseLogic": True,
                #     "Question": "Is reserved"
                # }
            
        }
    }
}

prettyPrintedJson  = json.dumps(data, indent=2)
print(prettyPrintedJson)