from Component import Component

class Monitor(Component):
    def __init__(self, name, monitoringRulesSet):
        super().__init__(name)
        self.monitoringRulesSet = monitoringRulesSet

    def monitor_step(self, interval_handle):
        for i in range(len(self.monitoringRulesSet)):
            data.append([])

        while True:
            for i in self.monitoringRulesSet:
                data[i].append(self.monitoringRulesSet[i]())

        yield interval_handle()

        return data

