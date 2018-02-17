class Component(object):
    def __init__(self, name):
        self.name = name;
        print("Initializing " + self.name)

    def run(self):
        pass

    def stop(self):
        pass

    def get_name(self):
        return self.name
