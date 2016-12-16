import copy

def DragonCurve(a):
    b = a[::-1]
    b = b.replace('1', '2')
    b = b.replace('0', '1')
    b = b.replace('2', '0')
    return a + '0' + b

def DragonCurveUpTo(a, length):
    result = a
    while len(result) < length:
        result = DragonCurve(result)
    return result