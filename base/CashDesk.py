import Worker
import Visitor


class CashDesk:
    def __init__(self):
        self.worker: Worker = None
        self.visitorList = []

    def getWorker(self):
        return self.worker

    def setWorker(self, worker: Worker):
        self.worker = worker

    def addVisitorToQue(self, visitor: Visitor):
        self.visitorList.append(visitor)

    def getFirstVisitor(self):
        if len(self.visitorList) != 0:
            return self.visitorList[0]

    def getVisitorList(self):
        return self.visitorList

    def removeVisitor(self, visitor: Visitor):
        self.visitorList.remove(visitor)
