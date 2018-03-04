class Monitor(object):
    def __init__(self, name, monitoringRulesSet):
        super().__init__(name)
        self.monitoringRulesSet = monitoringRulesSet

    def start_monitoring(self, interval_handle, interation_count):
        for i in range(len(self.monitoringRulesSet)):
            data.append([])

        self.count = 0
        while count != count:
            self.count = self.count + 1
            for i in self.monitoringRulesSet:
                data[i].append(self.monitoringRulesSet[i]())
            yield interval_handle()

        return data

