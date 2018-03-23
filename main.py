from converters.to_roman_converter import arabic_to_roman
from converters.to_arabic_converter import roman_to_arabic


def menu():
    value = ''
    while value != 'e':
        value = input('''
    What do you want to do?
    
e - exit the program
r - convert roman to arabic
a - convert arabic to roman
    ''')
        try:
            if value == 'r':
                roman_case()
            elif value == 'a':
                arabic_case()
            elif value == 'e':
                break
            else:
                continue
        except ValueError as err:
            print(f'''
        Invalid input!
        {err.args[0]}''')


def roman_case():
    roman = input("Enter roman number: ")
    transformed_number = roman_to_arabic(roman)
    print(f'Arabic value: {transformed_number}')


def arabic_case():
    number = input("Enter arabic number: ")
    transformed_number = arabic_to_roman(int(number))
    print(f'Roman value: {transformed_number}')


def main():
    menu()


if __name__ == '__main__':
    main()