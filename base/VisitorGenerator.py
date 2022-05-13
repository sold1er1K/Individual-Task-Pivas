import CoffeeHouse
from Settings import Settings
from Visitor import Visitor


class VisitorGenerator:
    def __init__(self, model: CoffeeHouse):
        self.model = model
        self.nextActionTime = 0
        self.request = Settings()

    def proccess(self, currentTime: int):
        if self.nextActionTime <= currentTime:
            visitor = self.generateVisitor()
            self.nextActionTime += self.request.VISITOR_WAITING_TIME
            print('Time={} Generate visitor {}'.format(currentTime, visitor))

    def generateVisitor(self):
        return Visitor(self.model)
