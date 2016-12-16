
def Checksum(str):
    while len(str)%2 == 0:
        newInput = ''
        for i in range(0,len(str),2):
            newInput += '1' if str[i:i+2].count(str[i]) % 2 == 0 else '0'
        str = newInput
    return str