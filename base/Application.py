from CoffeeHouse import CoffeeHouse
from VisitorGenerator import VisitorGenerator
from CashDesk import CashDesk
from Worker import Worker
from Product import Product
from Ingredient import Ingredient
from KitchenMachine import KitchenMachine
from Recipe import Recipe
from RecipeStep import RecipeStep


class Application:
    def __init__(self):
        self.app = Application()
        model = self.app.build()
        print('Start modeling')
        model.run()
        print('Finish rating: {}'.format(model.getAvgRating()))

    def build(self):
        model = CoffeeHouse()
        model.setVisitorGenerator(VisitorGenerator(model))


        cashDesk = CashDesk()
        cashDesk.setWorker(Worker(model, cashDesk))
        model.addCashDesk(cashDesk)

        cashDesk = CashDesk()
        cashDesk.setWorker(Worker(model, cashDesk))
        model.addCashDesk(cashDesk)

        model.addDessert(Product("Печенье", False), 20)
        model.addDessert(Product("Пирожное", False), 20)
        model.addDessert(Product("Торт", False), 20)

        coffeeBeans = Ingredient("Кофейные зерна")
        milk = Ingredient("Молоко")
        syrup = Ingredient("Сироп")

        model.addIngredient(coffeeBeans, 1000)
        model.addIngredient(milk, 200)
        model.addIngredient(syrup, 100)

        coffeeMachine = KitchenMachine("Кофе машина")
        cappuccinatore = KitchenMachine("Капучинатор")

        model.addRecipe(Product("Эспрессо", True),Recipe().addStep(RecipeStep(coffeeBeans, 5, coffeeMachine, 120)))
        model.addRecipe(Product("Раф кофе", True),
        Recipe().addStep(RecipeStep(syrup, 10, None, 10)).addStep(RecipeStep(coffeeBeans, 5, coffeeMachine, 120)).addStep(RecipeStep(milk, 10, cappuccinatore, 100)))
        model.addRecipe(Product("Каппучино", True),Recipe().addStep(RecipeStep(coffeeBeans, 5,
                                                                              coffeeMachine, 120)).addStep(RecipeStep(milk, 10, None, 10)).addStep(RecipeStep(milk, 10, cappuccinatore, 100)))

        return model
