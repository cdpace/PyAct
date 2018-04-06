class Actor:

    def __init__(self,key):
        self.key = key

    def call(self):
        print(self.key)