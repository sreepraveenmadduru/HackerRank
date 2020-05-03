# problem statement: https://www.hackerrank.com/challenges/a-very-big-sum/problem


n = int(input())
num_list = list(map(int,input().split()))

result = 0
for num in num_list:
    result += num

print(result)