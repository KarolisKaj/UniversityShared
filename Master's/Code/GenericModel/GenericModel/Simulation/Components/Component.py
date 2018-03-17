from Simulation.Components.AttributeRules import attribute_actions
from Simulation.Components.ComponentState import *
from Simulation.Constants.Constants import *

class Component(object):
    def __init__(self, name, attributes):
        self.name = name
        print("Initializing component named - " + self.name)
        self.actions = []
        self.attributes = attributes
        self.timeout_action = None

        self.component_state = ComponentState.Undefined
        self.recovery_rate_handle = None
        self.death_rate_handle = None

        self.model_component(self.attributes)

    def run(self):
        while True:
            self.component_state = self.new_state()
            if(self.component_state != ComponentState.Dead):
                for action in self.actions: 
                    yield action()
            yield self.timeout_action()

    def add_action(self, action):
        self.actions.append(action)
    
    def set_timeout_action(self, action):
        self.timeout_action = action

    def get_name(self):
        return self.name

    def get_attrbutes(self):
        return self.attributes

    def model_component(self, attributes):
        if(recovery_rate in attributes):
            self.recovery_rate_handle = lambda : attribute_actions[recovery_rate](float(attributes[recovery_rate]))
        
        if(death_rate in attributes):
            self.death_rate_handle = lambda : attribute_actions[death_rate](float(attributes[death_rate]))

    def clone(self):
        component = Component(self.get_name(), self.attributes)
        component.set_timeout_action(self.timeout_action)
        for action in self.actions:
            component.add_action(action)
         
        return component

    def new_state(self):
        if(self.recovery_rate_handle is None and self.death_rate_handle is None): return ComponentState.Alive
        if(self.component_state == ComponentState.Dead):
            if(self.recovery_rate_handle is None): return ComponentState.Dead
            return ComponentState.Alive if self.recovery_rate_handle() else ComponentState.Dead;
        else:
            if(self.death_rate_handle is None): return ComponentState.Alive;
            return ComponentState.Dead if self.death_rate_handle() else ComponentState.Alive;
