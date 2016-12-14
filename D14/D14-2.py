from MD5 import MD5

md5 = MD5()
hexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

foundList = set()
targetFoundListSize = 65
possibleAnswer = dict()
for h in hexList:
    possibleAnswer.setdefault(h,list())



index = 0
maxGap = 1000
input = 'zpqevtbw'

while len(foundList) < targetFoundListSize:
    saltedInput = '{}{}'.format(input, index)
    result = md5.calculate(saltedInput)
    stretching = 0
    while stretching < 2016:
        result = md5.calculate(result)
        stretching += 1

    min3 = maxGap
    min3letterList = list()
    min5 = maxGap
    min5letterList = list()

    for h in hexList:
        answerList = possibleAnswer[h]
        while len(answerList) > 0 and answerList[0] + maxGap < index:
            answerList.pop(0)

        target = h * 5
        index3 = result.find(target[:3])
        if 0 < index3:
            min3letterList.append(h)

        if len(answerList):
            index5 = result.find(target)
            if 0 < index5:
                min5letterList.append(h)


    for min5letter in min5letterList:
        answerList = possibleAnswer[min5letter]
        for i in range(0, len(answerList)):
            if index < answerList[i] + maxGap:
                print('{}:: at index {} letter {}'.format(len(foundList),answerList[i], min5letter))
                foundList.add(answerList[i])

    if len(min5letterList):
        print('--------------------------------------')

    for min3letter in min3letterList:
        possibleAnswer[min3letter].append(index)

    index += 1

print(foundList)