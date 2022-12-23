arr = [3, 4, 1, 5, 2, 6, 0]
count = [0] * 10
sortedArr = []

for i in arr:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        sortedArr.append(i)

print(sortedArr)