
class Display:

    def __init__(self,width,height):
        self.Y = height
        self.X = width
        self.display = [[0 for i in range(0, self.X)] for i in range(0, self.Y)]
        return

    def __str__(self):
        return '\n'.join( str(self.display[i]) for i in range(0,self.Y)) + '\n'

    def __repr__(self):
        return self.display

    def _rect(self,a,b):
        for y in range(0,min(b,self.Y)):
            for x in range(0,min(a,self.X)):
                self.display[y][x] = 1
        return

    def _rotateCol(self,x,s):
        for i in range(0,s):
            yE = self.display[self.Y-1][x]
            for y in range(self.Y-1,0,-1):
                self.display[y][x] = self.display[y-1][x]
            self.display[0][x] = yE
        return

    def _rotateRow(self,y,s):
        for i in range(0,s):
            xE = self.display[y][self.X-1]
            for x in range(self.X-1,0,-1):
                self.display[y][x] = self.display[y][x-1]
            self.display[y][0] = xE
        return

    def Instruction(self, input):
        input = input.replace('\n','')
        if input.find('rect') != -1:
            input = input[4:]
            x = input.find('x')
            self._rect(int(input[:x]),int(input[x+1:]))
        else:
            by = input.find('by')
            if input.find('col') != -1:
                self._rotateCol(int(input[input.find('=') + 1:by - 1]), int(input[by + 2:]))
            else:
                self._rotateRow(int(input[input.find('=') + 1:by - 1]), int(input[by + 2:]))
        return

    def Count(self):
        return str(self).count('1')