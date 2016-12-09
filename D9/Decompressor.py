class Decompressor:

    def __init__(self, string, memorySave = False):
        self.input = string
        self.index = 0
        self.memorySave = memorySave
        self.count = 0
        return

    def decompress(self):
        while True:
            openB = self.input.find('(', self.index)
            if openB != -1:
                closeB = self.input.find(')', openB)
                xPos = self.input.find('x', openB)
                section = int(self.input[openB+1:xPos])
                copy = int(self.input[xPos+1:closeB]) - 1


                preChunk = self.input[:openB]
                postChunk = self.input[closeB + 1:]
                if not self.memorySave:
                    chunk = postChunk[:min(section, len(postChunk))]
                    self.input = preChunk + (chunk*copy) + postChunk
                    self.index += (copy+1)*section
                else:
                    self.count += len(preChunk)
                    chunk = postChunk[:min(section, len(postChunk))]
                    self.input = postChunk[min(section, len(postChunk)):]
                    chunkDecomp = Decompressor(chunk, True)
                    chunkDecomp.decompress()
                    self.count += chunkDecomp.count * (copy+1)
            else:
                self.count += len(self.input)
                break

