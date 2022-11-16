import time

class Helloworld:
    count = 0
    ids_list = []

    @classmethod
    def is_id_valid(cls, i):
        is_valid = False
        if i.is_integer() and not i in cls.ids_list :
            is_valid = True
        return is_valid


    def __init__(self, i):
        if Helloworld.is_id_valid(i):
            self.id = i
            Helloworld.count += 1
            Helloworld.ids_list.append(i)
        else:
            print(f'{i} is taken, assigning timestamp...')
            self.id = int(time.time()) + 42
        
    def __repr__(self):
        return f'Not one more hello world! {self.id}'
