#object and class
class parent:
    name = 'bmw'
    gear = 5
    def info(self):
        print("the car gear is :",self.gear)
    def info_2(self):
        print("The car name is :",self.name)
obj = parent()
obj.info_2()
obj.info()

