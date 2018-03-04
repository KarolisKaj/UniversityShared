from Simulation.Components.AttributeRules import attribute_actions

class Component(object):
    def __init__(self, name, attributes):
        self.name = name
        print("Initializing component named - " + self.name)
        self.actions = []
        self.model_component(attributes)
        self.timeout_action = None


    def run(self):
        while True:
            for action in self.actions: 
                action()
                print("action exists")
            yield self.timeout_action()

    def add_action(self, action):
        self.actions.append(action)
    
    def set_timeout_action(self, action):
        print("added time out")
        self.timeout_action = action

    def get_name(self):
        return self.name

    def model_component(self, attributes):
        for attribute in attributes:
            print(attribute)

