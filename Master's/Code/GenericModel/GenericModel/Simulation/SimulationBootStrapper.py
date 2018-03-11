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

        self.dataGrid = None

    def run_sim(self):
        global stored_stores
        stored_stores = dict()
        self.env = simpy.Environment()

        global stored_components
        stored_components = create_components(stored_edges, self.env, stored_stores, stored_attributes)
        for index in stored_components:
            [self.env.process(component.run()) for component in stored_components[index]]

        monitor = Monitoring([self.create_monitor_rule(store) for store in stored_stores])
        self.env.process(monitor.start_monitoring(lambda: self.env.timeout(default_monitoring_interval)))

        self.env.run(until=simulation_duration)
        self.create_dataGrid(monitor.get_results())

        print("Finished simulation...")

    def create_dataGrid(self, data):
        if(self.dataGrid is None):
            self.dataGrid = DataGrid()
            self.dataGrid.create_grid(data)
            self.create_dataGrid_dynamic_sliders()
            self.dataGrid.show_grid()
        else: 
            self.dataGrid.update_data(data)

    def create_dataGrid_dynamic_sliders(self):
        for component in stored_attributes:
            for attribute in stored_attributes[component]:
                self.create_slider(component, attribute)
                
    def create_slider(self, component, attribute):
        if(attribute == clone_attribute):
            self.dataGrid.add_changeable_slider(component + clone_attribute, lambda x: self.update_handle(component, clone_attribute, int(x)), int(stored_attributes[component][clone_attribute]))
            
    def update_handle(self, component, name, value):
        global stored_attributes
        stored_attributes[component][name] = value
        self.run_sim()

    def create_monitor_rule(self, name):
        return MonitoringRule(name, lambda: len(stored_stores[name].items))
