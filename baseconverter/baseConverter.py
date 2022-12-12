

def convertionFunc(binaryNum, baseNum):
    decimalNum = 0
    x = 1
    for bit in binaryNum[::-1]:
        intBit = int(bit)
        if intBit != 0:
            intBit *= x
            decimalNum += intBit
        x *= baseNum
    return decimalNum

while True>
    num = input("Enter a number: ")
    base = int(input("Enter a base for your number: "))
    print(convertionFunc(num, base))
