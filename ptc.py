# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
summ = 0
for i in arr:
    if i in A:
        summ +=1
    if i in B:
        summ -=1
print(summ)