import Ingredient
import KitchenMachine


class RecipeStep:
    def __init__(self, ingredient: Ingredient, amount: int, machine: KitchenMachine, time: int):
        self.ingredient = ingredient
        self.amount = amount
        self.machine = machine
        self.time = time

    def getIngredient(self):
        return self.ingredient

    def getAmount(self):
        return self.amount

    def getMachine(self):
        return self.machine

    def getTime(self):
        return self.time
