'''
Created on Mar 21, 2017

@author: Utilizator
'''

class GraphClass(object):
    '''
    classdocs
    '''


    def __init__(self, n):
        '''
        Constructor
        '''
        self.outEdges=[[] for x in range(n)]
        self.inEdges=[[] for x in range(n)]
        
    def getEdges(self):
        return list(self.__edges.values())
    
    def getVertices(self):
        return self.__vertices
    
    def getNumberOfVertices(self):
        vertices=self.getVertices()
        return len(vertices)
    
    def addEdge(self,edge):
        self.__edges[edge.id]=edge
        
    def addInAndOuts(self,origin,target):
        self.__outEdges[origin].append(target)
        self.__inEdges[target].append(origin)
        
    def isEdge(self,origin,target):
        return target in self.__outEdges[origin]
    
    def getOutVerteces(self, vertex):
        out=[]
        for target in self.__outEdges[vertex]:
            out.append(target)
        return out
    
    def getInVerteces(self, vertex):
        inV=[]
        for origin in self.__inEdges[vertex]:
            inV.append(origin)
        return inV
    def getInDegree(self, vertex):
        inV=self.getInVerteces(vertex)
        return len(inV)   
    def getOutDegree(self, vertex):
        outV=self.getOutVerteces(vertex)
        return len(outV)
    