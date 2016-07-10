peopleData = []
peopleData.append([174,53])
peopleData.append([180,70])
peopleData.append([176,87])
#各種迴圈使用方式
# 使用　for 的印出介紹

# 使用range的方法
for i in range(0,len(peopleData)):
    print(peopleData[i])


# 並且印出index
for i in range(0,len(peopleData)):
    print(str(i) + " " + str(peopleData[i]))
# 間隔為2
for i in range(0,len(peopleData),2):
    print(str(i) + " " + str(peopleData[i]))

# 使用　for in
for item in peopleData:
    print(str(item))

# 使用　for in 並且印出index
indexCount = 1
for item in peopleData:
    print(str(indexCount) + " " + str(item))
    indexCount+=1

# enumerate 介紹

for index,item in enumerate(peopleData):
    print(str(index) + " " + str(item))