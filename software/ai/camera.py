
class Camera:
    x_flip  = 1 # 1 is not flip -1 is flip 
    y_flip  = 1
    x_dist_per_pix_per_meter: float = 0.0003792011843564136 * x_flip
    y_dist_per_pix_per_meter: float = 0.0005137066016141622 * y_flip
    fov_x: float = 27.4   # degrees
    fov_y: float = 21.0   # degrees
    width: int = 1280
    height: int = 720