import converter


def main():
    while True:
        roman = input("Enter roman number: ")
        transformed_number = converter.roman_to_arabic(roman)
        print(transformed_number)


if __name__ == '__main__':
    main()