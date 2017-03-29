'''
Created on Mar 16, 2017

@author: Utilizator
'''
import unittest
from domain.Graph import Graph


class Test(unittest.TestCase):


    def setUp(self):
        self.__graph=Graph("C:\\Users\\Utilizator\\Desktop\\University\\Semester 2\\Graph Algorithms\\Lab1\\graph")


    def tearDown(self):
        del self.__graph


    def testName(self):
        inV=self.__graph.getInVerteces(3)
        assert(len(inV)==2)
        inD=self.__graph.getInDegree(3)
        assert(inD==2)
        outV=self.__graph.getOutVerteces(0)
        assert(len(outV)==2)
        #for i in range(len(outV)):
        #    print(outV[i])
        inV=self.__graph.getInVerteces(1)
#         for i in range(len(inV)):
#             print(inV[i])
        e=self.__graph.getEdges()
        self.__graph.modifyCost(1, 2, 100)
#         for i in e:
#             print(i)
        assert(self.__graph.isEdge(3, 4)==False)
        assert(self.__graph.isEdge(1,2)==True)
        print(len(self.__graph.getInVerteces((4))))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()