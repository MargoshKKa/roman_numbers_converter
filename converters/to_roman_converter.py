# create dictionary of roman - arabic suggestions
romans = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
          6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
          30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
          90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
          600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
          2000: 'MM', 3000: 'MMM'}


def is_correct_arabic_number(number):
    if number > 3999:
        return False, f'Values over 3999 are not allowed: {number}'
    if number <= 0:
        return False, f'Non-positive values are not allowed: {number}'
    return True, ''


def arabic_to_roman(number):
    result = is_correct_arabic_number(number)
    if not result[0]: raise ValueError(result[1])

    # reverse string to get result
    roman = process(number)[::-1]
    return roman


def process(number):
    result = ''
    number = number.__str__()
    rank = 1
    # in inverse loop transform every digit of arabic number to roman
    # using romans dictionary
    # and add it to result string
    for digit in number[::-1]:
        if digit != '0':
            result += romans.get(int(digit) * rank)
        # change rank of the digit
        rank *= 10
    return result

