
class Program:
    def __init__(self, initValue):
        self.reg = dict()
        self.reg.setdefault('a', initValue[0])
        self.reg.setdefault('b', initValue[1])
        self.reg.setdefault('c', initValue[2])
        self.reg.setdefault('d', initValue[3])
        self.instructions = list()
        self.index = 0

    def compile(self, file):
        for instruction in file:
            self.instructions.append(instruction.replace('\n', ''))

    def run(self):
        while self.index < len(self.instructions):
            instruction = self.instructions[self.index]
            nextIndex = self.index + 1;
            inputs = instruction.split(' ')
            if inputs[0] == 'cpy':
                if inputs[1].isnumeric():
                    self.reg[inputs[2]] = int(inputs[1])
                else:
                    self.reg[inputs[2]] = self.reg[inputs[1]]
            elif inputs[0] == 'inc':
                self.reg[inputs[1]] += 1
            elif inputs[0] == 'dec':
                self.reg[inputs[1]] -= 1
            elif inputs[0] == 'jnz':
                if inputs[1].isnumeric():
                    check = int(inputs[1]) != 0
                else:
                    check = self.reg[inputs[1]] != 0

                if check:
                    nextIndex = self.index + int(inputs[2])

            self.index = nextIndex