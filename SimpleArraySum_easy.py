# problem: https://www.hackerrank.com/challenges/simple-array-sum/problem



# METHOD 1
n = int(input())
value = input().split()

def func(value):
    result = 0 
    for _,v in enumerate(value):
        result += int(v)
    return result

print(func(value))

#METHOD 2
n = int(input())
func = lambda *args : sum(*args)
print(func(list(map(int,input().split()))))
