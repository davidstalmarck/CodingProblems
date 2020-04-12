def solve(n, lst):
    shouldBeAt = 1
    for i in range(n):
        if lst[i] ==shouldBeAt:
            shouldBeAt+=1
    print(n-shouldBeAt+1)


for _ in range(int(input())):
    solve(int(input()), [int(x) for x in input().split()])