class MonitoringRule(object):
    def __init__(self, name, rule):
        self.name = name
        self.rule = rule

    def evaluate(self):
        return self.rule();

    def get_name(self):
        return self.name

