# you can find the problem here https://open.kattis.com/problems/a1paper
# written by David Stålmarck 2019-12-31, yes, I was coding on New Years Eve hahaa

n = int(input())
lista = [int(x) for x in input().split()]

count = 2**29
paper = 0

for i, el in enumerate(lista):
    count -= 2**(28-i)*el
    paper += (2**(-(5+2*i)/4)+2**(-(3+2*i)/4))*el
    if count<=0:
        paper+=(count/(2**(28-i)))*(2**(-(5+2*i)/4)+2**(-(3+2*i)/4))
        print(paper-2**(-3/4)-2**(-1/4))
        break
    else:
        continue
else:
    print('impossible')