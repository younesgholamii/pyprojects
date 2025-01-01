import _datetime as dt


class Ticket:
    """for reserving the ticket"""

    id_list = [k for k in range(1, 10000)]
    empty_id_list = []
    days_list = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def __init__(self, nick_name, ages, chosen_sans):

        self.nick_name = nick_name
        self.age = ages
        self.chosen_sans = chosen_sans
        self.ticket_day = self.days_list[(dt.date.today().day % 7) - 1]

        if 0 < self.age <= 10 and chosen_sans in [(13, 14), (14, 15), (15, 16)]:
            self.model = 'model 1'
        elif 10 < self.age <= 20 and chosen_sans in [(16, 17), (17, 18), (18, 19)]:
            self.model = 'model 2'
        elif 20 < self.age and chosen_sans in [(19, 20), (20, 21)]:
            self.model = 'model 3'
        else:
            pass

    def get_id(self):
        """return an id for each ticket"""
        chosen_id = self.id_list[0]
        self.empty_id_list.append(self.id_list.remove(chosen_id))
        return chosen_id

    def ticket_print(self, ticket_ids, seat_numbers, device_name):
        """return a ticket for customer"""
        print()
        ticket = {'name': self.nick_name,
                  'ticket id': ticket_ids,
                  'seat number': seat_numbers,
                  'device name': device_name,
                  'program model': self.model,
                  'ticket day': self.ticket_day,
                  'game time': self.chosen_sans
                  }
        print('\n*********************************************')
        for i, j in ticket.items():
            print(f'{i}:  {j}')
        print('*********************************************\n')

    def check_for_right_sans(self, time_now):
        """check for valid age for chosen sans"""
        if 0 < self.age <= 10 and 13 <= time_now < 16:
            return True
        elif 10 < self.age <= 20 and 16 <= time_now < 19:
            return True
        elif 20 < self.age and 19 <= time_now < 21:
            return True
        else:
            return False
