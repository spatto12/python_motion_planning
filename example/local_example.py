'''
@file: local_example.py
@breif: local planner application examples
@author: Winter
@update: 2023.10.24
'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))
from utils import Grid, Map, ControlFactory

if __name__ == '__main__':
    '''
    local planner constructor
    '''
    control_factory = ControlFactory()
    
    # build environment
    start = (5, 5, 0)
    goal = (45, 25, 0)
    env = Grid(120, 54)

    # creat planner
    planner = control_factory("apf", start=start, goal=goal, env=env)

    # animation
    planner.run()
