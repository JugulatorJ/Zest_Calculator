import tabulate


def fruits_names():
    return ['orange', 'grapefruit', 'lemon', 'lime', 'tangerine']

def fruits_avg_weights_grams():
    avg_weights_g = {'orange': 230, 'grapefruit': 250, 'lemon': 123, 'lime': 115, 'tangerine': 123}
    return avg_weights_g

def fruits_avg_weights_kilograms():
    avg_weights_kg = {'orange': 0.23, 'grapefruit': 0.4, 'lemon': 0.13, 'lime': 0.1, 'tangerine': 0.1}
    return avg_weights_kg

def fruits_avq_diameter_cm():
    avg_diameters = {'orange': 6, 'grapefruit': 8, 'lemon': 4, 'lime': 4, 'tangerine': 4}
    return avg_diameters

def fruit_avg_weight_after_peeling_grams():
    avg_weights_after_peeling_g = {'orange': 220, 'grapefruit': 239, 'lemon': 118, 'lime': 111, 'tangerine': 118}
    return avg_weights_after_peeling_g

def fruit_avg_weight_after_peeling_kilograms():
    avg_weights_after_peeling_g = {'orange': 0.22, 'grapefruit': 0.239, 'lemon': 0.118, 'lime': 0.111, 'tangerine': 0.118}
    return avg_weights_after_peeling_kg

def zest_from_one_fruit_grams(fruits_avg_weights_grams, fruit_avg_weight_after_peeling_grams):
    before_peeling = fruits_avg_weights_grams()
    after_peeling = fruit_avg_weight_after_peeling_grams()
    single_fruit_zest_g = {key: before_peeling[key] - after_peeling.get(key, 0) for key in before_peeling}
    return single_fruit_zest_g


def display_fruits_table():
    while True:
        fruit_table = tabulate.tabulate(zip(fruits_names(), fruits_avg_weights_grams().values(), fruits_avg_weights_kilograms().values(),
                        fruits_avq_diameter_cm().values()), headers=['Fruit', 'Avg. Weight (g)', 'Avg. Weight (kg)', 'Avg. Diameter (cm)'],
                        tablefmt='fancy_grid')
        print(fruit_table)
        print('\nPRESS ENTER TO GET BACK TO MAIN MENU\n')
        go_back = input()
        if go_back == '':
            break
        else:
            print('\nPRESS ENTER TO GET BACK TO MAIN MENU\n')
    main()

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
              "Program will calculate how many fruits you should buy to produce specific amount of zest to get desired level of aroma intensity\n"
              "Grams of zest per liter of beer is based on my own experience. The program assumes 15-40 minutes whirpool addition.\n"
              "ZEST CALCULATOR FOR CRAFT BREWERIES will allow you to send an email with an order to your supplier and save a copy of it on your computer\n"
              "CHEERS!!!\n"
              "\n>>>PRESS ENTER TO GET BACK TO MAIN MENU<<<"
              )
        go_back = input()
        if go_back == '':
            break
        # else:
        #     print('\nPRESS ENTER TO GET BACK TO MAIN MENU\n')
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



def welcome_func():
    welcome_txt = '>>>Welcome to ZEST CALCULATOR FOR CRAFT BREWERIES!!!<<<\n'
    len_welcome_txt = len(welcome_txt)
    star = '*'
    welcome = (welcome_txt + star * len_welcome_txt + '\n')
    return welcome

def beer_volume(unit_pair):
    while True:
        if unit_pair == 1:
            try:
                beer_volume = float(input('Enter beer volume in hectoliters: '))
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            if beer_volume <= 0:
                print('Invalid input. Please enter a number greater than 0.')
                continue
            else:
                return beer_volume
        elif unit_pair == 2:
            try:
                beer_volume = float(input('Enter beer volume in liters: '))
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            if beer_volume <= 0:
                print('Invalid input. Please enter a number greater than 0.')
                continue
            else:
                return beer_volume

def vol_zest_aroma_ratio(unit_pair, aroma_intensity, volume):
    low_ratio = [0.5, 1]
    low_zest = []
    medium_ratio = [1, 1.5]
    medium_zest = []
    high_ratio = [1.5, 2]
    high_zest = []
    very_high_ratio = [2, 2.5]
    very_high_zest = []
    if unit_pair == 1:
        if aroma_intensity == 1:
            for ratio in low_ratio:
                zest = (volume * ratio)/10
                low_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume, low_zest[0], low_zest[1]))
            return low_zest
        if aroma_intensity == 2:
            for ratio in medium_ratio:
                zest = (volume * ratio)/10
                medium_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume, medium_zest[0], medium_zest[1]))
            return medium_zest
        if aroma_intensity == 3:
            for ratio in high_ratio:
                zest = (volume * ratio)/10
                high_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume, high_zest[0], high_zest[1]))
            return high_zest
        if aroma_intensity == 4:
            for ratio in very_high_ratio:
                zest = (volume * ratio)/10
                very_high_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume, very_high_zest[0], very_high_zest[1]))
            return very_high_ratio
    if unit_pair == 2:
        if aroma_intensity == 1:
            for ratio in low_ratio:
                zest = volume * ratio
                low_zest.append(zest)
            print("To infuse {} liters of beer you need {}-{} grams of zest in total.".format(volume,low_zest[0],low_zest[1]))
            return low_zest
        if aroma_intensity == 2:
            for ratio in medium_ratio:
                zest = volume * ratio
                medium_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume,medium_zest[0],medium_zest[1]))
            return medium_zest
        if aroma_intensity == 3:
            for ratio in high_ratio:
                zest = volume * ratio
                high_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume, high_zest[0],high_zest[1]))
            return high_zest
        if aroma_intensity == 4:
            for ratio in very_high_ratio:
                zest = volume * ratio
                very_high_zest.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume,very_high_zest[0],very_high_zest[1]))
            return very_high_ratio


def main():
    print(welcome_func())
    menu_pick = main_menu()
    if menu_pick == 4 :
        print('See you next time! ')
        quit()
    elif menu_pick == 3:
        about_program()
    elif menu_pick == 2:
        display_fruits_table()
    elif menu_pick == 1:
        unit_pair = unit_picker()
        volume = beer_volume(unit_pair)
        aroma_intensity = intensity_level()
        vol_zest_aroma_ratio(unit_pair, aroma_intensity, volume)

print(main())