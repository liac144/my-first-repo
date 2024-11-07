from numpy import linspace
import numpy as np

# Constants
initial_height = 100.0  # Initial height in meters
gravity = 9.81          # Acceleration due to gravity in m/s²
def calculate_position(initial_height, gravity, time):
    """
    Calculate the position of an object in free fall at a given time.
    
    Parameters:
    - initial_height: The height from which the object is dropped (in meters)
    - gravity: The acceleration due to gravity (in m/s²)
    - time: The time elapsed since the object was dropped (in seconds)
    """

    position = initial_height - (0.5 * gravity * (time ** 2))  # Calculate position
    # Ensure that the position does not fall below ground level
    if position < 0:
        position = 0
    
    return position
# Time intervals to check the position (in seconds)
arr = linspace(0, 5, num=5)
print(arr)
# Calculate and display the position at each time interval
for time in arr:
    position = calculate_position(initial_height, gravity, time)
    print(f"At time {time} seconds, the position of the object is {position:.2f} meters.")

#Now, we're goingt to calculate the differences in position between consective timesteps, which represent the distances fallen during each time interval
distance_fallen = np.diff(position)
average_distance_fallen = np.mean(distance_fallen)
print(f"Time to hit the ground: {time:.2f} seconds")
print(f"Average distance fallen per time step: {average_distance_fallen:.4f} meters")