class Product:
    def __init__(self, name: str, isNeedPrepare: bool):
        self.name = name
        self.isNeedPrepare = isNeedPrepare

    def getName(self):
        return self.name

    def toString(self):
        info = 'Product({}) name={}'.format(hash(self), self.name)
        return info
