import numpy as np

def image_coordinate_to_projected_point(image_point: np.ndarray, pixel_pitch_mm: float, focal_length_mm: float):
    assert isinstance(image_point, np.ndarray)
    # S += sensor_size_px / 2
    I_project = image_point * pixel_pitch_mm / 1e3
    I = np.array([I_project[0], I_project[1], -focal_length_mm / 1e3])
    return I

def compute_world_point(
        laser_origin: np.ndarray,
        laser_axis: np.ndarray,
        camera_params: tuple,
        image_coordinate: np.ndarray) -> np.ndarray:
    projected_point = image_coordinate_to_projected_point(
        image_point=image_coordinate,
        pixel_pitch_mm=camera_params[0],
        focal_length_mm=camera_params[3])
    final_laser_axis = -1 * projected_point / np.linalg.norm(projected_point)

    point_constant = (-1 * laser_axis[2] * laser_origin[0]) / (laser_axis[0] * final_laser_axis[2] - laser_axis[2] * final_laser_axis[0])

    world_point = point_constant * final_laser_axis
    return world_point
