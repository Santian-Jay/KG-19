relationWithHT = {}
symmetric = {}
symmetricIndex = 0
strIndex = []



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


"""
Symmetric relationship algorithm, print data that can be reversed in each relationship
"""

for i in range(len(relationWithHT)):
    temp = relationWithHT[strIndex[i]]      # first row
    temp_1 = [temp[0]]                      # first group of first row
    tempList = [temp_1[0][0], temp_1[0][1]] #  first group of first row change to list
    # print("The first comparison data：", tempList)
    temp.remove(temp[0])    # remove first group
    while len(temp) != 0:
        for j in range(len(temp)):
            if len(temp) > 0:
                newArray = [temp[j][1], temp[j][0]]
                # print("The model for comparison is：", newArray)
                if tempList == newArray:
                    symmetric[symmetricIndex] = []
                    symmetric[symmetricIndex].append((strIndex[i], tempList, strIndex[i], (temp[j][0], temp[j][1])))
                    symmetricIndex += 1
                    # print(newArray)
        tempList = [temp[0][0], temp[0][1]]
        # print("update comparative data：", tempList)
        temp.remove(temp[0])

for i in range(len(symmetric)):
    print(symmetric[i])