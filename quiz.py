print("WELCOME TO THE QUIZ!!")
playing = input("DO YOU WANT TO PLAY THE GAME :- ")
if playing.lower() == "yes":
    print("THE QUIZ BEGINS!!!!!!!!")
    print("Let's start the quiz!")
    q1 = input("What is the capital of U.S.A? ")
    if q1.lower() == "washington dc":
        p1 = 1
    else:
        p1 = 0
    q2 = input("What is the highest mountain in Japan? ")
    if q2.lower() == "mt fuji":
        p2 = 1
    else:
        p2 = 0
    q3 = input("Which Japanese city is famous for its annual cherry blossom festivals and historic temples, such as Kinkaku-ji (the Golden Pavilion)? ")
    if q3.lower() == "kyoto":
        p3 = 1
    else:
        p3 = 0
    q4 = input("Which river is the longest in the world? ")
    if q4.lower() == "nile":
        p4 = 1
    else:
        p4 = 0
    q5 = input("What is the capital of China? ")
    if q5.lower() == "beijing":
        p5 = 1
    else:
        p5 = 0
    q6 = input("Who was the first President of the United States? ")
    if q6.lower() == "george washington":
        p6 = 1
    else:
        p6 = 0
    q7 = input('Who wrote the play "Romeo and Juliet"? ')
    if q7.lower() == "william shakespeare":
        p7 = 1
    else:
        p7 = 0
    q8 = input("What currency is used in South Korea? ")
    if q8.lower() == "won":
        p8 = 1
    else:
        p8 = 0
    q9 = input("What is the smallest country in the world by land area? ")
    if q9.lower() == "vatican city":
        p9 = 1
    else:
        p9 = 0
    q10 = input('Who directed the movie "Inception"? ')
    if q10.lower() == "christopher nolan":
        p10 = 1
    else:
        q10 = 0
    score = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    if score < 5:
        print("NICE TRY!!!")
        print(f"Your Score is {score} out of 10!!")
    elif score >= 5:
        print("GREAT JOB!!!")
        print(f"Your Score is {score} out of 10!!")
    else:
        print("BAD JOB!!!")
else:
    print("NO WORRIES!!")
    print("Have a Good Day!")