class Game:
    """do the all changes at the moment"""

    def __init__(self, game_name, capacity, price, sans_lists):

        self.models_sale = {'model 1': 0, 'model 2': 0, 'model 3': 0}
        self.test = capacity + 1        # help for seat number
        self.capacity = {f'{sans}': capacity for sans in sans_lists}
        self.price = price
        self.game_name = game_name

    def giving_seat(self, sans):
        """giving a free seat to the customer"""
        chosen_seat = self.test - self.capacity[f'{sans}']
        return chosen_seat

    def change_model_dict(self, model):
        """change the model sale dictionary value"""
        self.models_sale[f'{model}'] += 1


sans_list = [(13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21)]
sans_dict = {(13, 14): 0, (14, 15): 0, (15, 16): 0, (16, 17): 0, (17, 18): 0, (18, 19): 0, (19, 20): 0, (20, 21): 0}

hockey = Game('hockey', 2, 10000, sans_list)
snooker = Game('snooker', 2, 20000, sans_list)
carousel = Game('carousel', 15, 30000, sans_list)
dragon_device = Game('dragon', 10, 55000, sans_list)
dart = Game('dart', 4, 3000, sans_list)
ping_pong = Game('ping pong', 2, 25000, sans_list)
lucky_box = Game('lucky box', 6, 18000, sans_list)

device_dict = {0: hockey, 1: snooker, 2: carousel, 3: dragon_device, 4: dart, 5: ping_pong, 6: lucky_box}
device_list = ['hockey', 'snooker', 'carousel', 'dragon', 'dart', 'ping pong', 'lucky box']
