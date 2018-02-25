import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid
from Simulation.Components.Component import Component

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        self.vertices = vertices;
        self.edges = edges;
        self.subgraphs = subgraphs;

        self.dataGrid = DataGrid(self.run_sim_handle)
        self.dataGrid.create_grid(100, ['Unprocessed messages', 'Total messages'])

    def run_sim_handle(self):
        components = self.initialize_components(self.edges)
        components = self.add_component_actions(components, self.edges)
        self.env = simpy.Environment()
        self.store = simpy.Store(self.env)

        #TODO: Start monitoring;
        #TODO: Add parsing;
        #TODO: Add 
        pass

    def initialize_components(self, edges):
        components = []
        for edge in edges:
            if(not self.key_exists(edge["start"], components)):
                components.append(Component(edge["start"]))
            if(not self.key_exists(edge["end"], components)):
                components.append(Component(edge["end"]))
        return components

    def key_exists(self, name, components):
        for component in components:
            if(name == component.get_name()):
                return True
        return False

    def add_component_actions(self, components, edges):
        pass