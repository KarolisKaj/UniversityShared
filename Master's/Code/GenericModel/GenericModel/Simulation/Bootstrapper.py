from Simulation.DisplayComponents.DataGrid import DataGrid

class BootStrapper(object):
    def __init__(self):
        print("-----Initiliazing Bootstrapper-----")
        dataGrid = DataGrid(self.run_sim_handle)
        dataGrid.create_grid(100, ['Unprocessed messages', 'Total messages'])

    def run_sim_handle(self):
        pass



        