from geopy.distance import distance, geodesic
from geopy.point import Point
import math

def estimate_real_coords(drone_lat, drone_lon, altitude, heading, gimbal_pitch, x_pixel, y_pixel, image_width, image_height, hfov, vfov):
    """
    Estimate the real-world coordinates of a target detected in a drone image.
    
    Parameters:
    - drone_lat, drone_lon: Drone's GPS coordinates (degrees).
    - altitude: Drone's altitude (meters).
    - heading: Drone's heading (degrees, -180-180 clockwise from North).
    - gimbal_pitch: Gimbal pitch (degrees, -90 to 0).
    - x_pixel, y_pixel: Target's pixel coordinates.
    - image_width, image_height: Image dimensions.
    - hfov, vfov: Camera's horizontal and vertical field of view (degrees).
    
    Returns:
    - (target_lat, target_lon): Estimated coordinates.
    """
    # Calculate delta angles
    delta_azimuth = ((x_pixel - image_width / 2) / (image_width / 2)) * (hfov / 2)
    delta_elevation = ((image_height / 2 - y_pixel) / (image_height / 2)) * (vfov / 2)
    
    total_pitch = gimbal_pitch + delta_elevation
    if total_pitch >= 0 or total_pitch <= -120:
        raise ValueError(f"Invalid pitch: {total_pitch}°")
    
    # Normalize heading to 0-360 and compute total azimuth
    normalized_heading = heading % 360  # Converts -180-180 to 0-360
    total_azimuth = (normalized_heading + delta_azimuth) % 360
    
    # Calculate distance to target
    total_pitch_rad = math.radians(total_pitch)
    line_of_sight = altitude / math.sin(-total_pitch_rad)
    horizontal_distance = line_of_sight * math.cos(total_pitch_rad)
    
    # Compute new coordinates
    drone_point = Point(drone_lat, drone_lon)
    target_point = distance(meters=horizontal_distance).destination(drone_point, total_azimuth)
    return (target_point.latitude, target_point.longitude)

class TargetTracker:
    def __init__(self, distance_threshold=5.0):
        self.targets = []
        self.current_id = 0
        self.distance_threshold = distance_threshold  # meters
    
    def add_target(self, lat, lon):
        new_point = (lat, lon)
        min_dist = float('inf')
        min_id = None
        
        for target_id, t_lat, t_lon in self.targets:
            dist = geodesic((t_lat, t_lon), new_point).meters
            if dist < min_dist:
                min_dist = dist
                min_id = target_id
        
        if min_dist <= self.distance_threshold:
            return min_id
        else:
            self.targets.append((self.current_id, lat, lon))
            self.current_id += 1
            return self.current_id - 1

# Example Usage
if __name__ == "__main__":
    # # Drone parameters 1 0018 34.04009351677366, -118.53560895941024
    # drone_lat, drone_lon = 34.04031455555555, -118.5352648888889
    # altitude = 80  # meters
    # heading = -135  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 2437, 1691  # Image size 1600x1200
    # hfov, vfov = 69.6, 55.2  # degrees

    # Drone parameters 2 0022 34.04037669013741, -118.53544857266266
    # drone_lat, drone_lon = 34.04031472222222, -118.5352650277778 
    # altitude = 80  # meters
    # heading = -44.8  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 675, 2445  # Image size 1600x1200
    # hfov, vfov = 69.6, 55.2  # degrees

    # ## 128 34.03940622314881, -118.53409494322955
    # drone_lat, drone_lon = 34.03930138888889, -118.5345236944444
    # altitude = 80  # meters
    # heading = 44.8  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 3657, 1653  # Image size 1600x1200
    # hfov, vfov = 69.6, 55.2  # degrees

    # ## 129 34.03925629546663, -118.53381325653338
    # drone_lat, drone_lon = 34.03930127777777, -118.5345235555556
    # altitude = 80  # meters
    # heading = 90  # degrees
    # gimbal_pitch = -59.9  # degrees
    # x_pixel, y_pixel = 2250, 993  # Image size 1600x1200
    # hfov, vfov = 69.6, 55.2  # degrees

    # ## 130 34.039245893920345, -118.53381200633686
    # drone_lat, drone_lon = 34.03930161111111, -118.5345236944444
    # altitude = 80  # meters
    # heading = 90.1  # degrees
    # gimbal_pitch = -32  # degrees
    # x_pixel, y_pixel = 2303, 2504  # Image size 1600x1200
    # hfov, vfov = 69.6, 55.2  # degrees

    ## 131 34.03911397127907, -118.53399104254375
    drone_lat, drone_lon = 34.03930163888889, -118.53452375
    altitude = 80  # meters
    heading = 135  # degrees
    gimbal_pitch = -32  # degrees
    x_pixel, y_pixel = 732, 2819  # Image size 1600x1200
    hfov, vfov = 69.6, 55.2  # degrees
    
    # Estimate target coordinates
    target_lat, target_lon = estimate_real_coords(
        drone_lat, drone_lon, altitude, heading, gimbal_pitch,
        x_pixel, y_pixel, 4000, 3000, hfov, vfov
    )
    
    # Track targets
    tracker = TargetTracker(distance_threshold=5.0)
    target_id = tracker.add_target(target_lat, target_lon)
    print(f"Target Coordinates: {target_lat}, {target_lon} | ID: {target_id}")