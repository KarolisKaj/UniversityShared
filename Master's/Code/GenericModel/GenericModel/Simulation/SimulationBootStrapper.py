import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        self.vertices = vertices;
        self.edges = edges;
        self.subgraphs = subgraphs;

        self.dataGrid = DataGrid(self.run_sim_handle)
        self.dataGrid.create_grid(100, ['Unprocessed messages', 'Total messages'])

    def run_sim_handle(self):
        self.env = simpy.Environment()
        self.store = simpy.Store(self.env)
        #TODO: Start monitoring;
        #TODO: Add parsing;
        #TODO: Add 
        pass

    def initialize_components(self, components):
        
        #for edge in self.edges:
        #    if(edge.)
        #    pass
        # TODO: Do the magic.
        pass


        