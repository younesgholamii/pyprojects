from EndGame import *


def display_csv_content(day):
    """read the csv file"""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    if os.path.exists(f'E:/file save/{f'{day}_sale.csv'}'):
        print('\n*****************************************\n')
        print('this day sale:\n', pd.read_csv(f'E:/file save/{f'{day}_sale.csv'}', sep='\t'))
        print('\n*****************************************\n')
        print('the most sale of each model:\n', pd.read_csv(f'E:/file save/{day}_device_models_sale.csv', sep='\t'))
        print('\n*****************************************\n')
        print(pd.read_csv(f'E:/file save/{day}_most_models_sale.csv', sep='\t'))
        print('\n*****************************************\n')
        print(pd.read_csv(f'E:/file save/{day}_most_device_sale.csv', sep='\t'))
        print('\n*****************************************\n')
        print(pd.read_csv(f'E:/file save/{day}_crowded_sans.csv', sep='\t'))
        print('\n*****************************************\n')
    else:
        print('\nyou have no information in this day.')


def setting():
    """every thing that should happen in setting"""

    while True:
        """choose an option"""
        try:
            option = int(input("\nchoose a setting option:\n1-today info\n2-last days info\n3-delete a game"
                               "\n4-each models sale\n5-most model sale"
                               "\n6-most device sale\n7-popular times\n8-back\noption:"))
            print()

        except ValueError:
            print('\nerror!!!\nenter an integer between 1 to 8\n')

            """show the sales up to now"""

        if option == 1:
            today = days_list[(dt.datetime.now().day % 7) - 1]
            total = {}
            for device in device_dict.values():
                total.update({f'{device.game_name}': sum(device.models_sale.values()) * device.price})
            total_day_sale = sum(total.values())
            print('today sale up to now: ', total_day_sale)

            """show last days information"""

        elif option == 2:
            day = int(input('which day you wanna see?\n1-sat\n2-sun\n3-mon\n4-tue\n5-wed\n6-thu\n7-fri\noption:'))
            if 1 <= day <= 7:
                todays = days_list[day - 1]
                display_csv_content(todays)
            else:
                print('enter an integer between 1 and 7.')

            """delete a game from games list"""

        elif option == 3:
            deleted_item = int(input('which item you wanna delete?\n'
                                     '[0]-hockey [1]-snooker [2]-carousel [3]-dragon device'
                                     '[4]-dart [5]-ping pong [6]-lucky box\nitem:'))
            del device_dict[deleted_item]

            """show each models sale"""

        elif option == 4:
            for device in device_dict.values():
                for model in device.models_sale.keys():
                    print(f'{model} at {device.game_name}: {device.models_sale[f'{model}'] * device.price}', end=', ')
                print()

            """show the model that have most sale"""

        elif option == 5:
            model1_sale, model2_sale, model3_sale = 0, 0, 0
            for device in device_dict.values():
                model1_sale += device.models_sale['model 1']
                model2_sale += device.models_sale['model 2']
                model3_sale += device.models_sale['model 3']
            result1 = {'model 1': model1_sale, 'model 2': model2_sale, 'model 3': model3_sale}
            result = max(model1_sale, model2_sale, model3_sale)
            if result != 0:
                print('most model sale: ', max(result1), 'with', result, 'sale')
            else:
                print('there is no sale')

            """the most device sale"""

        elif option == 6:
            device_sale = {}
            for device in device_dict.values():
                device_sale.update({f'{device.game_name}': sum(device.models_sale.values()) * device.price})

            most_device_sale = max(device_sale, key=device_sale.get)
            print(device_sale)
            if device_sale[most_device_sale] != 0:
                print('most device sale: ', most_device_sale)
            else:
                print('there is no sale')

            """show the most popular time"""
        elif option == 7:
            if max(sans_dict.values()) != 0:
                print('most sale sans:', max(sans_dict, key=sans_dict.get), f'with {max(sans_dict.values())} sale')
            else:
                print('there is no sale.')

        elif option == 8:
            break

        else:
            print("invalid input ! please try again")


def report():
    """show the times with their capacities at the moment"""

    report_dict = {}
    for time in sans_list:
        report_dict.update({f'{time}': {}})
    for time1 in sans_list:
        for device in device_dict.values():
            report_dict[f'{time1}'].update({f'{device.game_name}': device.capacity[f'{time1}']})
    df = pd.DataFrame.from_dict(report_dict, orient='index', columns=device_list)
    print(df)
