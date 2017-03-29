'''
Created on Mar 16, 2017

@author: Utilizator
'''
from domain.Graph import Graph
class Iterator:
    '''
    classdocs
    '''

    
    def __init__(self, vertices,first,last):
        
        if vertices == None:
            self.__vertices=[]
        else:
            self.__vertices=vertices
        self.__first=first
        self.__last=last
        self.__current=self.__vertices[first]
    def __len__(self):
        return len(self.vertices)
    
    def __getitem__(self, key):
        return self.vertices[key]
    
    def __setitem__(self, key, value):
        self.vertices[key] = value
    
    def __delitem__(self, key):
        del(self.vertices[key])
        
    def __iter__(self):
        return self
      
    def __next__(self):
        if self.__first> self.__last:
            raise StopIteration
        else:
            self.__first+=1
            self.__current=self.__vertices[self.__first - 1]
            return self.__vertices[self.__first-1]
    
g=Graph("C:\\Users\\Utilizator\\Desktop\\University\\Semester 2\\Graph Algorithms\\Lab1\\graph")
v=g.getVertices()
for e in Iterator(v,0,len(v)-1):
    print(e)   