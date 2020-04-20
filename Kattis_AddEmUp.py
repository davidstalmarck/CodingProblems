# you can find the problem here https://open.kattis.com/problems/addemup
# written by David Stålmarck 2020-03-18


n, s = [int(x) for x in input().split()]

numbers, allNumbers = input().split(),[]

for x, numb in enumerate(numbers):
    allNumbers.append([int(numb), x])
    if ('3' and '7') not in numb:
        revNumb = list(numb[::-1])
        for i in range(len(revNumb)):
            if revNumb[i] == '6':
                revNumb[i] = '9'
            elif revNumb[i] == '9':
                revNumb[i] = '6'
        allNumbers.append([int(''.join(revNumb)), x])

allNumbers.sort(key=lambda x: x[0])

j, length = -1, len(allNumbers)


for i in range(length):
    fromBottom = allNumbers[i]
    for _ in range(length):
        if length+j==0:
            break
        fromTop = allNumbers[j]
        summ = fromTop[0] + fromBottom[0]
        if summ == s and fromTop[1] != fromBottom[1]:
            #print(fromTop[0], fromBottom[0])
            print('YES')
            exit()
        elif summ > s:
            j -= 1
        elif summ < s:
            break

print('NO')