# problem statement: https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compare():
    Alice = list(map(int,input().split()))
    Bob = list(map(int,input().split()))

    a_score, b_score = 0,0

    for i in range(len(Alice)):
        if Alice[i] > Bob[i]:
            a_score += 1
        elif Alice[i] < Bob[i]:
            b_score += 1

    print (a_score,b_score)

compare()