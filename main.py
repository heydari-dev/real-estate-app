from sample import create_samples
from advertisment import (
    ApartmentSell, HouseSell, StoreSell
)


class Handler:

    ADVERTISEMENT_TYPES = {
        1: ApartmentSell, 2: HouseSell, 3: StoreSell,
        # 4: ApartmentRent, 5: HouseRent, 6: StoreRent
    }

    SWITCHES = {
        'r': 'get_report',
        'g': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())
            print('-' * 30)

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            for obj in adv.objects_list:
                obj.show_detail()
                print('-'*30)

    def run(self):
        print(f'Hello World...!')
        for key in self.SWITCHES:
            print(f'press: {key} for {self.SWITCHES[key]}')
        user_input = input(f'Enter your choice: ')
        print('-' * 30)
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print('Invalid input...')
            print('-' * 30)
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == '__main__':
    create_samples()
    Handler().run()
