'''
Harry's Maths Homework

a b
c d

ab + ac + cd + bd = 200

(a*10 + b) + (a*10 + c) + (c*10 + d) + (b*10 + d) = 200
'''

import random
solutions = {}
answerKey = 1

while len(solutions.items()) < 20:

    # re-initialise variables
    a = 0
    b = 0
    c = 0
    d = 0
    test = 0
    answer = []

    # loop to find solution = 200
    while test != 200:

        a = random.randint(1,9)
        b = random.randint(1,9)
        c = random.randint(1,9)
        d = random.randint(1,9)

        test = (a*10 + b) + (a*10 + c) + (c*10 + d) + (b*10 + d)

    answer = [a, b, c, d]
    # print("a = ", a, "| b = ", b,"| c = ", c, "| d = ", d)
    print(a, b, "\n", c, d)
    print("answer: ", answerKey)
    d[answerKey].append(answer)
    answerKey =+ 1
