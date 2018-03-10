import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid
from Simulation.Monitoring.Monitoring import Monitoring
from Simulation.Monitoring.MonitoringRule import MonitoringRule
from Simulation.Extensions.ComponentExtensions import *
from Simulation.Constants.Constants import default_monitoring_interval, simulation_duration
from Simulation.Data.DataStore import *

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        global stored_vertices 
        stored_vertices = vertices
        global stored_edges 
        stored_edges = edges
        global stored_subgraphs 
        stored_subgraphs = subgraphs
        
        global stored_attributes
        stored_attributes = get_attributes(stored_edges)

        stored_stores = dict()
        
        self.dataGrid = None

    def run_sim_handle(self):
        self.env = simpy.Environment()

        global stored_components
        stored_components = create_components(stored_edges, self.env, stored_stores, stored_attributes)
        for index in stored_components:
            [self.env.process(component.run()) for component in stored_components[index]]

        monitor = Monitoring([self.create_monitor_rule(store) for store in stored_stores])
        self.env.process(monitor.start_monitoring(lambda: self.env.timeout(default_monitoring_interval)))

        #TODO: Display adjustments;
            #TODO: Events on invoked

        self.env.run(until=simulation_duration)
        self.create_dataGrid(monitor.get_results())

        for component in stored_components:
            print(stored_attributes[component])
            print(stored_components[component])
            self.dataGrid.add_changeable_slider(component, (lambda x: self.assign(stored_attributes[name], "cl", int(x))))

        self.dataGrid.show_grid()
        print("Finished simulation. Waiting for events...")

    def assign(self, dic, name, value):
        dic[name] = value

    def create_dataGrid(self, data):
        if(self.dataGrid is None):
            self.dataGrid = DataGrid()
            self.dataGrid.create_grid(data)
        else: 
            self.dataGrid.update_data(monitor.get_results())

    def create_monitor_rule(self, name):
        return MonitoringRule(name, lambda: len(stored_stores[name].items))
