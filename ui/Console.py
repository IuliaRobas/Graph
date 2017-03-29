'''
Created on Mar 14, 2017

@author: Utilizator
'''


class Console(object):
    '''
    classdocs
    '''


    def __init__(self,controller):
        '''
        Constructor
        '''
        self.__ctrl=controller
        
    def __printMenu(self):
        print("*********************************************************************")
        print("1. Get the number of vertices")
        print("2. Find if there is and edge from a vertex from another")
        print("3. Get the in degree or the out degree of a specified vertex")
        print("4. Iterate through the set of inbound or outbound edges of a vertex")
        print("5. Retrieve or modify the information attached to a specified edge")
        print("0. Exit")
        print("*********************************************************************")
        print("\n")
        
    def __readCommand(self):
        option = input("Your option is: ")   
        try:
            int(option)
        except ValueError:
            raise Exception()
        return int(option)
    
    def __isEdge(self):
        origin=input("Please input the origin vertex: ")
        try:
            origin=int(origin)
        except ValueError:
            raise Exception("Invalid input! Vertex must be an integer!")
        target=int(input("Please input the target vertex: "))
        try:
            target=int(target)
        except ValueError:
            raise Exception("Invalid input! Vertex must be an integer!")
        exists=self.__ctrl.isEdge(origin,target)
        if exists is not False:
            print("There is an edge from",origin,"to",target,".")
        else:
            print("There isn't any edge from",origin,"to",target,".")
    def __getNumberOfVertices(self):
        print(self.__ctrl.getNumberOfVertices())
        
    def __getInOutDegree(self):
        option=input("Please input your option (in/out): ")
        if option not in ["in","out"]:
            raise Exception ("Invalid option! Please try again!")
        vertex=input("Please input the vertex number: ")
        try:
            vertex=int(vertex)
        except ValueError:
            raise Exception("Invalid input! Vertex must be an integer!")
        if option=="in":
            inDegree=self.__ctrl.getInDegree(vertex)
            print("The in degree of {0} is {1}.".format(vertex,inDegree))
            return
        elif option=="out":
            outDegree=self.__ctrl.getOutDegree(vertex)
            print("The out degree of {0} is {1}.".format(vertex,outDegree))
            return
       
    
    def __iterateEdges(self):
        option=input("Please input your option (in/out): ")
        if option not in ["in","out"]:
            raise Exception ("Invalid option! Please try again!")
        vertex=input("Please input the vertex number: ")
        try:
            vertex=int(vertex)
        except ValueError:
            raise Exception("Invalid input! Vertex must be an integer!")
        if option=="in":
            inEdges=self.__ctrl.getInEdges(vertex)
            if (len(inEdges)==0):
                print("There isn't any edge with target vertex {0}.".format(vertex))
            else:
                print("The origin vertex/vertices are: ",end="")
                for v in inEdges:
                    print(v,end=" ")
            return
        elif option=="out":
            outEdges=self.__ctrl.getOutEdges(vertex)
            if (len(outEdges)==0):
                print("There isn't any edge with origin vertex {0}.".format(vertex))
            else:
                print("The target vertex/vertices are: ",end="")
                for v in outEdges:
                    print(v,end=" ")
            return
    def __retrieveModifyCost(self):
        option=input("Please type in your option(retrieve/modify): ")
        if option not in ["modify","retrieve"]:
            raise Exception("Invalid input! Please type in again!")
        origin=input("Please type in the origin vertex: ")
        try:
            origin=int(origin)
        except ValueError:
            raise Exception("Invalid input! Please type in an integer!")
        target=input("Please type in the target vertex: ")
        try:
            target=int(target)
        except ValueError:
            raise Exception("Invalid input! Please type in an integer!")
        
        if option=="modify":
            newCost=input("Please type in the new cost for the specified edge: ")
            try:
                newCost=int(newCost)
            except ValueError:
                raise Exception("Invalid input! Please type in an integer!")
            self.__ctrl.modifyCost(origin,target,newCost)
        elif option=="retrieve":
            cost=self.__ctrl.getCost(origin,target)
            print("The cost of edge {0} {1} is {2}.".format(origin,target,cost))
      
      
        
    def runApp(self):
        commands = {1: self.__getNumberOfVertices,2:self.__isEdge,3:self.__getInOutDegree,4:self.__iterateEdges,
                    5:self.__retrieveModifyCost}
        while True:
            self.__printMenu()
            cmd = self.__readCommand()
            if cmd == 0:
                print("Thank you! Bye!")
                return
            try:
                commands[cmd]()
            except KeyError:
                print("Invalid input! Type in again!")           
            except Exception as ex:
                print(ex)
            print("\n")