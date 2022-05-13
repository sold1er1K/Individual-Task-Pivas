import RecipeStep
import Product
import Recipe
import CoffeeHouse
import CashDesk


class Worker:
    def __init__(self, model: CoffeeHouse, cashDesk: CashDesk):
        self.cashDesk = cashDesk
        self.model = model
        self.currentRecipe: Recipe = None
        self.currentProduct: Product = None
        self.recipeStepIndex = 0
        self.nextActionTime = 0

    def process(self, currentTime: int):
        if not self.currentRecipe:
            visitor = self.cashDesk.getFirstVisitor()
            if not visitor:
                return
            self.currentProduct = visitor.getDesiredProduct()
            if self.currentProduct.isNeedPrepare():
                self.currentRecipe = self.model.getRecipe(self.currentProduct)
                print('Time={} Worker({}) start prepare product {}'.format(currentTime,
                                                                           hash(self), self.currentProduct))
            else:
                visitor.askDesiredProduct(currentTime)
        if self.currentRecipe:
            self.prepareProductProcess(currentTime)

    def prepareProductProcess(self, currentTime: int):
        if self.nextActionTime == 0:
            self.recipeStepIndex = 0
            step = self.getRecipeStep(self.recipeStepIndex)
            assert step

            self.nextActionTime = currentTime
            self.processStepTime(step)

        elif self.nextActionTime <= currentTime:
            step = self.getRecipeStep(self.recipeStepIndex)
            assert step

            result = self.model.takeIngredient(step.getIngredient(), step.getAmount())

            if not result:
                self.cashDesk.getFirstVisitor().failDesiredProduct(currentTime, self.currentProduct)
                self.prepareProductFinished(currentTime)
            self.recipeStepIndex += 1
            nextStep = self.getRecipeStep(self.recipeStepIndex)
            if not nextStep:
                self.model.takeProduct(self.currentProduct)
                self.cashDesk.getFirstVisitor().givePreparedProduct(currentTime, self.currentProduct)
                self.prepareProductFinished(currentTime)
            else:
                self.processStepTime(nextStep)
                self.prepareProductProcess(currentTime)

    def prepareProductFinished(self, currentTime: int):
        print('Time={} Worker({}) finish prepare {}'.format(currentTime, hash(self), self.currentProduct))
        self.nextActionTime = 0
        self.recipeStepIndex = 0
        self.currentProduct = None
        self.currentRecipe = None

    def processStepTime(self, step: RecipeStep):
        self.nextActionTime += step.getTime()

    def getRecipeStep(self, index: int):
        assert self.currentRecipe
        stepList = self.currentRecipe.getStepList()
        if len(stepList) > self.recipeStepIndex:
            return stepList.get(self.recipeStepIndex)
