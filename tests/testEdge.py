'''
Created on Mar 26, 2017

@author: Utilizator
'''
import unittest
from domain.Edge import Edge

class Test(unittest.TestCase):


    def setUp(self):
        self.__edge=Edge(1,2,8)


    def tearDown(self):
        del self.__edge

    def testName(self):
        assert(self.__edge.cost==8)
        assert(self.__edge.origin==1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()