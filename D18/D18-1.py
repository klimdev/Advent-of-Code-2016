
class Row:
    def __init__(self, row):
        width = len(row.row)
        self.row = [ False for i in range(0,width) ]
        for i in range(0, width):
            left = False
            right = False
            if i > 0:
                left = row[i-1]
            center = row[i]
            if i + 1 < width:
                right = row[i+1]

            if ((left and center) and not right) or\
               ((right and center) and not left) or\
               (left and not (right or center)) or \
               (right and not (left or center)):
                self.row[i] = True

        self.safe = self.row.count(False)
        return

    def __getitem__(self, item):
        return self.row[item]

class FirstRow(Row):
    def __init__(self, string = ''):
        self.row = [ True if c == '^' else False for c in string.replace('\n','') ]
        self.safe = self.row.count(False)
        return

inputFile = open('D18.txt', 'r')

rows = list()
rows.append(FirstRow(inputFile.readline()))

#rowCount = 40
rowCount = 400000

while len(rows) < rowCount:
    rows.append(Row(rows[len(rows)-1]))

safes = 0
for row in rows:
    safes += row.safe

print(safes)