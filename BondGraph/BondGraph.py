# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 08:42:25 2014
+------------------------------------------------------+
|(c) 2014 The University of Texas at Austin            |
|         Mechanical Enigneering Department            |
|         NERDLab - Neuro-Engineering, Research &      |
|                   Development Laboratory             |
|         @author: benito                              |
+------------------------------------------------------+
"""

""" A Python Class
A simple Python BondGraph class, demonstrating the essential 
facts and functionalities of BondGraph.

"""
from Extras.enum import Enum
import itertools
from graphClass import Graph
from BGconstants import *

#<<<----------------------------------------------------->>>#
        
class BGcomponent( object ):
    id_generator = itertools.count(0) # first generated is 0
    __ID = 0
    def __init__(self, Name = None, Type = None, Position = []):
        """ initializes a BGcomponent object """
        self.id = next(self.id_generator)
        self.__id = BGcomponent.__ID
        BGcomponent.__ID += 1
        self.__id += 1
        self.__name = Name
        self.__type = Type
        self.__value = 0
        self.__effort = 0
        self.__flow = 0
        self.__energyDomain = None
        self.__parameter = 0
        self.__input = 0
        self.__output = 0
        self.__position = Position
    def __str__(self):
        display =  'BGcomponent::_____:___________________\n'
        display += '            :   id: %d\n' % self.__id
        display += '            : Name: %s\n' % self.__name
        display += '            : Type: %s'   % self.__type
        return display
    @staticmethod
    def is_defined(self):
        # check if the sequence sequence is non-increasing:
        return not (self.__id == 0)        
        
#<<<----------------------------------------------------->>>#
        
class BGbond( BGcomponent, Graph ):
    id_generator = itertools.count(0) # first generated is 0
    __ID = 0
    def __init__(self, fromPort = 0, toPort = 0, Type = 'PowerBond'):
        """ initializes a BGcomponent object """
        BGcomponent.__init__(self)
        Graph.__init__(self)
        self.id = next(self.id_generator)
        self.__id = BGbond.__ID
        BGbond.__ID += 1
        self.__id += 1
        self.__fromPort = fromPort
        self.__toPort = toPort
        self.__causalityStroke = 1
        self.__directionArrow = 1
        self.__type = Type
    def __str__(self):
        display =  'BGbond::_____:___________________\n'
        display += '       :   id: %d\n' % self.__id
        display += '       : from: %s\n' % self.__fromPort
        display += '       :   to: %s\n' % self.__toPort
        display += '       : Type: %s'   % self.__type
        return display   
    def addBond(self, fromPort = 0, toPort = 0, Type = 'PowerBond'):
        self.add_edge(fromPort, toPort)

#<<<----------------------------------------------------->>>#
        
class BGelement( BGcomponent, Graph ):
    id_generator = itertools.count(0) # first generated is 0
    __ID = 0
    def __init__(self, Name = None, Type = None, Position = [0,0]):
        """ initializes a BGcomponent object """
        BGcomponent.__init__(self)
        Graph.__init__(self)
        self.id = next(self.id_generator)
        self.__id = BGelement.__ID
        BGelement.__ID += 1
        self.__id += 1
        self.__type = Type
        self.__name = Name
        self.__position = Position
        self.variable = None
        self.stateEquation = None
        self.outputEquation = None
        self.modulus = None
        self.common = None
    def __str__(self):
        display =  'BGelement::_____:___________________\n'
        display += '          :   id: %d\n' % self.__id
        display += '          : name: %s\n' % self.__name
        display += '          : Type: %s\n' % self.__type
        display += '          :  pos: %s\n' % self.__position
        return display        
    def addElement(self, Name = None, Type = None, Position = [0,0]):
        self.add_node(Name, position = Position)
    def setStateEquation(self, Equation = None):
        self.stateEquation = Equation
    def getStateEquation(self):
        return self.stateEquation
    def setOutputEquation(self, Equation = None):
        self.outputEquation = Equation
    def getOutputEquation(self):
        return self.outputEquation
    def setVariable(self, Variable = None):
        self.variable = Variable
    def getVariable(self):
        return self.variable

#<<<----------------------------------------------------->>>#
        
#<<<----------------------------------------------------->>>#
        
#<<<----------------------------------------------------->>>#
        
#<<<----------------------------------------------------->>>#
        

#--------------------------------------------------------
# END-OF-Graph class
#

if __name__ == "__main__":
    print 'BGcomponent::\n' \
          'Tried to execute BonGraph.py module\n' \
          '(with PyBondGraph classes definitions)'
          
    print '------------------------------------'
    print '----------BGcomponents--------------'
    print '------------------------------------'
    bgc0  = BGcomponent()
    bgc1  = BGcomponent('F','FlowSource')
    bgc2  = BGcomponent('C','Capacitor')
    bgc3  = BGcomponent('0','ZeroJunction')
    bgc4  = BGcomponent('T','Transformer')
    bgc5  = BGcomponent('R','Resistance')
    
    bgcs = [bgc0, bgc1, bgc2, bgc3, bgc4, bgc5]
    
    for bgc in bgcs:
        print '------------------------------------'
        print bgc
    
    print '------------------------------------'

    print '------------------------------------'
    print '------------BGbonds-----------------'
    print '------------------------------------'
    bgb0  = BGbond()
    bgb1  = BGbond(0,1)
    bgb2  = BGbond(1,4,'SignalBond')

    bgbs = [bgb0, bgb1, bgb2]
    
    for bgb in bgbs:
        print '------------------------------------'
        print bgb
    
    print '------------------------------------'

   
    print '------------------------------------'
    print '-----------BGelements---------------'
    print '------------------------------------'
    bge0  = BGelement()
    bge1  = BGelement('E','EffortSource',[1,3])
    bge2  = BGelement('1','OneJunction',[2,4])

    bges = [bge0, bge1, bge2]
    
    for bge in bges:
        print '------------------------------------'
        print bge
    
    print '------------------------------------'

    bge1.setVariable('x')
    bge1.setStateEquation('dx/dt = -2*cos(x)')
    bge1.setOutputEquation('y = x**2')

    print ' Element bge1 variable: %s' % bge1.getVariable()
    print ' Element bge1 state equation: %s' % bge1.getStateEquation()
    print ' Element bge1 output equation: %s' % bge1.getOutputEquation()
   
    print '------------------------------------'

    print bgc1.is_defined(bgc1)
    print bgb1.is_defined(bgb1)
    print bge1.is_defined(bge1)
    
    print '------------------------------------'

    for (key,val,name) in BGelementSymbols:
        print 'BGelementSymbols[%2s] = %s <- %s' % (key, val, name)

    print '------------------------------------'
        
    print 'BondType.Signal[%s] = %s' % (BondType.Signal[0], BondType.Signal[1])
    print 'BondType.Power[%s]  = %s' % (BondType.Power[0], BondType.Power[1])

    print '------------------------------------'


    print '\n\n ... done!'
    
#
# NEXT: draw graph
#    pos=nx.spring_layout(G) # positions for all nodes
#
#    # nodes
#    nx.draw_networkx_nodes(G,pos,node_size=700)



