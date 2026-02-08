class Manager:
    def __init__(self, _class):
        self._class = _class

    def __str__(self):
        return f'Manager: {self._class}'

    def search(self, **kwargs):
        """
        for search in objects
        :param kwargs:
        :return:objects target
        """
        result = list()
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    result.append(obj)

        return result

    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    return obj
        return False
