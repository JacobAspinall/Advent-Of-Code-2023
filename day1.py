
digitToWordPairs = {
                '1' : 'one',
                '2' : 'two',
                '3' : 'three',
                '4' : 'four',
                '5' : 'five',
                '6' : 'six',
                '7' : 'seven',
                '8' : 'eight',
                '9' : 'nine'
                }

def getFirstDigit(string):

    for digit in digitToWordPairs.keys():
        digitAsWord = digitToWordPairs[digit]
        if digitAsWord in string:
            if all(not char.isdigit() for char in string.split(digitAsWord)[0]) and all(not digitWord in string.split(digitAsWord)[0] + digitAsWord[:-1] for digitWord in digitToWordPairs.values()):
                return digit

    #first digit is a real digit
    for char in string:
        if char.isdigit():
            return char
        
def getLastDigit(string):

    for digit in digitToWordPairs.keys():
        digitAsWord = digitToWordPairs[digit]
        if digitAsWord in string:
            if all(not char.isdigit() for char in string.split(digitAsWord)[-1]) and all(not digitWord in digitAsWord[1:] + string.split(digitAsWord)[-1] for digitWord in digitToWordPairs.values()):
                return digit

    for char in reversed(string):
        if char.isdigit():
            return char
        
def createTwoDigitNumberFrom2Digits(firstDigit, secondDigit):
    return int(firstDigit + secondDigit)

def getCalibrationCode(string):
    return createTwoDigitNumberFrom2Digits(getFirstDigit(string), getLastDigit(string))

def getSumOfCalibrationValues(input):
    sum = 0
    for line in input.split():
        sum += getCalibrationCode(line)
    return sum

with open('day1.txt') as input:
    print(getSumOfCalibrationValues(input.read()))