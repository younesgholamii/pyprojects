from re import fullmatch
from EndGame import *
from Ticket import *


national_code_dict = {}


def n_code_list(nationals_code, time):
    """save all person's national code"""
    national_code_dict.update({f'{nationals_code}': time})


def national_code_check(nationals_code):
    """check the national code to be 10 integer digits"""
    return False if fullmatch(r'\d{10}', f"{nationals_code}") else True


def New_Customer():
    while True:
        try:
            """choose a device and manage the exceptions"""
            device1 = int(input('\n[-1]-back [0]-hockey [1]-snooker [2]-carousel [3]-dragon device'
                                ' [4]-dart [5]-ping pong [6]-lucky box\ndevice:'))
            if device1 == -1:
                return None
            device = device_dict[device1]
            break

        except ValueError or IndexError:
            print('error!!!\nenter integer digit from 0 to 6')  # do not be character and out of list range
        except KeyError:
            print('this game is not available right now choose another one')

    name1 = input('name(-1 to back):')  # get customer name
    if name1 == '-1':
        return None

    while True:
        try:
            """get customer age"""
            age = int(input('age(-1 to back):'))
            if age == -1:
                return None
            if age <= 0:
                raise ValueError
            break

        except ValueError:
            print('error!!!\nenter a positive integer')  # do not be character or less than 0
            continue

    while True:
        try:
            """get customer national code"""
            national_code = int(input('national code(-1 to back):'))

            if national_code == -1:
                return None

            if national_code_check(national_code):      # being 10-digit number
                raise ValueError

            if f'{national_code}' not in national_code_dict.keys():  # check for not using a national code for two
                # devices
                break
            else:
                print("you can't choose another device for maximum of one hour.")
                return None

        except ValueError:
            print('error!!!\nenter a 10 digit integer')      # do not be less or more than 10 digit
            continue

    while True:
        try:
            """choose the suitable sans"""
            sans1 = int(input('[-1]-back [0]-(13, 14) [1]-(14, 15) [2]-(15, 16) [3]-(16, 17)'
                              '[4]-(17, 18) [5]-(18, 19) [6]-(19, 20) [7]-(20, 21)\nsans:'))
            sans = sans_list[sans1]

            if sans1 == -1:
                return None

            if sans[0] < dt.datetime.now().hour:    # do not choose past tense
                print('this sans already begin. choose another sans')
                continue

            if device.capacity[f'{sans}'] == 0:  # check for having free sans
                print('this sans is already filled. choose another sans.')
                continue
            print()
            name = Ticket(name1, age, sans)

            if name.check_for_right_sans(sans[0]):  # check for being suitable time for this age

                seat_number = device.giving_seat(sans)                  # get a seat number from seats list
                device.capacity[f'{sans}'] -= 1                         # minus the time capacity
                n_code_list(national_code, sans[0])                     # save the national code
                sans_dict[sans] += 1                                    # save that how much this sans sold?
                ticket_id = name.get_id()                               # get an id from ids list
                name.ticket_print(ticket_id, seat_number, device.game_name)  # print ticket for customer
                device.change_model_dict(name.model)                    # save that how much this model sold?
                break

            else:
                print('this sans is not suitable for your age.')

        except ValueError or IndexError:                  # do not be character or out of list range
            print('error!!!\nenter an integer number from 0 to 7')
