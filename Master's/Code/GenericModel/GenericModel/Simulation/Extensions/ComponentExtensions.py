import simpy
import re

from Simulation.Constants.Constants import *
from Simulation.Components.Component import Component
from Simulation.Extensions.RandomValueGenEx import *

def create_components(edges, env, stores):
    components = dict()
    for edge in edges:
        add_new_key(edge[startNode], components, env)
        add_new_key(edge[endNode], components, env)
        add_actions(components, edge, stores, env)
    
    clone_components(components)
    return components

def add_new_key(name, components, env):
    if(not name in components):
        attributes = extract_model_attributes(name)
        components[name] = Component(name, attributes)
        components[name].set_timeout_action(create_timeout_action(env, attributes))
      
def extract_model_attributes(name):
    matches = re.findall("(!([a-z]+)(\d+[\,\.]?\d*))", name)
    attributes = []
    for match in matches:
        attributes.append((match[1], match[2]))

    return dict(attributes)

def clone_components(components):
    for component in components:
        components[component] = clone_component(components[component])

def clone_component(component):
    components = [component]
    attributes = component.get_attrbutes()
    for index in range((int(attributes['cl']) - 1) if 'cl' in attributes else 0):
        components.append(component.clone())
    
    return components

def create_timeout_action(env, attributes):
    return lambda: generate_gauss_timeout(env, int(attributes['to']) if 'to' in attributes else default_timeout)  

def add_actions(components, edge, stores, env):
    if (not edge[startNode] + ' To ' + edge[endNode] in stores):
        store = simpy.Store(env)
        components[edge[startNode]].add_action(lambda: store.put(edge[startNode] + " produced message."))
        components[edge[endNode]].add_action(lambda: store.get())
        stores[edge[startNode] + ' To ' + edge[endNode]] = store
