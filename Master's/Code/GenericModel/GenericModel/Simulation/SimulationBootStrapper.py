import simpy
import re

from Simulation.DisplayComponents.DataGrid import DataGrid
from Simulation.Components.Component import Component
from Simulation.Monitoring.Monitoring import Monitoring
from Simulation.Monitoring.MonitoringRule import MonitoringRule
from Simulation.Extensions.RandomValueGenEx import *

default_timeout = 10

class SimulationBootStrapper(object):
    def __init__(self, vertices, edges, subgraphs):
        print("-----Initiliazing Bootstrapper-----")
        
        self.startNode = "start"
        self.endNode = "end"
        self.linkText = "text"

        self.vertices = vertices
        self.edges = edges
        self.subgraphs = subgraphs

        self.stores = dict()
        

    def run_sim_handle(self):
        self.env = simpy.Environment()

        components = self.initialize_components(self.edges)
        for index in components:
            self.env.process(components[index].run())

        monitor = Monitoring([self.create_monitor_rule(store) for store in self.stores])
        self.env.process(monitor.start_monitoring(lambda: self.env.timeout(10)))

        #TODO: Display adjustments;
            #TODO: Events on invoked

        self.env.run(until=1000)
        self.create_dataGrid(monitor.get_results())

    def create_dataGrid(self, data):
        self.dataGrid = DataGrid(self.run_sim_handle)
        self.dataGrid.create_grid(data)

    def create_monitor_rule(self, name):
        return MonitoringRule(name, lambda: len(self.stores[name].items))

    def initialize_components(self, edges):
        components = dict()
        for edge in edges:
            self.add_new_key(edge[self.startNode], components)
            self.add_new_key(edge[self.endNode], components)
            self.add_actions(components, edge)

        return components

    def add_new_key(self, name, components):
        if(not name in components):
            attributes = self.extract_model_attributes(name)
            components[name] = Component(name, attributes)
            components[name].set_timeout_action(self.create_timeout_action(self.env, attributes))
          
    def extract_model_attributes(self, name):
        matches = re.findall("(!([a-z]+)(\d+[\,\.]?\d*))", name)
        attributes = []
        for match in matches:
            attributes.append((match[1], match[2]))

        return dict(attributes)

    def create_timeout_action(self, env, attributes):
        return lambda: generate_gauss_timeout(self.env, int(attributes['to']) if 'to' in attributes else default_timeout)  

    def add_actions(self, components, edge):
        if (not edge[self.startNode] + ' To ' + edge[self.endNode] in self.stores):
            store = simpy.Store(self.env)
            components[edge[self.startNode]].add_action(lambda: store.put(edge[self.startNode] + " produced message."))
            components[edge[self.endNode]].add_action(lambda: store.get())
            self.stores[edge[self.startNode] + ' To ' + edge[self.endNode]] = store
