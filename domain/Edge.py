'''
Created on Mar 2, 2017

@author: Utilizator
'''

class Edge(object):
    '''
    represents an arc of the graph
    '''

    counter=0
    def __init__(self, origin, target, cost):
        '''
        Constructor
        '''
        self.__origin=origin
        self.__target=target
        self.__cost=cost
#         self.__id=id(self)
        Edge.counter+=1
        self.__id=Edge.counter
    def __str__(self):
        return "{0} {1} {2}".format(self.__origin,self.__target,self.__cost)
    
    def get_origin(self):
        return self.__origin


    def get_target(self):
        return self.__target


    def get_cost(self):
        return self.__cost


    def get_id(self):
        return self.__id


    def set_origin(self, value):
        self.__origin = value


    def set_target(self, value):
        self.__target = value


    def set_cost(self, value):
        self.__cost = value


    def set_id(self, value):
        self.__id = value


    def del_origin(self):
        del self.__origin


    def del_target(self):
        del self.__target


    def del_cost(self):
        del self.__cost


    def del_id(self):
        del self.__id

    origin = property(get_origin, set_origin, del_origin, "origin's docstring")
    target = property(get_target, set_target, del_target, "target's docstring")
    cost = property(get_cost, set_cost, del_cost, "cost's docstring")
    id = property(get_id, set_id, del_id, "id's docstring")
    
    
        