import csv
from enum import Enum


class ResponseEnum(Enum):
    NO = 'no'
    YES = 'yes'


def search_cities():
    with open('/Users/natividadesusana/Documents/cases-brazil-cities.csv', 'r') as csvfile:       
        city = input('\nEnter the city you want to search for:')
        print('-------------------------------------------------------')
        
        reader = csv.DictReader(csvfile)
        for row in reader:
            if city == row['city']:
                print('Total Covid cases in ' + city + ': ' + row['totalCases'])
                print('Total Deaths by Covid in ' + city + ': ' + row['deaths'])
                print('-------------------------------------------------------')


def get_response_from_question():
    question = '\nType [yes] to continue or [no] to exit: \n'
    response = input(question).lower().strip()
    return response


def main():
    print('\n- Welcome!')

    while True:
        search_cities()

        response = get_response_from_question()

        if response == ResponseEnum.NO.value:
            print('\nThanks for searching! 👍\n')
            break


if __name__ == '__main__':
    main()