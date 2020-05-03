# problem statement: https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input())
list_of_lists = [list(map(int,input().split())) for i in range(n)]

# METHOD 1
def diagonaldifference(n,list_of_lists):
    diag1 = 0
    diag2 = 0

    for i in range(n):
        diag1 += list_of_lists[i][i]

    for i in range(n):
        diag2 += list_of_lists[i][(n-1)-i]

    print(abs(diag1 - diag2))

diagonaldifference(n,list_of_lists)

# METHOD 2
diag1 = sum(list_of_lists[i][i] for i in range(n))
diag2 = sum(list_of_lists[i][n-1-i] for i in range(n))
print(abs(diag1-diag2))