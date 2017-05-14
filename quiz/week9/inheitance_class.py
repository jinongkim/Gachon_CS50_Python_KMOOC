class Subject(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Math(Subject):
    def say(self):
        print("힘내")