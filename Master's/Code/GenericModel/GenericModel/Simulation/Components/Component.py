class Component(object):
    def __init__(self, name):
        self.name = name;
        print(type(self).__name__)

    def Run(self):
        pass

    def getName(self):
        return self.name
