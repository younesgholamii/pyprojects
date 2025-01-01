from Game import *
import csv
import os
import datetime as dt
from Ticket import *
import pandas as pd


def save_to_csv(data, filename):
    """save files that must be saved"""
    df = pd.DataFrame({'date': [dt.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')]})
    df.to_csv(f'E:/file save/{filename}', index=False, quotechar='"')

    if os.path.exists(f'E:/file save/{filename}'):
        with open(f'E:/file save/{filename}', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for devices, sales in data.items():
                writer.writerow([devices, sales])

    else:
        with open(f'E:/file save/{filename}', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(f'\n{dt.datetime.now()}')
            for devices, sales in data.items():
                writer.writerow([devices, sales])


days_list = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']


flag = True
try:
    def endgame():
        """show and save each device sale at day"""

        today = days_list[(dt.datetime.now().day % 7) - 1]
        total_day_sale = {}
        for device in device_dict.values():
            total_day_sale.update({f'{device.game_name}': (sum(device.models_sale.values()) * device.price)})
        print('\n', total_day_sale)

        file_name1 = f'{today}_sale.csv'
        save_to_csv(total_day_sale, file_name1)
        print('\n___________________________________________________________________\n')

        """show and save each model of each device sale"""

        total_model_sale = {'model 1': {}, 'model 2': {}, 'model 3': {}}
        for device in device_dict.values():
            for model in device.models_sale.keys():
                total_model_sale[f'{model}'].update({f'{device.game_name}': device.models_sale[f'{model}'] * device.price})
        df = pd.DataFrame.from_dict(total_model_sale, orient='index', columns=device_list)
        print(df)

        file_name2 = f'{today}_device_models_sale.csv'
        save_to_csv(total_model_sale, file_name2)
        print('\n___________________________________________________________________\n')

        """show and save the most sale for models"""

        model1_sale, model2_sale, model3_sale = 0, 0, 0
        for device in device_dict.values():
            model1_sale += device.models_sale['model 1']
            model2_sale += device.models_sale['model 2']
            model3_sale += device.models_sale['model 3']
        result = {'model1': model1_sale, 'model2': model2_sale, 'model3': model3_sale}
        result2 = max(result, key=result.get)
        print('most model sale: ', result2)

        file_name3 = f'{today}_most_models_sale.csv'
        save_to_csv({'the most model sale: ': result2}, file_name3)
        print('\n___________________________________________________________________\n')

        """show and save the most device sale"""

        device_sale = {}

        for device in device_dict.values():
            device_sale.update({f'{device.game_name}': (sum(device.models_sale.values()) * device.price)})
        most_device_sale = max(device_sale, key=device_sale.get)
        print('most device sale: ', most_device_sale)

        file_name4 = f'{today}_most_device_sale.csv'
        save_to_csv({'the most device sale: ': most_device_sale}, file_name4)
        print('\n___________________________________________________________________\n')

        """show and save the crowded sans"""

        print('crowded sans: ', max(sans_dict))

        file_name5 = f'{today}_crowded_sans.csv'
        save_to_csv({'crowded time: ': max(sans_dict)}, file_name5)
finally:
    flag = False
