
from Compiler import Program


inputFile = open('D12.txt', 'r')

program = Program([0,0,0,0])

program.compile(inputFile)
program.run()

print(program.reg['a'])
