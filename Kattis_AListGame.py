# you can find the problem here https://open.kattis.com/problems/listgame
# written by David Stålmarck 2020-01-09

numb, count = int(input()), 0
for i in range(2, round(numb**0.5)+1):
    while numb%i==0: numb, count = numb/i, count+1
print([count+1 if numb !=1 else count][0])