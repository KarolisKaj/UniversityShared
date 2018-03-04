from Simulation.Components.AttributeRules import attribute_actions

class Component(object):
    def __init__(self, name, attributes):
        self.name = name
        print("Initializing component named - " + self.name)
        self.actions = []
        self.attributes = attributes
        self.model_component(self.attributes)
        self.timeout_action = None


    def run(self):
        while True:
            for action in self.actions: 
                action()
            yield self.timeout_action()

    def add_action(self, action):
        self.actions.append(action)
    
    def set_timeout_action(self, action):
        self.timeout_action = action

    def get_name(self):
        return self.name

    def model_component(self, attributes):
        for attribute in attributes:
            print(attribute)

    def clone(self):
        component = Component(self.get_name(), self.attributes)
        component.set_timeout_action(self.timeout_action)
        for action in self.actions:
            component.add_action(action)
         
        return component
