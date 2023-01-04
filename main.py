import tabulate


def fruits_names():
    return ['orange', 'grapefruit', 'lemon', 'lime', 'tangerine']

def fruits_avg_weights_grams():
    avg_weights = {'orange': 230, 'grapefruit': 400, 'lemon': 130, 'lime': 100, 'tangerine': 100}
    return avg_weights

def fruits_avq_diameter_cm():
    avg_diameters = {'orange': 6, 'grapefruit': 8, 'lemon': 4, 'lime': 4, 'tangerine': 4}
    return avg_diameters


def display_fruits_table():
    fruit_table = tabulate.tabulate(
        zip(fruits_names(), fruits_avg_weights_grams().values(), fruits_avq_diameter_cm().values()),
        headers=['FRUIT', 'AVG. WEIGHT (g)', 'AVG. DIAMETER (cm)'], tablefmt = 'fancy_grid')
    print(fruit_table)




def intensity_level():
    while True:
        try:
            print('1. Low\n2. Medium\n3. High\n4. Very high')
            aroma_intensity = int(input('\nPick an aroma intensity level: '))
        except:
            print('\nInvalid input. Pick a level in range 1-4. Value must be integer.')
            continue
        if aroma_intensity == 1:
            print('You picked low aroma intensity')
            return aroma_intensity
        elif aroma_intensity == 2:
            print('You picked medium aroma intensity')
            return aroma_intensity
        elif aroma_intensity == 3:
            print('You picked high aroma intensity')
            return aroma_intensity
        elif aroma_intensity == 4:
            print('You picked very high aroma intensity')
            return aroma_intensity
        else:
            print('\nInvalid input. Pick a level in range 1-4.')

def about_program():
    while True:
        print("\nZEST CALCULATOR FOR CRAFT BREWERIES allows you to calculate amount of citrus fruits you need to buy for your beer.\n"
              "The program stores data on the average weight and size of most common citrus fruits. In the first step you"
              "will choose units.\nThen you will enter amount of zest you need. Program will calculate how many fruits you should buy"
              " to produce such an amount of zest,\nsave this information in file and send this information to your co-workers"
              "by e-mail. Press any ENTER to get back to main menu."
              )
        go_back = input()
        if go_back == '':
            break
        else:
            print('\nPRESS ENTER TO GET BACK TO MAIN MENU\n')
    main()


def main_menu():
    print("1. Calculate amount of zest you need\n2. Display citrus fruits table. \n3. About program\n4. Exit\n")
    while True:
        try:
            menu_pick = int(input('What do you want to do? '))
        except ValueError:
            print('Please enter integer value from range 1-4.')
            continue
        if 1 <= menu_pick <= 4:
            return menu_pick
        else:
            print('Please enter integer value from range 1-4.')

def unit_picker():
    print('1. Hectoliters and Kilograms\n2. Liters and Grams')
    while True:
        try:
            unit_pair = int(input('Pick a unit pair: '))
        except ValueError:
            print('Please enter integer value from range 1-2.')
            continue
        if 1 <= unit_pair <= 2:
            return unit_pair
        else:
            print('Invalid input. Please enter integer value from range 1-2.')



def welcome():
    welcome = '>>>Welcome in ZEST CALCULATOR FOR CRAFT BREWERIES!!!<<<\n'
    len_welcome = len(welcome)
    star = '*'
    print(welcome, star * len_welcome, '\n')

def main():
    welcome()
    menu_pick = main_menu()
    if menu_pick == 4 :
        print('See you next time! ')
        quit()
    elif menu_pick == 3:
        about_program()
    elif menu_pick == 2:
        display_fruits_table()
    elif menu_pick == 1:
        units = unit_picker()
        aroma = intensity_level()


print(main())