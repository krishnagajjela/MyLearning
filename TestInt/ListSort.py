#program to sort the list without sort funciton
ol = [10, 2, 5, 9, 3]
nl = []

while ol:
    mini = ol[0]
    for x in ol:
        if x < mini:
            mini = x
    nl.append(mini)
    ol.remove(mini)

print(nl)
print(ol)


# ---------------- easy way -------------------
NumList = [2,5,3,7,8,1,4]

Number = len(NumList)
for i in range (Number):
    for j in range(i + 1, Number):
        if NumList[i] > NumList[j]:
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print(NumList)
