print("Welcome to my quiz")

quiz=[
    {
        "ques":"What is the capital of france?",
        "options":["A. Paris","B. London","C. Berlin"],
        "answer":"A"
    },
    {
        "ques":"Which country is known as the Land of the Rising Sun?",
        "options":["A. China","B. Japan","C. England"],
        "answer":"B"
    },
    {
        "ques":"What gas do plants absorb from the atmosphere?",
        "options":["A. Oxygen","B. CarbonDioxide","C. Helium"],
        "answer":"B"
    },
    {
        "ques":"Which is the longest river in the world?",
        "options":["A. Amazon River","B. Yangtze River","C. Nile River"],
        "answer":"C"
    },
    {
        "ques":"Which desert is the largest in the world?",
        "options":["A. Sahara Desert","B. Arabian Desert","C. Kalahari Desert"],
        "answer":"A"
    }
]

def quiz_start():
    score = 0
    for i,questions in enumerate(quiz):
        print(f"Q{i + 1}: {questions["ques"]}")
        for option in questions['options']:
            print(option)
        ans = (input("select any option: "))
        if ans == questions['answer']:
            score += 6
    print(f"your total score is {score}/30")
quiz_start()
