aList = [7, 12, 9, 11, 3]

n = len(aList) - 1

for i in range(n):
    for j in range(n - i ):
        if aList[j] > aList[j+1]:
            aList[j], aList[j+1] = aList[j+1], aList[j]


print(aList)