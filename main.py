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
    avg_weights_after_peeling_kg = {'orange': 0.22, 'grapefruit': 0.239, 'lemon': 0.118, 'lime': 0.111, 'tangerine': 0.118}
    return avg_weights_after_peeling_kg


def zest_from_one_fruit_grams(fruits_avg_weights_grams, fruit_avg_weight_after_peeling_grams):
    before_peeling = fruits_avg_weights_grams()
    after_peeling = fruit_avg_weight_after_peeling_grams()
    single_fruit_zest_g = {key: before_peeling[key] - after_peeling.get(key, 0) for key in before_peeling}
    return single_fruit_zest_g


def zest_from_one_fruit_kilograms(fruits_avg_weights_kilograms, fruit_avg_weight_after_peeling_kilograms):
    before_peeling = fruits_avg_weights_kilograms()
    after_peeling = fruit_avg_weight_after_peeling_kilograms()
    single_fruit_zest_kg = {key: before_peeling[key] - after_peeling.get(key, 0) for key in before_peeling}
    return single_fruit_zest_kg


def display_fruits_table():
    while True:
        fruit_table = tabulate.tabulate(zip(fruits_avq_diameter_cm().keys(), fruits_avg_weights_grams().values(),
                                            fruits_avg_weights_kilograms().values(),
                                            fruits_avq_diameter_cm().values()),
                                        headers=['Fruit', 'Avg. Weight (g)', 'Avg. Weight (kg)', 'Avg. Diameter (cm)'],
                                        tablefmt='fancy_grid')

        print(fruit_table, '\n')
        go_back_func(main)


def intensity_level():
    while True:
        print('Choose desired level of citrus zest aroma.')
        try:
            print('1. Low\n2. Medium\n3. High\n4. Very high')
            aroma_intensity = int(input('\nPick an aroma intensity level [1-4]:\n>>> '))
            if aroma_intensity == 1:
                print('\nYou picked low aroma intensity.\n')
                return aroma_intensity
            elif aroma_intensity == 2:
                print('\nYou picked medium aroma intensity.\n')
                return aroma_intensity
            elif aroma_intensity == 3:
                print('\nYou picked high aroma intensity.\n')
                return aroma_intensity
            elif aroma_intensity == 4:
                print('\nYou picked very high aroma intensity.\n')
                return aroma_intensity
            else:
                print('\nInvalid input. Value must be integer. Pick a level in range [1-4].')
        except ValueError:
            print('\nInvalid input. Value must be integer. Pick a level in range [1-4].')
            continue


def go_back_func(func):
    while True:
        try:
            go_back = input('\nDo you want to return to main menu? [Y/N]\n>>>')
            if go_back == 'y'.lower():
                print('\n')
                print(func())
            elif go_back == 'n'.lower():
                print('\n')
                break
        except ValueError:
            continue


def about_program():
    while True:
        print("ZEST CALCULATOR FOR CRAFT BREWERIES allows you to calculate amount of citrus fruits you need to buy for "
              "your beer.\nProgram will calculate how many fruits you should buy to produce specific amount of zest to "
              "get desired level of aroma intensity\nGrams of zest per liter of beer is based on my own experience. "
              "The program assumes 15-40 minutes whirpool addition.\nZEST CALCULATOR FOR CRAFT BREWERIES will allow you"
              " to send an email with an order to your supplier and save a copy of it on your computer\nCHEERS!!!\n"
              )
        go_back_func(main)


def main_menu():
    print("[1] Calculate amount of zest you need\n[2] Display citrus fruits table. \n[3] About program\n[4] Exit\n")
    while True:
        try:
            menu_pick = int(input('What do you want to do? Pick a number [1 - 4]:\n>>> '))
            print('\n')
            if 1 <= menu_pick <= 4:
                return menu_pick
        except ValueError:
            continue


def unit_picker():
    while True:
        print('Choose your units:\n[1] Hectoliters and Kilograms\n[2] Liters and Grams\n[3] Main menu')
        try:
            unit_pair = int(input('Pick a unit pair [1-2] or go back to main menu [3]:\n>>> '))
            if 1 <= unit_pair <= 3:
                if 1 <= unit_pair <= 2:
                    return unit_pair
                elif unit_pair == 3:
                    go_back_func(main)
            else:
                print('Invalid input.\n')
                continue
        except ValueError:
            print('\nInvalid input.\n')
            continue


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
                print('Invalid input. Please enter positive integer')
                continue
            if beer_volume <= 0:
                print('Invalid input. Please enter positive integer.')
                continue
            else:
                print('\n')
                return beer_volume
        elif unit_pair == 2:
            try:
                beer_volume = float(input('Enter beer volume in liters: '))
            except ValueError:
                print('Invalid input. Please enter positive integer.')
                continue
            if beer_volume <= 0:
                print('Invalid input. Please enter positive integer.')
                continue
            else:
                print('\n')
                return beer_volume


def vol_zest_aroma_ratio(unit_pair, aroma_intensity, volume):
    low_ratio = [0.5, 1]
    medium_ratio = [1, 1.5]
    high_ratio = [1.5, 2]
    very_high_ratio = [2, 2.5]
    zest_range = []
    if unit_pair == 1:
        if aroma_intensity == 1:
            for ratio in low_ratio:
                zest = (volume * ratio)/10
                zest_range.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume,
                                                                                                       zest_range[0],
                                                                                                       zest_range[1]))
            return zest_range
        if aroma_intensity == 2:
            for ratio in medium_ratio:
                zest = (volume * ratio)/10
                zest_range.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume,
                                                                                                       zest_range[0],
                                                                                                       zest_range[1]))
            return zest_range
        if aroma_intensity == 3:
            for ratio in high_ratio:
                zest = (volume * ratio)/10
                zest_range.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume,
                                                                                                       zest_range[0],
                                                                                                       zest_range[1]))
            return zest_range
        if aroma_intensity == 4:
            for ratio in very_high_ratio:
                zest = (volume * ratio)/10
                zest_range.append(zest)
            print("To infuse {} hectoliters of beer you need {}-{} kilograms of zest in total.".format(volume,
                                                                                                       zest_range[0],
                                                                                                       zest_range[1]))
            return zest_range
    if unit_pair == 2:
        if aroma_intensity == 1:
            for ratio in low_ratio:
                zest = volume * ratio
                zest_range.append(zest)
            print("To infuse {} liters of beer you need {}-{} grams of zest in total.".format(volume, zest_range[0],
                                                                                              zest_range[1]))
            return zest_range
        if aroma_intensity == 2:
            for ratio in medium_ratio:
                zest = volume * ratio
                zest_range.append(zest)
            print("To infuse {} liters of beer you need {}-{} grams of zest in total.".format(volume, zest_range[0],
                                                                                              zest_range[1]))
            return zest_range
        if aroma_intensity == 3:
            for ratio in high_ratio:
                zest = volume * ratio
                zest_range.append(zest)
            print("To infuse {} liters of beer you need {}-{} grams of zest in total.".format(volume, zest_range[0],
                                                                                              zest_range[1]))
            return zest_range
        if aroma_intensity == 4:
            for ratio in very_high_ratio:
                zest = volume * ratio
                zest_range.append(zest)
            print("To infuse {} liters of beer you need {}-{} grams of zest in total.".format(volume, zest_range[0],
                                                                                              zest_range[1]))
            return zest_range




def main():

    print(welcome_func())
    menu_pick = main_menu()
    if menu_pick == 4:
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
        zest_range = vol_zest_aroma_ratio(unit_pair, aroma_intensity, volume)


def choose_fruits_and_amount():
    chosen_fruits = set()
    fruit = fruits_avg_weights_grams().keys()
    menu = (list(enumerate(fruit)))
    for option in menu:
        print('[{}] {}'.format(option[0]+1, option[1]))

    print('[{}] Aprove list of fruits and proceed'.format(len(menu)+1))
    print('[{}] Go back to main menu'.format(len(menu)+2))

    while True:

        try:
            pick = int(input('Add fruit [1-5]. Enter [6] to approve list of fruits or enter '
                             '[7] to go back to main menu: '))
            if pick == 7:
                go_back_func(main)
            elif 1 <= pick <= 5:
                chosen_fruits.add(menu[pick-1][1])
                print('You have added {} to the list of fruits.'.format(menu[pick-1][1]))
            elif pick == 6:
                break
            else:
                print('Invalid input. Please try again.')
                continue
        except ValueError:
            print('Invalid input. Please try again.')
            continue

    print('You have chosen following fruits: {}'.format(chosen_fruits))


print(choose_fruits_and_amount())