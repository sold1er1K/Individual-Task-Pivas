import CoffeeHouse
import random
from enum import Enum
from Settings import Settings
import Product
from VisitorRequestStatus import VisitorRequestStatus


class Visitor:
    def __init__(self, model: CoffeeHouse):
        self.model = model
        menu = model.getMenu()
        self.desiredProduct = menu.get(random.randint(0, len(menu)))
        self.cashDeskList = model.getCashDeskList()
        self.cashDesk = self.cashDeskList.get(random.randint(0, len(self.cashDeskList)))
        self.cashDesk.addVisitorToQue(self)
        self.nextActionTime = 0
        self.settings = Settings()
        self.request = VisitorRequestStatus(Enum)
        self.successRating = 5

    def process(self, currentTime: int):
        if self.nextActionTime == 0:
            self.nextActionTime = currentTime + self.settings.getVisitorWaitingTime()

        if currentTime >= self.nextActionTime:
            self.model.addRaiting(0)
            self.model.visitorLeave(self)
            print('Time={} Visitor leave by timeout {}'.format(currentTime, self))

    def askDesiredProduct(self, currentTime: int):
        requestStatus = self.model.requestProduct(self.desiredProduct)
        if requestStatus == self.request.SUCCESS:
            self.model.takeProduct(self.desiredProduct)
            self.model.addRaiting(self.successRating)
            self.model.visitorLeave(self)
            print('Time={} Visitor({}) leave with product {}'.format(currentTime, hash(self), self.desiredProduct))
        elif requestStatus == self.request.PRODUCT_MISSING:
            self.failDesiredProduct(currentTime, self.desiredProduct)

    def givePreparedProduct(self, currentTime: int, product: Product):
        self.model.addRating(self.successRating)
        self.model.visitorLeave(self)
        print('Time={} Visitor({}) leave with product {}'.format(currentTime, hash(self), product))

    def failDesiredProduct(self, currentTime: int, product: Product):
        self.model.addRating(1)
        self.model.visitorLeave(self)
        print('Time={} Visitor({}) leave without product {}'.format(currentTime, hash(self), product))

    def getDesiredProduct(self):
        return self.desiredProduct

    def getCashDesk(self):
        return self.cashDesk

    def toString(self):
        builder = 'Visitor({}) desiredProduct=[{}] queuePos={}'.format(hash(self), self.desiredProduct,
                                                                     self.cashDesk.getVisitorList().index(self))
        return builder

