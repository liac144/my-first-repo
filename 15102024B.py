# Function to calculate final position, velocity, and acceleration
def calculate_motion(initial_position, initial_velocity, acceleration, time):
    # Final position (x) using the equation: x = x0 + v0 * t + 0.5 * a * t^2
    final_position = initial_position + (initial_velocity * time) + (0.5 * acceleration * (time ** 2))
    
    # Final velocity (v) using the equation: v = v0 + a * t
    final_velocity = initial_velocity + (acceleration * time)
    
    return final_position, final_velocity

# Main program
def main():
    print("Motion Analysis Program")
    
    # Get user input
    try:
        initial_position = float(input("Enter the initial position (x0) in meters: "))
        initial_velocity = float(input("Enter the initial velocity (v0) in meters/second: "))
        acceleration = float(input("Enter the acceleration (a) in meters/second^2: "))
        time = float(input("Enter the time (t) in seconds: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate final position and velocity
    final_position, final_velocity = calculate_motion(initial_position, initial_velocity, acceleration, time)

    # Display results
    print(f"\nResults:")
    print(f"Final Position (x): {final_position:.2f} meters")
    print(f"Final Velocity (v): {final_velocity:.2f} meters/second")

# Run the program
if __name__ == "__main__":
    main()
