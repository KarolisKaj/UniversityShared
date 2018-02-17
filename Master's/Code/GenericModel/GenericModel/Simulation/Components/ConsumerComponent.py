from Component import Component

class ConsumerComponent(Component):
    def __init__(self, name):
        print("Initializing " + name)

    def run(self):
        pass

    def stop(self):
        pass