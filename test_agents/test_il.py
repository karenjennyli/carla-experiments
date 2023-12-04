# Import the CARLA Python API library and some utils
import sys

try:
    sys.path.append('/home/karenli/carla/PythonAPI/carla/dist/carla-0.9.14-py3.8-linux-x86_64.egg')
except IndexError:
    print('Error: CARLA PythonAPI not found.')
    pass

import carla 
import random 

import os

import scipy

import tensorflow as tf
import numpy as np

# import agent
from agents.imitation.imitation_learning import ImitationLearning

# Connect to the client and get the world object
city_name = 'Town01'
client = carla.Client('localhost', 2000)
client.load_world(city_name)
world = client.get_world()

# Get the blueprint library
bp_lib = world.get_blueprint_library() 

# Get the map spawn points
spawn_points = world.get_map().get_spawn_points()

# View all spawn points in debug mode
for i, spawn_point in enumerate(spawn_points):
    # Draw in the spectator window the spawn point index
    world.debug.draw_string(spawn_point.location, str(i), life_time=100)
    # We can also draw an arrow to see the orientation of the spawn point
    # (i.e. which way the vehicle will be facing when spawned)
    world.debug.draw_arrow(spawn_point.location, spawn_point.location + spawn_point.get_forward_vector(), life_time=100)

# Start and end spawn points for right turn
spawn_point_start = spawn_points[18]
spawn_point_end = spawn_points[148]

# Retrieve the spectator object
spectator = world.get_spectator()

# Set the spectator location
location = spawn_point_start.location
spectator.set_location(location + carla.Location(z=50))

# Get the blueprint for the vehicle you want
vehicle_bp = bp_lib.find('vehicle.lincoln.mkz_2020') 

# Try spawning the vehicle at a randomly chosen spawn point
vehicle = world.try_spawn_actor(vehicle_bp, spawn_point_start)

# create imitation learning agent
self.agent = ImitationLearning(vehicle=vehicle, city_name='Town01', avoid_stopping=False)
print('created')