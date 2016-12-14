from MD5 import MD5

md5 = MD5()
hexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

foundList = list()
targetFoundListSize = 64
possibleAnswer = dict()
for h in hexList:
    possibleAnswer.setdefault(h,list())



index = 0
maxGap = 1000
input = 'zpqevtbw'

while len(foundList) < targetFoundListSize:
    saltedInput = '{}{}'.format(input, index)
    result = md5.calculate(saltedInput)

    min3 = maxGap
    min3letter = ''
    min5 = maxGap
    min5letterList = list()

    for h in hexList:
        answerList = possibleAnswer[h]
        while len(answerList) > 0 and answerList[0] + maxGap < index:
            answerList.pop(0)

        target = h * 5
        index3 = result.find(target[:3])
        if 0 < index3 < min3:
            min3 = index3
            min3letter = h

        if len(answerList):
            index5 = result.find(target)
            if 0 < index5:
                min5letterList.append(h)


    for min5letter in min5letterList:
        print('{}:: at index {} letter {}'.format(len(foundList),possibleAnswer[min5letter][0], min5letter))
        foundList.append(possibleAnswer[min5letter][0])
        possibleAnswer[min5letter].pop(0)

    if len(min5letterList):
        print('--------------------------------------')
        continue

    if min3letter != '':
        possibleAnswer[min3letter].append(index)

    index += 1

foundList.sort()
print(foundList)