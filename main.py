from random import choice
from user import User


first_name_list = ['ali', 'reza', 'mani', 'sara']
last_number_list = ['amiri', 'karimi', 'naji', 'shahi']
phone_number_list = ['0912222', '0914444', '0913333', '0917777', '0915555']
if __name__ == "__main__":
    for phone in phone_number_list:
        User(choice(first_name_list), choice(last_number_list), phone)

    for user in User.obj_list:
        print(f'{user.id}\t {user.full_name}')
