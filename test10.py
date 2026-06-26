class Bird:
    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Penguin swim faster")
peggy=Penguin()
peggy.whoisthis()
peggy.run()
peggy.swim()
