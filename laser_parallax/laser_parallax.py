import numpy as np

def image_coordinate_to_projected_point(
        image_point: np.ndarray, pixel_pitch_mm: float, focal_length_mm: float):
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
        pixel_pitch_mm=camera_params[3],
        focal_length_mm=camera_params[0])
    final_laser_axis = -1 * projected_point / np.linalg.norm(projected_point)

    # point_constant = (-1 * laser_axis[2] * laser_origin[0]) / \
    #     (laser_axis[0] * final_laser_axis[2] - laser_axis[2] * final_laser_axis[0])

    # Least squares
    point_constant = ((final_laser_axis.T @ laser_origin) - ((laser_axis.T @ laser_origin) * (laser_axis.T @ final_laser_axis))) / \
                        (1 - (laser_axis.T @ final_laser_axis) ** 2)

    world_point = point_constant * final_laser_axis
    return world_point

def test_run():
    sensor_size_px = np.array([4000, 3000])
    pixel_pitch_mm = 0.0015
    focal_length_mm = 4.5
    laser_1_origin = np.array([0.05, 0, 0])
    laser_1_axis = np.array([0, 0, 1])

    plane_normal = np.array([0, 0, 1])
    plane_origin = np.array([0, 0, 5])

    laser_1_scalar = np.dot((plane_origin - laser_1_origin), plane_normal) / np.dot(laser_1_axis, plane_normal)
    laser_1_dot = laser_1_origin + laser_1_axis * laser_1_scalar
    laser_1_dot

    laser_1_projection = -focal_length_mm / 1e3 / laser_1_dot[2] * laser_1_dot[0:2] / (pixel_pitch_mm / 1e3) # in pixels
    laser_1_projection

    world_coordinate = compute_world_point(
        laser_origin=laser_1_origin,
        laser_axis=laser_1_axis,
        camera_params=(focal_length_mm, sensor_size_px[0], sensor_size_px[1], pixel_pitch_mm),
        image_coordinate=laser_1_projection
    )
    print(world_coordinate)
    assert world_coordinate == 5.

if __name__ == '__main__':
    test_run()