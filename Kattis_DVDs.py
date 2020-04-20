# you can find the problem here https://open.kattis.com/problems/dvds
# written by David Stålmarck 2020-03-19

def solve(n, lst):
    shouldBeAt = 1
    for i in range(n):
        if lst[i] ==shouldBeAt:
            shouldBeAt+=1
    print(n-shouldBeAt+1)


for _ in range(int(input())):
    solve(int(input()), [int(x) for x in input().split()])