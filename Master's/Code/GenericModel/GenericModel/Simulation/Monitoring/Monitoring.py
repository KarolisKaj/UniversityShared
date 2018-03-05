class Monitoring(object):
    def __init__(self, monitoringRulesSet):
        self.monitoringRulesSet = monitoringRulesSet
        self.data = dict()

    def start_monitoring(self, interval_handle):
        while True:
            for rule in self.monitoringRulesSet:
                #print(rule.get_name())
                if(rule.get_name() in self.data):
                    self.data[rule.get_name()].append(rule.evaluate())
                else:
                    self.data[rule.get_name()] = []
                    self.data[rule.get_name()].append(rule.evaluate())

            yield interval_handle()

    def get_results(self):
        return self.data
