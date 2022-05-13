import RecipeStep


class Recipe:
    def __init__(self):
        self.stepList = []

    def addStep(self, step: RecipeStep):
        self.stepList.append(step)

    def getStepList(self):
        return self.stepList
