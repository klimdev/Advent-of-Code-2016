from MD5 import MD5

md5 = MD5()
hexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
searchList = dict()

foundList = list()
targetFoundListSize = 64
possibleAnswer = dict()
for h in hexList:
    possibleAnswer.setdefault(h,list())
    searchList.setdefault(h, h*5)



index = 0
maxGap = 1000
input = 'abc'

min3 = maxGap
min3letterList = list()
min5 = maxGap
min5letterList = list()

while len(foundList) < targetFoundListSize:
    saltedInput = '{}{}'.format(input, index)
    result = md5.calculate(saltedInput)

    min3 = maxGap
    min3letter = None
    min5 = maxGap
    min5letterList.clear()

    for h in hexList:
        answerList = possibleAnswer[h]
        while len(answerList) > 0 and answerList[0] + maxGap < index:
            answerList.pop(0)

        index3 = result.find(searchList[h][:3])
        if 0 <= index3 < min3:
            min3letter = h
            min3 = index3

        if len(answerList):
            index5 = result.find(searchList[h])
            if 0 < index5:
                min5letterList.append(h)

    for min5letter in min5letterList:
        answerList = possibleAnswer[min5letter]
        for i in range(0, len(answerList)):
            #if index <= answerList[i] + maxGap:
                if answerList[i] not in foundList:
                    print('{}:: at index {} letter {} by index {}'.format(len(foundList),answerList[i], min5letter, index))
                    foundList.append(answerList[i])

    if len(min5letterList):
        print('--------------------------------------')

    #for min3letter in min3letterList:
    if min3letter:
        possibleAnswer[min3letter].append(index)

    index += 1

foundList.sort()
print(foundList)
print(foundList[targetFoundListSize-1])