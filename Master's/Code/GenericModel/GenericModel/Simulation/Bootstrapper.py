from Simulation.DisplayComponents.DataGrid import DataGrid

class BootStrapper(object):
    def __init__(self):
        print("-----Initiliazing Bootstrapper-----")
        dataGrid = DataGrid()
        dataGrid.create_grid(100,self.run_sim_handle)

    def run_sim_handle(self):
        pass



        