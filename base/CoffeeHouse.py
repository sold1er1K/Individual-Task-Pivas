from Settings import Settings
import VisitorGenerator
import CashDesk
import Visitor
import Product
import Recipe
import Ingredient
from VisitorRequestStatus import VisitorRequestStatus


class CoffeeHouse:
    def __init__(self):
        self.currentTime = 0
        self.request = Settings()
        self.visitorGenerator: VisitorGenerator = None
        self.cashDeskList = []
        self.outgoingVisitorList = []
        self.recipeMap = {}
        self.dessertMap = {}
        self.ratingSum = 0
        self.ratingAmount = 0
        self.menuList = {}
        self.ingredientMap = {}

    def run(self):
        self.createMenu()

        while self.currentTime < self.request.CLOSING_TIME:
            for visitor in self.outgoingVisitorList:
                visitor.getCashDesk().removeVisitor(visitor)
            self.outgoingVisitorList.clear()

            assert self.visitorGenerator
            self.visitorGenerator.process(self.currentTime)

            for cash_desk in self.cashDeskList:
                cash_desk.getWorker().prosecc(self.currentTime)
                for visitor in cash_desk.getVisitorList():
                    visitor.process(self.currentTime)

    def requestProduct(self, product: Product):
        if product.isNeedPrepare():
            if self.recipeMap[product]:
                return VisitorRequestStatus.NEED_PREPARE

        else:
            if self.dessertMap.get(product, default = 0) > 0:
                return VisitorRequestStatus.SUCCESS

        return VisitorRequestStatus.PRODUCT_MISSING

    def setVisitorGenerator(self, visitorGenerator: VisitorGenerator):
        self.visitorGenerator = visitorGenerator

    def addRating(self, rating: int):
        self.ratingSum += rating
        self.ratingAmount += 1

    def getAvgRating(self):
        return float(self.ratingSum) / float(self.ratingAmount)

    def visitorLeave(self, visitor: Visitor):
        self.outgoingVisitorList.append(visitor)

    def createMenu(self):
        for key, value in self.dessertMap.items():
            self.menuList += key
        for key, value in self.recipeMap.items():
            self.menuList += key

    def getMenu(self):
        return self.menuList

    def addDessert(self, dessert: Product, amount: int):
        self.dessertMap[dessert] = amount

    def takeProduct(self, product: Product):
        if not product.isNeedPrepare:
            currentAmount = self.dessertMap.get(product, default=0)
            if currentAmount > 0:
                self.dessertMap[product] -= 1

    def addRecipe(self, product: Product, recipe: Recipe):
        self.recipeMap[product] = recipe

    def getRecipe(self, product: Product):
        return self.recipeMap.get(product, default=0)

    def addIngredient(self, ingredient: Ingredient, amount: int):
        self.ingredientMap[ingredient] = amount

    def takeIngredient(self, ingredient: Ingredient, amount: int):
        currentAmount = self.ingredientMap.get(ingredient, default=0)
        if currentAmount - amount >= 0:
            self.ingredientMap[ingredient] -= amount
            return True
        return False

    def addCashDesk(self, cashDesk: CashDesk):
        self.cashDeskList.append(cashDesk)

    def getCashDeskList(self):
        return self.cashDeskList
