# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:01:48 2022

@author: faheem.u
"""

# import math
# class Circle():
#     is_shape = True
#     def __init__(self, radius, color='red'):
#         self.radius = radius
#         self.color = color
#     def area(self):
#         a=math.pi * self.radius ** 2
#         return a
#     def __str__(self):
#         return '%s (area: %s cm)' % ( self.area.a)

# from turtle import Turtle, done
# for i in range(100):
#     turtle = Turtle()
#     turtle.right(180)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(50)
# done()

# import turtle
# star = turtle.Turtle()
 
# # star.right(75)
# # star.forward(100)
 
# for i in range(5):
#     star.right(144)
#     star.forward(100)
     
# turtle.done()

# import turtle
# star = turtle.Turtle()
 
# star.right(75)
# star.forward(100)
 
# for i in range(100):
#     star.right(144)
#     star.forward(100)
     
# turtle.done()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()
data = np.array([
[30, 20, 10,],
[10, 40, 15],
[12, 10, 20]
])
sns.heatmap(data, annot=True )
