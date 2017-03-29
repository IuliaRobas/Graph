from domain.Edge import Edge
class Graph(object):
    '''
    classdocs
    '''
    

    __n=0
    __vertices=[]
    __edges={}
    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__loadFromFile()
    def __loadFromFile(self):
        try:
            f=open(self.__fileName,"r")
            line=f.readline().split(" ")
            self.__n=int(line[0])
            self.__outEdges=[[] for x in range(self.__n)]
            m=int(line[1])
            self.__inEdges=[[] for x in range(self.__n)]
            for i in range(0,self.__n):
                self.__vertices.append(i)
            for i in range(0,m):
                line=f.readline().split(" ")
                origin=int(line[0])
                target=int(line[1])
                cost=int(line[2])
                edge=Edge(origin,target,cost)               
                self.addEdge(edge)
                self.addInAndOuts(origin,target)
                #if origin not in Graph.__vertices:
                #    Graph.__vertices.append(origin)
                #if target not in Graph.__vertices:
                #    Graph.__vertices.append(target)
            
        except IOError:
            raise Exception()
        finally:
            f.close()
    
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
    def getCost(self,origin,target):
        if not self.isEdge(origin, target):
            raise Exception("There isn't any edge from {0} to {1}!".format(origin,target))
        edges=self.getEdges()
        for edge in edges:
            if (edge.get_origin() == origin) and (edge.get_target()==target):
                return edge.get_cost()
    def modifyCost(self,origin,target,newCost):
        if not self.isEdge(origin, target):
            raise Exception("There isn't any edge from {0} to {1}!".format(origin,target))
        edges=self.getEdges()
        for edge in edges:
            if (edge.get_origin() == origin) and (edge.get_target()==target):
                edge.cost=newCost
                #edge.set_cost(newCost)
    def explicitGraph(self,n):
        '''
        constructs a graph with n vertices and without arcs
        '''
        pass
    def count_vertex(self):
        '''
        returns the number of vertices
        '''
        pass
    def insert_new_vertex(self):
        '''
        inserts a new vertex and returns its number
        '''
        pass
    def remove_vertex(self,v):
        '''
        removes the vertex given v
        '''
        pass
    def insert_new_edge(self,v1,v2):
        '''
        inserts an arc from vertex v1 towards vertext v2
        precondition: there must be no arc from v1 to v2
        '''
        pass