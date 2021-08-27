class Tictactoe:
    def __init__(self):
        self.x = input('Enter number: ')
        self.data_store = {}

    def print_pattern(self):
        print(f"{self.data_store.get(7,' ')}|{self.data_store.get(8,' ')}|{self.data_store.get(9,'')}")
        print(f'-+-+-')
        print(f"{self.data_store.get(4,' ')}|{self.data_store.get('5',' ')}|{self.data_store.get(6,'')}")
        print(f'-+-+-')
        print(f"{self.data_store.get('1',' ')}|{self.data_store.get(2,' ')}|{self.data_store.get(3,'')}")


    def logic(self):
        if self.x not in self.data_store:
            self.data_store[self.x] =  'x'
            self.data_store['1'] = 'y'

