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
    
    Returns:
    - position: The height of the object above the ground at the given time (in meters)
    """
    # Using the equation of motion for an object in free fall:
    # position = initial_height - (1/2 * gravity * time²)
    # where:
    # - initial_height is the starting height above the ground
    # - gravity is the acceleration due to gravity
    # - time is the elapsed time since the object was dropped
    
    position = initial_height - (0.5 * gravity * (time ** 2))  # Calculate position
    
    # Ensure that the position does not fall below ground level
    if position < 0:
        position = 0
    
    return position

# Time intervals to check the position (in seconds)
time_intervals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Time intervals in seconds

# Calculate and display the position at each time interval
for time in time_intervals:
    position = calculate_position(initial_height, gravity, time)
    print(f"At time {time} seconds, the position of the object is {position:.2f} meters.")
