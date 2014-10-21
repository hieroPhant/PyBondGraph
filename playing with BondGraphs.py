# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 08:39:08 2014
+------------------------------------------------------+
|(c) 2014 The University of Texas at Austin            |
|         Mechanical Enigneering Department            |
|         NERDLab - Neuro-Engineering, Research &      |
|                   Development Laboratory             |
|         @author: benito                              |
+------------------------------------------------------+
"""
try:
    import matplotlib.pyplot as plt
except:
    raise

from BondGraphs import graphClass as grph

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }
    
h = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
    }

complete_graph = { 
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
}

isolated_graph = { 
    "a" : [],
    "b" : [],
    "c" : []
}

graph0 = grph.Graph(graph)
print("graph density of complete_graph:")
print(graph0.density())
print 'Edges of graph'
print(graph0.edges())
#->|[('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('b', 'c'), ('b', 'e'), ('e', 'c'), ('e', 'b'), ('d', 'c')]

print 'Isolated nodes on graph'
print(graph0.find_isolated_vertices())
#->|

   
graph1 = grph.Graph(complete_graph)
print("graph density of complete_graph:")
print(graph1.density())

graph2 = grph.Graph(isolated_graph)
print("graph density of isolated_graph:")
print(graph2.density())

graph3 = grph.Graph(g)    
print("graph density of g:")
print(graph3.density())

print("Vertices of graph:")
print(graph3.vertices())

print("Edges of graph:")
print(graph3.edges())

print("Add vertex:")
graph3.add_vertex("z")

print("Vertices of graph:")
print(graph3.vertices())
 
print("Add an edge:")
graph3.add_edge({"a","z"})

print("Vertices of graph:")
print(graph3.vertices())

print("Edges of graph:")
print(graph3.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph3.add_edge({"x","y"})
print("Vertices of graph:")
print(graph3.vertices())
print("Edges of graph:")
print(graph3.edges())

print ' ... done!'
