import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid

class SimulationBootStrapper(object, vertices, edges, subgraphs):
    def __init__(self):
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

    def initialize_components(self):
        #for edge in self.edges:
        #    if(edge)
        #    pass
        # TODO: Do the magic.
        pass


        