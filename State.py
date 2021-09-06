#A class with table and a father
class  State:
    def __init__(self, table, father=None):
        self.father = father
        self.table = table
