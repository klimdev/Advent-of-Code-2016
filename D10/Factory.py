
class Bot:
    def __init__(self):
        self.toLow = 'x' #b + number = bot, o + number = output
        self.toHigh = 'x' #b + number = bot, o + number = output
        self.inputs = list()
        self.id = -1
        return

    def setInstruction(self, botID, string):
        self.id = botID
        lowTo = string.find('low to')
        highTo = string.find('high to')
        self.toLow = string[lowTo+7]
        if self.toLow == 'b':
            self.toLow += string[lowTo + 11:highTo - 5]
        else:
            self.toLow += string[lowTo + 14:highTo - 5]

        self.toHigh = string[highTo+8]
        if self.toHigh == 'b':
            self.toHigh += string[highTo + 12:]
        else:
            self.toHigh += string[highTo + 15:]

        return

    def getInput(self, chip):
        self.inputs.append(chip)
        return len(self.inputs)

    def execute(self, bots, outputs):
        if len(self.inputs) == 2:
            print('bot {} comparing {} and {}'.format(self.id, self.inputs[0], self.inputs[1]))
            self._give(min(self.inputs), self.toLow, bots, outputs)
            self._give(max(self.inputs), self.toHigh, bots, outputs)
            self.inputs.clear()
        return

    def _give(self, chip, to, bots, outputs):
        id = int(to[1:])
        if to[0] == 'b':
            bots[id].getInput(chip)
            bots[id].execute(bots, outputs)
        else:
            if id not in outputs:
                outputs.setdefault(id, chip)
        return

class Factory:
    def __init__(self, instructions):

        self.bots = dict()
        self.outputs = dict()
        self.readyBots = list()
        for instruction in instructions:
            instruction.replace('\n','')
            givesIndex = instruction.find('gives')
            if givesIndex != -1: #instruction for bot
                botID = int(instruction[instruction.find('t')+1:givesIndex])
                if botID not in self.bots:
                    self.bots.setdefault(botID, Bot())
                self.bots[botID].setInstruction(botID, instruction)
            else:
                value = int(instruction[6:instruction.find('goes')])
                to = int(instruction[instruction.find('bot')+4:])
                if to not in self.bots:
                    self.bots.setdefault(to, Bot())
                if self.bots[to].getInput(value) == 2:
                    self.readyBots.append(self.bots[to])
        return

    def run(self):
        for bot in self.readyBots:
            bot.execute(self.bots, self.outputs)

        print(self.outputs)


