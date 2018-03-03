class Component(object):
    def __init__(self, name, attributes):
        self.name = name
        print("Initializing component named - " + self.name)
        self.actions = []
        self.model_component(attributes)

    def run(self):
        while True:
             if len(self.actions) == 0: break
             for action in self.actions: 
                 yield action()

    def add_action(self, action):
        self.actions.append(action)

    def get_name(self):
        return self.name

    def model_component(self, attributes):
        pass
