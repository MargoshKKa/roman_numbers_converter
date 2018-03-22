romans = {'I':	1,
          'V':	5,
          'X':	10,
          'L':	50,
          'C':	100,
          'D':	500,
          'M':	1000}


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

