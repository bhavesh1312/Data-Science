QnA = {

    "Hi":"Hello sir, how may I help you ?",
    "I want to buy a watch":"Sir / Madam, which type of watch do you want to buy ?",
    "Which types of watches are available at your store ?":"Sir / Madam, we have smart watches, formal watches, casual watches as well as semi-casual watches",
    "I would like to buy a smart watch":"Good Choice, I would like to ask you some questions, so that I would get you some of the best watches",
    "Yes, sure":"Your age and gender",
    "I am 21 years old and I am an male individual":"Ok Sir, here are some of the watches",
    "I would like to buy this watch":"Ok Sir, Thank You for your purchase",
    "Thank You for your service too":"Welcome sir"


}

while True:
    Ques = input()

    if(Ques == "quit"):
        break

    else:
        print(QnA[Ques])