from animal import Animal

class Horse(Animal):
    speed = 0

    def __init__(self, weight, hair, speed):
        super().__init__(weight, hair)
        self.speed = speed
    
    def race(self):
        moving = self.speed
        print("The horse is fast, and runs away from you at " + str(moving) + "mph.")

        return self.speed