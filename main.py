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
    avg_weights_after_peeling_g = {'orange': 220, 'grapefruit': 239, 'lemon': 118,
                                   'lime': 111, 'tangerine': 118}

    return avg_weights_after_peeling_g


def fruit_avg_weight_after_peeling_kilograms():
    avg_weights_after_peeling_kg = {'orange': 0.22, 'grapefruit': 0.239, 'lemon': 0.118,
                                    'lime': 0.111, 'tangerine': 0.118}

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


def welcome_func():
    welcome_txt = '>>>Welcome to ZEST CALCULATOR FOR CRAFT BREWERIES!!!<<<\n'
    len_welcome_txt = len(welcome_txt)
    star = '*'
    welcome = (welcome_txt + star * len_welcome_txt + '\n')
    return welcome


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
              "The program assumes 15-40 minutes whirlpool addition.\nZEST CALCULATOR FOR CRAFT BREWERIES will allow you"
              " to send an email with an order to your supplier and save a copy of it on your computer\nCHEERS!!!\n"
              )
        go_back_func(main)


def main_menu():
    print("[1] Calculate amount of zest you need\n[2] Display citrus fruits table. \n[3] About program\n[4] Exit\n")
    while True:
        menu_pick = input('What do you want to do? Pick a number [1 - 4]:')
        try:
            menu_pick = int(menu_pick)
            if 1 <= menu_pick <= 4:
                print('\n')
                return menu_pick
            else:
                print("Enter integer value 1-4")
        except ValueError:
            print("Enter integer value 1-4")



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


def beer_volume(unit_pair):
    while True:
        if unit_pair == 1:
            try:
                beer_vol = float(input('Enter beer volume in hectoliters: '))
            except ValueError:
                print('Invalid input. Please enter positive integer')
                continue
            if beer_vol <= 0:
                print('Invalid input. Please enter positive integer.')
                continue
            else:
                print('\n')
                return beer_vol
        elif unit_pair == 2:
            try:
                beer_vol = float(input('Enter beer volume in liters: '))
            except ValueError:
                print('Invalid input. Please enter positive integer.')
                continue
            if beer_vol <= 0:
                print('Invalid input. Please enter positive integer.')
                continue
            else:
                print('\n')
                return beer_vol


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


def choose_fruits_and_amount():
    chosen_fruits = set()
    fruit = list(fruits_avg_weights_grams().keys())
    fruit.sort()
    menu = list(enumerate(fruit))
    print('\n')
    print('CHOOSE CITRUSES!!!\n')
    for option in menu:
        print('[{}] {}'.format(option[0] + 1, option[1]))
    print('[{}] Approve list of fruits and proceed'.format(len(menu) + 1))
    print('[{}] Clear list of fruits and start over again'.format(len(menu) + 2))
    print('[{}] Go back to main menu\n'.format(len(menu) + 3))

    while True:
        try:
            pick = int(input('>>>'))
            if pick == 8:
                go_back_func(main)
                fruit = list(fruits_avg_weights_grams().keys())
                fruit.sort()
                menu = list(enumerate(fruit))
                print('CHOOSE CITRUSES!!!\n')
                for option in menu:
                    print('[{}] {}'.format(option[0] + 1, option[1]))
                print('[{}] Approve list of fruits and proceed'.format(len(menu) + 1))
                print('[{}] Clear list of fruits and start over again'.format(len(menu) + 2))
                print('[{}] Go back to main menu\n'.format(len(menu) + 3))
            elif pick == 7:
                chosen_fruits.clear()
                print('List cleared! Choose your fruits again!\n')
                fruit = list(fruits_avg_weights_grams().keys())
                fruit.sort()
                menu = list(enumerate(fruit))
                menu = list(enumerate(fruit))
                print('CHOOSE CITRUSES!!!\n')
                for option in menu:
                    print('[{}] {}'.format(option[0] + 1, option[1]))
                print('[{}] Approve list of fruits and proceed'.format(len(menu) + 1))
                print('[{}] Clear list of fruits and start over again'.format(len(menu) + 2))
                print('[{}] Go back to main menu\n'.format(len(menu) + 3))
            elif 1 <= pick <= 5:
                chosen_fruits.add(menu[pick - 1][1])
                print('You have added {} to the list of fruits.\n'.format(menu[pick - 1][1]))
            elif pick == 6:
                return chosen_fruits
            else:
                print('Invalid input. Please try again.')
                continue
        except ValueError:
            print('Invalid input. Please try again.')
            continue


def enter_zest_amount(chosen_fruits, unit_pair, zest_range):  # NEEDS REFACTORING
    srtd_list_chosen_fruits = sorted(list(chosen_fruits))
    list_of_chosen_fruits_dicts = [{fruit: 0} for fruit in srtd_list_chosen_fruits]
    current_sum = 0
    if unit_pair == 1:
        while True:
            print('Current sum of zest is {} kg'.format(current_sum))
            print(list_of_chosen_fruits_dicts)
            print("You need {}-{} kg of zest".format(zest_range[0], zest_range[1]))
            print('Enter name of citrus or type "MENU" to go back to main menu"')
            name = input('>>>')
            if name.lower() == 'menu':
                go_back_func(main)

            elif name in srtd_list_chosen_fruits:
                print("Enter amount of zest in kilograms. Use '-' to subtract from current amount.")
                amount = float(input('>>>'))
                if current_sum + amount < 0:
                    print('Negative zest amount is not allowed.')
                    continue
                else:
                    for fruit_dict in list_of_chosen_fruits_dicts:
                        if name in fruit_dict:
                            fruit_dict[name] += amount
                            current_sum = sum([list(x.values())[0] for x in list_of_chosen_fruits_dicts])
                print('{:-^75}\n'.format('Enter another citrus'))

            else:
                print('Invalid input. Please try again.')
                continue
            if zest_range[0] <= current_sum <= zest_range[1]:
                print("You have reached the desired amount of zest.")
                print("You can proceed by typing 'DONE' or keep modifying amount of zest ")

            elif current_sum < zest_range[0]:
                print("Not enough zest yet. You need to add more.")
            elif current_sum > zest_range[1]:
                print("Too much zest. You need to remove some.")



def main():

    while True:
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
            chosen_fruits = choose_fruits_and_amount()
            enter_zest_amount(chosen_fruits, unit_pair, zest_range)


if __name__ == '__main__':
    main()