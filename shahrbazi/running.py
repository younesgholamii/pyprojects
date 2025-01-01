import time
from New_Customer import *
from setting import *
import threading
from EndGame import flag


def remove_national_code():
    """delete the national code that have no time anymore"""
    current_time = dt.datetime.now().hour
    for code, last_time in list(national_code_dict.items()):
        if current_time - last_time == 1:
            del national_code_dict[code]


def run_schedular():
    """check the national code dictionary each 5 minute."""
    while flag:
        remove_national_code()
        time.sleep(300)


"""make a thread for doing two while's side by side"""
scheduler_thread = threading.Thread(target=run_schedular)
scheduler_thread.start()


while True:
    try:
        option = int(input('\n1-new customer\n2-settings\n3-devices list with their capacity\n4-end program\noption:'))
    except ValueError:
        print('error!!!\nenter an integer digit between 1 to 4')
        continue

    if option == 1:
        New_Customer()

    elif option == 2:
        setting()

    elif option == 3:
        report()

    elif option == 4:
        try:
            make_sure = int(input('are you sure to exit?([0]-no  [1]-yes)'))

        except ValueError:
            print('error!!!\nenter 1 or 0.')
            continue
        if make_sure == 0:
            continue
        else:
            endgame()
        break

    else:
        print('enter a number between 1 to 4')
        continue
