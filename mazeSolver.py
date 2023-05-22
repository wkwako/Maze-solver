import sys
#sys.path.insert(1,"C:/Users/Will/Documents/Python_things/")
import numpy as np
import matplotlib.pyplot as plt
import MazeGen
import random

#Primary assumptions:
#1. The first path a breadth-first search (bfs) finds through the maze is always the
#shortest
#2. We will never need to visit any coordinate more than once

def contains(struct, item):
    """
    Returns True if item is in struct, and False otherwise
    """
    if item in struct:
        return True
    return False

def getPath(parentDict, enter, exitt):
    """
    parentDict maps tuples to other tuples. Emulates a LinkedList so we can
    trace a path back through the maze.
    """
    coords = [exitt]
    curr = exitt
    while contains(parentDict,parentDict[curr]) is True:
        coords.append(parentDict[curr])
        curr = parentDict[curr]
    coords.append((1,enter[1])) #adds back first two coordinates to the final path
    coords.append((0,enter[1]))
    return coords

def initBFS():
    """
    Initializes 'adj', a dictionary that stores adjacent values and coordinates
    """
    dictVals = 'upVal upCoords downVal downCoords leftVal leftCoords rightVal rightCoords'
    dictVals = dictVals.split(' ')
    adj = {i:None for i in dictVals}
    return adj

def setAdjacentBFS(adj,curr,maze):
    """
    Updates 'adj'
    """
    y,x = curr
    adj['upVal'],adj['upCoords'] = maze[y-1,x],(y-1,x)
    adj['downVal'],adj['downCoords'] = maze[y+1,x],(y+1,x)
    adj['leftVal'],adj['leftCoords'] = maze[y,x-1],(y,x-1)
    adj['rightVal'],adj['rightCoords'] = maze[y,x+1],(y,x+1)
    return adj

def enqueueValidCoords(queue,adj,visitedSet,parentDict,curr):
    """
    Enqueues each adjacent coordinate that is not a wall and also
    has not already been visited.
    """
    if (adj['upVal'] == 0) and (not contains(visitedSet,adj['upCoords'])):
        queue.append(adj['upCoords'])
        parentDict[adj['upCoords']] = curr
    if (adj['rightVal'] == 0) and (not contains(visitedSet,adj['rightCoords'])):
        queue.append(adj['rightCoords'])
        parentDict[adj['rightCoords']] = curr
    if (adj['downVal'] == 0) and (not contains(visitedSet,adj['downCoords'])):
        queue.append(adj['downCoords'])
        parentDict[adj['downCoords']] = curr
    if (adj['leftVal'] == 0) and (not contains(visitedSet,adj['leftCoords'])):
        queue.append(adj['leftCoords'])
        parentDict[adj['leftCoords']] = curr
    return queue,parentDict

def BFS(maze,enter,exitt):
    """
    Given a maze, an entrance coord and an exit coord, finds and plots the shortest path
    through the maze.
    """
    visitedSet = {enter}
    enter = (1,enter[1])
    queue = [enter]
    curr = None
    parentDict = {}
    adj = initBFS()
    while curr != exitt and len(queue) > 0:
        curr = queue.pop(0)
        visitedSet.add(curr)
        if curr == exitt:
            break
        adj = setAdjacentBFS(adj,curr,maze)
        queue,parentDict = enqueueValidCoords(queue,adj,visitedSet,parentDict,curr)
    #path has been found
    coords = getPath(parentDict, enter, exitt)
    xs = [p[0] for p in coords]
    ys = [p[1] for p in coords]
    plt.imshow(maze,'gray_r')
    plt.plot(ys,xs,linewidth=4)
    plt.show()

size = 20
maze, enter, exitt = MazeGen.gen_maze2(size)
plt.figure(figsize=(8,8))
BFS(maze, enter, exitt)