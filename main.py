import converter


def menu():
    value = ''
    while value != 'e':
        value = input('''
    What do you want to do?
    
e - exit the program
r - convert roman to arabic
a - convert arabic to roman
    ''')
        if value == 'r':
            roman_case()
        elif value == 'a':
            arabic_case()
        elif value == 'e':
            break
        else:
            continue


def roman_case():
    roman = input("Enter roman number: ")
    if not converter.is_roman(roman):

        print('''
             Invalid input!

             Please, use this characters for roman number:
             I V X L C D M 
             ''')

    transformed_number = converter.roman_to_arabic(roman)
    print(f'Arabic value: {transformed_number}')


def arabic_case():
    pass


def main():
    menu()



if __name__ == '__main__':
    main()