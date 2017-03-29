'''
Created on Mar 14, 2017

@author: Utilizator
'''
from domain.Graph import Graph
class Controller:
    '''
    classdocs
    '''


    def __init__(self, graph):
        '''
        Constructor
        '''
        self.__graph=graph
    
    def getNumberOfVertices(self):
        return self.__graph.getNumberOfVertices()
    def isEdge(self,origin,target):        
        numberOfVertices=self.__graph.getNumberOfVertices()
        if origin>=numberOfVertices:
            raise Exception("Invalid origin vertex! There are only {0} vertices!".format(numberOfVertices))
       
        if target>=numberOfVertices:
            raise Exception("Invalid target vertex! There are only {0} vertices!".format(numberOfVertices))
        return self.__graph.isEdge(origin,target)
    def getInDegree(self,vertex):
        numberOfVertices=self.__graph.getNumberOfVertices()
        if vertex>=numberOfVertices:
            raise Exception("Invalid vertex! There are only {0} vertices!".format(numberOfVertices))
        return self.__graph.getInDegree(vertex)
    def getOutDegree(self,vertex):
        numberOfVertices=self.__graph.getNumberOfVertices()
        if vertex>=numberOfVertices:
            raise Exception("Invalid vertex! There are only {0} vertices!".format(numberOfVertices))
        return self.__graph.getOutDegree(vertex)
    def getOutEdges(self,vertex):
        numberOfVertices=self.__graph.getNumberOfVertices()
        if vertex>=numberOfVertices:
            raise Exception("Invalid vertex! There are only {0} vertices".format(numberOfVertices))
        return self.__graph.getOutVerteces(vertex)
    def getInEdges(self,vertex):
        numberOfVertices=self.__graph.getNumberOfVertices()
        if vertex>numberOfVertices:
            raise Exception("Invalid vertex! There are only {0} vertices".format(numberOfVertices))
        return self.__graph.getInVerteces(vertex)
    def getCost(self,origin,target):
        return self.__graph.getCost(origin,target)
    def modifyCost(self,origin,target,newCost):
        self.__graph.modifyCost(origin,target,newCost)