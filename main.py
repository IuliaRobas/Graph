'''
Created on Mar 14, 2017

@author: Utilizator
'''
from ui.Console import Console
from controller.Controller import Controller
from domain.Graph import Graph

graph=Graph("C:\\Users\\Utilizator\\Desktop\\University\\Semester 2\\Graph Algorithms\\Lab1\\graph")
ui=Console(Controller(graph))
ui.runApp();

