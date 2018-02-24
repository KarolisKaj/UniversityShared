from Component import Component

class WireComponent(Component):
    def __init__(self, name):
        super(Component, self).__init__(name)

    def run(self, timeoutAction):
        super(Component, self).run(timeoutAction)

    def add_action(self, action):
        super(Component, self).add_action(action)

    def get_name(self):
        return super(Component, self).get_name()
