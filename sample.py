from random import choice
from user import User
from estate import Apartment, House, Store
from region import Region
from advertisment import ApartmentSell, HouseSell, StoreSell


first_name_list = ['ali', 'reza', 'mani', 'sara']
last_number_list = ['amiri', 'karimi', 'naji', 'shahi']
phone_number_list = ['0912222', '0914444', '0913333', '0917777', '0915555']


def create_samples():
    for phone in phone_number_list:
        User(choice(first_name_list), choice(last_number_list), phone)

    reg1 = Region(name='R1')

    apt1 = Apartment(
        user=User.objects_list[0], area=80, rooms_count=2, built_year=1390,
        region=reg1, address='La ST...', has_elevator=True, has_parking=True,
        floor=1
    )

    house1 = House(
        user=User.objects_list[3], area=100, rooms_count=3, built_year=1350,
        region=reg1, address='La ST...', has_yard=True, floors_count=4,
    )

    store1 = Store(
            user=User.objects_list[-1], area=100, rooms_count=3,
            built_year=1350, region=reg1, address='La ST...'
        )

    apt_sell = ApartmentSell(
        user=User.objects_list[0], area=80, rooms_count=2, built_year=1390,
        region=reg1, address='La ST...', has_elevator=True, has_parking=True,
        floor=1, price_per_meter=10, discountable=True, convertable=False
    )

    house_sell = HouseSell(
        user=User.objects_list[3], area=100, rooms_count=3, built_year=1350,
        region=reg1, address='La ST...', has_yard=True, floors_count=4,
        price_per_meter=10, discountable=True, convertable=False
    )

    store_sell = StoreSell(
        user=User.objects_list[-1], area=100, rooms_count=3,
        built_year=1350, region=reg1, address='La ST...',
        price_per_meter=10, discountable=True, convertable=False
    )

    print('#'*10+' Sample created '+'#'*10)

