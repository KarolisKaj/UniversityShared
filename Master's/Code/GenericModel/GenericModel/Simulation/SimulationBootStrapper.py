import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid
from Simulation.Monitoring.Monitoring import Monitoring
from Simulation.Monitoring.MonitoringRule import MonitoringRule
from Simulation.Extensions.ComponentExtensions import *
from Simulation.Constants.Constants import default_monitoring_interval, simulation_duration

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        self.vertices = vertices
        self.edges = edges
        self.subgraphs = subgraphs

        self.stores = dict()

        self.dataGrid = None

    def run_sim_handle(self):
        self.env = simpy.Environment()

        components = create_components(self.edges, self.env, self.stores)
        for index in components:
            [self.env.process(component.run()) for component in components[index]]

        monitor = Monitoring([self.create_monitor_rule(store) for store in self.stores])
        self.env.process(monitor.start_monitoring(lambda: self.env.timeout(default_monitoring_interval)))

        #TODO: Display adjustments;
            #TODO: Events on invoked

        self.env.run(until=simulation_duration)
        self.create_dataGrid(monitor.get_results())

        print("Finished simulation. Waiting for events...")

    def create_dataGrid(self, data):
        if(self.dataGrid is None):
            self.dataGrid = DataGrid(self.run_sim_handle)
            self.dataGrid.create_grid(data)

    def create_monitor_rule(self, name):
        return MonitoringRule(name, lambda: len(self.stores[name].items))
