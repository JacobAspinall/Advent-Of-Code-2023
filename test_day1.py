import day1

def test_getFirstDigit_firstChar():
    assert day1.getFirstDigit('1jthreefksd5') == '1'

def test_getFirstDigit_notFirstChar():
    assert day1.getFirstDigit('fsfds1jthreefksd5') == '1'

def test_getFirstDigit_digitIsString():
    assert day1.getFirstDigit('fsfoneds1jfksd5') == '1'
    assert day1.getFirstDigit('fsftwods1jfksd5') == '2'
    assert day1.getFirstDigit('fsfthreeds1jfksd5') == '3'
    assert day1.getFirstDigit('fsffourds1jfksd5') == '4'
    assert day1.getFirstDigit('fsffiveds1jfksd5') == '5'
    assert day1.getFirstDigit('fsfsixds1jfksd5') == '6'
    assert day1.getFirstDigit('fsfsevends1jfksd5') == '7'
    assert day1.getFirstDigit('fsfeightds1jfksd5') == '8'
    assert day1.getFirstDigit('fsfnineds1jfksd5') == '9'

def test_getFirstDigit_digitIsStringWithMultipleStrings():
    assert day1.getFirstDigit('fsftwodsone1jfksd5') == '2'

def test_getLastDigit_lastChar():
    assert day1.getLastDigit('1jfksd5') == '5'

def test_getLastDigit_notLastChar():
    assert day1.getLastDigit('fsfds1jfksd5') == '5'

def test_getLastDigit_digitIsString():
    assert day1.getLastDigit('fsfds1jfksd5fonejk') == '1'
    assert day1.getLastDigit('fsfds1jfksd5ftwojk') == '2'
    assert day1.getLastDigit('fsfds1jfksd5fthreejk') == '3'
    assert day1.getLastDigit('fsfds1jfksd5ffourjk') == '4'
    assert day1.getLastDigit('fsfds1jfksd5ffivejk') == '5'
    assert day1.getLastDigit('fsfds1jfksd5fsixjk') == '6'
    assert day1.getLastDigit('fsfds1jfksd5fsevenjk') == '7'
    assert day1.getLastDigit('fsfds1jfksd5feightjk') == '8'
    assert day1.getLastDigit('fsfds1jfksd5fninejk') == '9'

def test_getLastDigit_digitIsStringWithMultipleStrings():
    assert day1.getLastDigit('fsfonedstwo1jfksd5onefdsthree') == '3'

def test_combineTwoDigitsIntoNumber_returnsCorrectNumber():
    assert day1.createTwoDigitNumberFrom2Digits('1','5') == 15

def test_getCalibrationCode():
    assert day1.getCalibrationCode('two1nine') == 29
    assert day1.getCalibrationCode('eightwothree') == 83
    assert day1.getCalibrationCode('abcone2threexyz') == 13
    assert day1.getCalibrationCode('xtwone3four') == 24
    assert day1.getCalibrationCode('4nineeightseven2') == 42
    assert day1.getCalibrationCode('zoneight234') == 14
    assert day1.getCalibrationCode('7pqrstsixteen') == 76

def test_getSumOfCalibrationValuesAllDigits_correctSum():
    input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

    assert day1.getSumOfCalibrationValues(input) == 142

def test_getSumOfCalibrationValuesWithSomeDigitsAsWords_correctSum():
    input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

    assert day1.getSumOfCalibrationValues(input) == 281