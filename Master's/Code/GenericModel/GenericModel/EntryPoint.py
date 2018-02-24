import argparse
import json

def addArgs():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('vertices')
    parser.add_argument('edges')
    parser.add_argument('subGraphs')
    return parser;

def getModelGraph(parser):
    args = parser.parse_args()
    vertices = json.loads(args.vertices)
    edges = json.loads(args.edges)
    subGraphs = json.loads(args.subGraphs)
    return vertices, edges, subGraphs

from Simulation.SimulationBootStrapper import SimulationBootStrapper
argsParser = addArgs()
bootstrapper = SimulationBootStrapper(getModelGraph(argsParser))
bootstrapper.run_sim_handle()
