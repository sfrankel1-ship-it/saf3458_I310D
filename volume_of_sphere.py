import math

def calculate_volume_of_sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Compute and print volumes for radius 30 and 40
print("Volume of sphere with radius 30:", calculate_volume_of_sphere(30))
print("Volume of sphere with radius 40:", calculate_volume_of_sphere(40))