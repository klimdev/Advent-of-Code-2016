import threading
import time
import hashlib

hexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
searchList = dict()

foundList = list()
targetFoundListSize = 64
possibleAnswer = dict()
for h in hexList:
    possibleAnswer.setdefault(h,list())
    searchList.setdefault(h, h*5)

def md5_2017(md5pool, index):
    with md5pool.lock:
        if index in md5pool.inProgress or index in md5pool.finished:
            print('error {} already in inProgress'.format(index))
            return
        md5pool.inProgress.add(index)

    result = '{}{}'.format(md5pool.input, index)
    for i in range(0, 2017):
        md5 = hashlib.md5()
        md5.update(result.encode('utf-8'))
        result = md5.hexdigest()


    with md5pool.lock:
        md5pool.inProgress.remove(index)
        md5pool.finished.setdefault(index, result)
        if md5pool.running:
            md5pool.pushNext(index)
    return

class MD5Pool:
    def __init__(self, word, interval):
        self.running = True
        self.inProgress = set()
        self.threads = dict()
        self.finished = dict()
        self.lock = threading.Lock()
        self.input = word
        self.interval = interval
        for i in range(0,interval):
            self.pushNext(-interval+i)

    def stop(self):
        self.running = False

    def pushNext(self, index):
        index = index + self.interval

        if index not in self.inProgress and index not in self.finished and index not in self.threads:
            self.threads.setdefault(index,threading.Thread(target=md5_2017, args=(self, index)))
            self.threads[index].start()
        return

    def get(self, index, maxGap):
        clean = index - (maxGap+1)
        if index - (maxGap+1) > 0:
            with self.lock:
                if clean in self.finished:
                    self.finished.pop(clean)

        while True:
            if index in self.inProgress:
                self.threads[index].join()
                self.threads.pop(index)
            elif index in self.finished:
                return self.finished[index]
            else:
                with self.lock:
                    if index not in self.inProgress and index not in self.finished and index not in self.threads:
                        self.threads.setdefault(index, threading.Thread(target=md5_2017, args=(self, index)))
                        self.threads[index].start()
                time.sleep(2)

index = 0
maxGap = 1000
input = 'zpqevtbw'
md5pool = MD5Pool(input,8)
min5letterList = list()

while len(foundList) < targetFoundListSize:
    result = md5pool.get(index, maxGap)
    #print('{} :: {}'.format(index, result))

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
            if index < answerList[i] + maxGap:
                if answerList[i] not in foundList:
                    print('{}:: at index {} letter {} by index {}'.format(len(foundList),answerList[i], min5letter, index))
                    foundList.append(answerList[i])

    if len(min5letterList):
        print('--------------------------------------')

    if min3letter:
        possibleAnswer[min3letter].append(index)

    index += 1
    if index % 1000 == 0:
        print('{}th check'.format(index))

md5pool.stop()

foundList.sort()
print(foundList)
print(foundList[targetFoundListSize-1])