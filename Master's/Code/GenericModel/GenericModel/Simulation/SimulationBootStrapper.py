import simpy

from Simulation.DisplayComponents.DataGrid import DataGrid

class SimulationBootStrapper(object):
    def __init__(self):
        print("-----Initiliazing Bootstrapper-----")
        
        dataGrid = DataGrid(self.run_sim_handle)
        dataGrid.create_grid(100, ['Unprocessed messages', 'Total messages'])

    def run_sim_handle(self):
        self.env = simpy.Environment()
        self.store = simpy.Store(self.env)
        #TODO: Start monitoring;
        #TODO: Add parsing;
        #TODO: Add 
        pass



        