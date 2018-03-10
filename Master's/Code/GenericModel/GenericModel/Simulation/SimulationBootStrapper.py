import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid
from Simulation.Monitoring.Monitoring import Monitoring
from Simulation.Monitoring.MonitoringRule import MonitoringRule
from Simulation.Extensions.ComponentExtensions import *

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        self.vertices = vertices
        self.edges = edges
        self.subgraphs = subgraphs

        self.stores = dict()

    def run_sim_handle(self):
        self.env = simpy.Environment()

        components = create_components(self.edges, self.env, self.stores)
        for index in components:
            [self.env.process(component.run()) for component in components[index]]

        monitor = Monitoring([self.create_monitor_rule(store) for store in self.stores])
        self.env.process(monitor.start_monitoring(lambda: self.env.timeout(5)))

        #TODO: Display adjustments;
            #TODO: Events on invoked

        self.env.run(until=1000)
        self.create_dataGrid(monitor.get_results())

    def create_dataGrid(self, data):
        self.dataGrid = DataGrid(self.run_sim_handle)
        self.dataGrid.create_grid(data)

    def create_monitor_rule(self, name):
        return MonitoringRule(name, lambda: len(self.stores[name].items))
