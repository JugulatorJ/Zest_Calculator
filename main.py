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
        fruit_table = tabulate.tabulate(zip(fruits_names(), fruits_avg_weights_grams().values(), fruits_avg_weights_kilograms().values(),
                        fruits_avq_diameter_cm().values()), headers=['Fruit', 'Avg. Weight (g)', 'Avg. Weight (kg)', 'Avg. Diameter (cm)'],
                        tablefmt='fancy_grid')
        print(fruit_table, '\n')
        go_back_func()


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
        except:
            print('\nInvalid input. Value must be integer. Pick a level in range [1-4].')
            continue


def go_back_func():
    while True:
        try:
            go_back = input('\nDo you want to return to main menu? [Y/N]\n>>>')
            if go_back == 'y'.lower():
                print('\n')
                main()
                break
            elif go_back == 'n'.lower():
                print('\n')
                break
        except ValueError:
            continue

def about_program():
    while True:
        print("ZEST CALCULATOR FOR CRAFT BREWERIES allows you to calculate amount of citrus fruits you need to buy for your beer.\n"
              "Program will calculate how many fruits you should buy to produce specific amount of zest to get desired level of aroma intensity\n"
              "Grams of zest per liter of beer is based on my own experience. The program assumes 15-40 minutes whirpool addition.\n"
              "ZEST CALCULATOR FOR CRAFT BREWERIES will allow you to send an email with an order to your supplier and save a copy of it on your computer\n"
              "CHEERS!!!\n"
              )
        go_back_func()




def main_menu():
    print("1. Calculate amount of zest you need\n2. Display citrus fruits table. \n3. About program\n4. Exit\n")
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
        print('Choose your units:\n1. Hectoliters and Kilograms\n2. Liters and Grams\n')
        try:
            unit_pair = int(input('Pick a unit pair [1-2]:\n>>> '))
            if 1 <= unit_pair <= 2:
                return unit_pair
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