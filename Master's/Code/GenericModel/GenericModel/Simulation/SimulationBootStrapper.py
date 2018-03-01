import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid
from Simulation.Components.Component import Component

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        self.startNode = "start"
        self.endNode = "end"
        self.linkText = "text"

        self.vertices = vertices
        self.edges = edges
        self.subgraphs = subgraphs

        self.dataGrid = DataGrid(self.run_sim_handle)
        self.dataGrid.create_grid(100, ['Unprocessed messages', 'Total messages'])

    def run_sim_handle(self):
        self.env = simpy.Environment()
        self.store = simpy.Store(self.env)

        components = self.initialize_components(self.edges)
        print(components)
        for index in components:
            #components[index].run()
            self.env.process(components[index].run())

        self.env.run(until=1000)
        #TODO: Start monitoring;
        #TODO: Add parsing;
        #TODO: Add
        

    def initialize_components(self, edges):
        components = dict()
        for edge in edges:
            self.add_new_key(edge[self.startNode], components)
            self.add_new_key(edge[self.endNode], components)
            self.add_actions(components, edge)

        return components

    def add_new_key(self, name, components):
        if(not name in components):
            components[name] = Component(name);

    def add_actions(self, components, edge):
        if(edge[self.startNode] == edge[self.endNode]):
            components[edge[self.startNode]].add_action(lambda: self.yield_timeout(self.env, edge, self.linkText))
    
    def yield_timeout(self, env, edge, linkText):
        return env.timeout(int(edge[linkText]))