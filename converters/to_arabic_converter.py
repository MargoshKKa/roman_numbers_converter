# create dictionary of roman - arabic suggestions
romans = {'I':	1,
          'V':	5,
          'X':	10,
          'L':	50,
          'C':	100,
          'D':	500,
          'M':	1000}


# checks if symbols are roman
def is_roman(roman):
    for r in roman:
        if r not in romans:
            return False
    return True


def roman_to_arabic(roman):
    result = 0
    # check if processed symbols are roman
    if not is_roman(roman): raise ValueError('''Please, use this characters for a roman number:
            I V X L C D M ''')

    # process every symbol
    for i in range(0, (len(roman))):
        # when symbol is the last - always add it to result number
        if i == len(roman)-1:
            result += romans[roman[i]]
            break

        # check if next symbol value less than current - then substract it from result
        if romans[roman[i]] < romans[roman[i+1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]

    return result


