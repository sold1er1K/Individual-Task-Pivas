class Settings:
    def __init__(self):
        self.TICK_TIME = 300
        self.CLOSING_TIME = 21600
        self.VISITOR_GENERATE_TIME_PERIOD = 900
        self.VISITOR_WAITING_TIME = 3000

    def getTickTime(self):
        return self.TICK_TIME

    def getClosingTime(self):
        return self.CLOSING_TIME

    def getVisitorGenerateTimePeriod(self):
        return self.VISITOR_GENERATE_TIME_PERIOD

    def getVisitorWaitingTime(self):
        return self.VISITOR_WAITING_TIME
