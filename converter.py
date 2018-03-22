import re


romans = {'I':	1,
          'V':	5,
          'X':	10,
          'L':	50,
          'C':	100,
          'D':	500,
          'M':	1000}


def is_roman(roman):
    for r in roman:
        if r not in romans:
            return False
    return True


def is_roman_correct(roman):
    result = re.search(roman,'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})')
    return result is not None


def roman_to_arabic(roman):
    result = 0

    for i in range(0, (len(roman))):
        if i == len(roman)-1:
            result += romans[roman[i]]
            break

        if romans[roman[i]] < romans[roman[i+1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]

    return result


