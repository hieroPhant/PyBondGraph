# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 02:25:04 2014
+------------------------------------------------------+
|(c) 2014 The University of Texas at Austin            |
|         Mechanical Enigneering Department            |
|         NERDLab - Neuro-Engineering, Research &      |
|                   Development Laboratory             |
|         @author: benito                              |
+------------------------------------------------------+
"""

""" A Python Class Enum Constants
A simple Python BondGraph class, demonstrating the essential 
facts and functionalities of BondGraph.

"""
from Extras.enum import Enum

class BondType(Enum):
    Signal = (0, 'SignalBond')
    Power  = (1, 'PowerBond')

class CausalityType(Enum):
    Tail    = (-1, 'Tail')
    Acausal = ( 0, 'Acausal') # Undefined
    Head    = ( 1, 'Head')

class ArrowType(Enum):
    Tail      = (-1, 'Tail')
    Undefined = ( 0, 'Undefined')
    Head      = ( 1, 'Head')
    
class ElementType(Enum):
    Junction     = (0,'Junction')
    Source       = (1,'Source')
    Storage      = (2,'Storage')
    Transduction = (2,'Transduction')
    Dissipation  = (5,'Dissipation')
    Undefined    = (-1,'Undefined')

class JunctionType(Enum):
    Zero = 0 + 2*ElementType.Junction[0]
    One  = 1 + 2*ElementType.Junction[0]
    
class SourceType(Enum):
    Flow   = 0 + 2*ElementType.Source[0]
    Effort = 1 + 2*ElementType.Source[0]
    
class StorageType(Enum):
    Capacitor = 0 + 2*ElementType.Storage[0]
    Inertia   = 1 + 2*ElementType.Storage[0]

class TransducerType(Enum):
    Transformer = 0 + 2*ElementType.Transduction[0]
    Gyrator     = 1 + 2*ElementType.Transduction[0]
    
class DissipationType(Enum):
    Resistance = 0 + 2*ElementType.Dissipation[0]
    Admittance = 1 + 2*ElementType.Dissipation[0]
    
BGelementSymbols = [(JunctionType.Zero,          '0', 'ZeroJunction'), \
                    (JunctionType.One,           '1', 'OneJunction'), \
                    (SourceType.Flow,            'F', 'FlowSource'), \
                    (SourceType.Effort,          'E', 'EffortSource'), \
                    (StorageType.Capacitor,      'C', 'Capacitor'), \
                    (StorageType.Inertia,        'I', 'inertia'), \
                    (TransducerType.Transformer, 'T', 'Transformer'), \
                    (TransducerType.Gyrator,     'G', 'Gyrator'), \
                    (DissipationType.Resistance, 'R', 'Resistance'), \
                    (DissipationType.Admittance, 'Y', 'Admittance')]

#<<<----------------------------------------------------->>>#
