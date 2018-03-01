class Component(object):
    def __init__(self, name):
        self.name = name
        print("Initializing component named - " + self.name)
        self.actions = []

    def run(self):
        while True:
             if len(self.actions) == 0: break
             for action in self.actions: yield action()

    def add_action(self, action):
        self.actions.append(action)

    def get_name(self):
        return self.name
