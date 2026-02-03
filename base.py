from abc import ABC


class BaseClass(ABC):
    _id = 0
    obj_list = list()

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)
        super().__init__(*args, *kwargs)

    @classmethod
    def store(cls, self):
        cls.obj_list.append(self)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id
