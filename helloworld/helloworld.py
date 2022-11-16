import time

class Helloworld:
    count = 0
    ids_list = []

    @classmethod
    def is_id_taken(cls, i):
        if (i in cls.ids_list):
            return True

 
    def __init__(self, i):
        if not Helloworld.is_id_taken(i):
            self.id = i
            Helloworld.count += 1
            Helloworld.ids_list.append(i)
        else:
            self.id = int(time.time())
        
    def __repr__(self):
        return f'Another helloworld {self.id}'
    