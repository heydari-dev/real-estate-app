
class Melk:
    listobject = []

    def __init__(self, foroshande, metraj, salsakht, type, listobject):
        self.foroshande = foroshande
        self.metraj = metraj
        self.salsakht = salsakht
        self.type = type
        listobject.append(self)

class Vila(Melk):
    def __init__(self, foroshande, metraj, salsakht, type, hayat):
        self.hayat = hayat
        super().__init__(foroshande, metraj, salsakht, type)

    def vilafiles(self, listobject):
        return listobject


class Apartment(Melk):
    def __init__(self, foroshande, metraj, salsakht, type, tabaghe):
        super().__init__(foroshande, metraj, salsakht, type)
        self.tabaghe = tabaghe


class Shop(Melk):
    def __init__(self, foroshande, metraj, salsakht, type):
        super().__init__(foroshande, metraj, salsakht, type)


if __name__ == '__main__':
    vilafile1 = Vila('ali', 70, 55, 'maskoni', True)
    vilafile2 = Vila('amir', 78, 44, 'maskoni', False)
    files = {
            'foroshande': self.foroshande, 'metraj': self.metraj,
            'salsakht': self.salsakht, 'type': self.type, 'hayat': self.hayat
        }
    resultfile = vilafile1.vilafiles()
    resultfile = vilafile2.vilafiles()

    print(resultfile)
