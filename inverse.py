relationWithHT = {}
inverse = {}
inverseIndex = 0
strIndex = []

"""
Determine if new data is already included in the dataset
"""
def checkRepeat(list1, list2):
    isIn = False
    for i in range(len(inverse)):
        if list1 == inverse[i] or list2 == inverse[i]:
            isIn = True
    return isIn

file = open("dataset/train2id.txt", "r")
entryNumber = (int)(file.readline())

"""
Classify the data in the dataset by relation
"""
for index in range(entryNumber):
    content = file.readline()
    head, tile, relation = content.strip().split()
    if relation not in relationWithHT:
        strIndex.append(str(relation))
        relationWithHT[relation] = []
    relationWithHT[relation].append((head, tile))

for i in range(len(relationWithHT)):
    baseDic = relationWithHT[strIndex[i]]
    if i < len(relationWithHT) - 1:
        for j in range(len(baseDic)):
            tempList = [baseDic[j][0], baseDic[j][1]]
            round = i + 1
            while round < len(relationWithHT):
                targetDic = relationWithHT[strIndex[round]]
                for k in range(len(targetDic)):
                    arr = targetDic[k]
                    tempArray = [arr[1], arr[0]]
                    new = [arr[0], arr[1]]
                    if tempList == tempArray:
                        list1 = [tempList, strIndex[i], new, strIndex[round]]
                        list2 = [new, strIndex[round], tempList, strIndex[i]]
                        if not checkRepeat(list1, list2):
                            inverse[inverseIndex] = []
                            inverse[inverseIndex].append((tempList, strIndex[i], new, strIndex[round]))
                            inverseIndex += 1
                round += 1


for i in range(len(inverse)):
    print(inverse[i])