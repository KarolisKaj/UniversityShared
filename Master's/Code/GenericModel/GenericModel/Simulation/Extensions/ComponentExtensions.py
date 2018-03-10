import simpy
import re

from Simulation.Constants.Constants import *
from Simulation.Components.Component import Component
from Simulation.Extensions.RandomValueGenEx import *

def create_components(edges, env, stores, attributes):
    components = dict()
    for edge in edges:
        add_new_key(edge[startNode], components, env, attributes)
        add_new_key(edge[endNode], components, env, attributes)
        add_actions(components, edge, stores, env)
    
    clone_components(components)
    return components

def add_new_key(name, components, env, attributes):
    if(not name in components):
        components[name] = Component(name, attributes[name])
        components[name].set_timeout_action(create_timeout_action(env, attributes[name]))


def clone_components(components):
    for component in components:
        components[component] = clone_component(components[component])

def clone_component(component):
    components = [component]
    attributes = component.get_attrbutes()
    for index in range((int(attributes[clone_attribute]) - 1) if clone_attribute in attributes else 0):
        components.append(component.clone())
    
    return components

def create_timeout_action(env, attributes):
    return lambda: generate_gauss_timeout(env, int(attributes[time_out]) if time_out in attributes else default_timeout)  

def add_actions(components, edge, stores, env):
    if (not edge[startNode] + ' To ' + edge[endNode] in stores):
        store = simpy.Store(env)
        components[edge[startNode]].add_action(lambda: store.put(edge[startNode] + " produced message."))
        components[edge[endNode]].add_action(lambda: store.get())
        stores[edge[startNode] + ' To ' + edge[endNode]] = store

def get_attributes(edges):
    attributes = dict()
    for edge in edges:
         attributes[edge[startNode]] = extract_component_attributes(edge[startNode])
         attributes[edge[endNode]] = extract_component_attributes(edge[endNode])

    return attributes

def extract_component_attributes(name):
    matches = re.findall("(!([a-z]+)(\d+[\,\.]?\d*))", name)
    attributes = dict()
    for match in matches:
        attributes[match[1]] = match[2]

    return attributes
