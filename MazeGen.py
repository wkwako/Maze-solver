
import numpy as np
import matplotlib.pyplot as plt
import random


def gen_maze(d, plot=False):

    size = d

    entrance = np.random.randint(1,size-1)

    d = np.ones((size,size))
    h,w = d.shape
    d[0,entrance] = 0
    d[1,entrance] = 0

    maze = [(1,entrance)]

    def get_nbrs(index):
        r, c = index
        nbrs = []
        if r-1 > 0:
            nbrs.append((r-1,c))
        if r+1 < size-1:
            nbrs.append((r+1,c))
        if c-1 > 0:
            nbrs.append((r,c-1))
        if c+1 < size-1:
            nbrs.append((r,c+1))
        return nbrs

    while len(maze):
    # for _ in range(2000):
        curr = maze[-1]
        # print(curr)
        nbrs = get_nbrs(curr)
        c = 1
        while len(nbrs)>0:
            ntry = nbrs.pop(np.random.randint(0,len(nbrs)))
            if d[ntry]:
                cnbrs = get_nbrs(ntry)
                cnbrs.remove(curr)
                if all([d[i]>0 for i in cnbrs]):
                    d[ntry] = 0
                    maze.append(ntry)
                    break
            c += 1
        if len(nbrs)==0:
            maze.pop(-1)

    finished = False
    possible_xs = [x for x in range(1,size-1)]
    random.shuffle(possible_xs)
    while not finished:
        #print (possible_xs)
        exit = possible_xs.pop()
        #exit = possible_xs[random.randint(0,len(possible_xs))-1] #new
        if d[(-2,exit)]==0:
            d[-1,exit] = 0
            finished = True
    if plot:
        plt.imshow(d, cmap='gray_r')
        plt.axis('off')
        plt.show()

    return d, (0,entrance), (h-1,exit)


def gen_maze2(size, plot=False):
    maze, enter, exit = gen_maze(size, plot=False)

    rrs = np.random.randint(1,size-1,int(size**2*0.05))
    rcs = np.random.randint(1,size-1,int(size**2*0.05))
    maze[rrs, rcs] = 0

    if plot:
        plt.imshow(maze, cmap='gray_r')
        plt.axis('off')
        plt.show()

    return maze, enter, exit

if __name__ == '__main__':
    gen_maze2(50, plot=True)

