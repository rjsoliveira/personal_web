import os
import numpy as np
import pyvista as pv
from stpyvista import stpyvista

def get_art(fea_xyz_data):
    fea_art_data = []
    for point_i in range(len(fea_xyz_data)):
        x = fea_xyz_data[point_i][0]
        y = fea_xyz_data[point_i][1]
        z = fea_xyz_data[point_i][2]

        a = z
        r = np.sqrt(x ** 2 + y ** 2)
        t = np.arctan2(y, x)

        fea_art_data.append([a, r, t])

    return np.array(fea_art_data)


def get_xyz(fea_art_data):
    fea_xyz_data = []
    for point_i in range(len(fea_art_data)):
        a = fea_art_data[point_i][0]
        r = fea_art_data[point_i][1]
        t = fea_art_data[point_i][2]

        x = r * np.cos(t)
        y = r * np.sin(t)
        z = a

        fea_xyz_data.append([x, y, z])

    return np.array(fea_xyz_data)


data_directory = r'sections\projects\mode_shapes\data'

mode_shape_file_name = 'ModeShape_N55_Mode_2_ND_8_SuctionSide.csv'

f = open(os.path.join(os.getcwd(), os.path.normpath(data_directory), os.path.normpath(mode_shape_file_name)), 'r')
mode_shape_lines = f.readlines()
f.close()

n_lines = len(mode_shape_lines)

mode_shape_coordinates = np.empty((n_lines - 1, 3))
mode_shape_real = np.empty((n_lines - 1, 3))
mode_shape_imag = np.empty((n_lines - 1, 3))

for line_i in range(1, n_lines):
    mode_shape_lines[1].split(';')
    mode_shape_coordinates[line_i - 1] = [float(val) for val in mode_shape_lines[line_i].split(';')[1:4]]
    mode_shape_real[line_i - 1] = [float(val) for val in mode_shape_lines[line_i].split(';')[8:11]]
    mode_shape_imag[line_i - 1] = [float(val) for val in mode_shape_lines[line_i].split(';')[11:14]]

point_cloud = pv.PolyData(mode_shape_coordinates)
point_cloud['fi'] = mode_shape_real

#BLADES
N = 16
sector_angle = 2 * np.pi / N
harmonic_index = 8

mode_shape_coordinates_art = get_art(mode_shape_coordinates)

pl = pv.Plotter()
#pl.add_mesh(point_cloud.copy(), scalars='fi')
for blade_id in np.linspace(1, 16, 16):

    # ----- ROTATION
    rotation_angle_rads = (blade_id - 1) * sector_angle

    # ----- ROTATE ART DEFORMATION
    mode_shape_coordinates_art_rot = np.ones(mode_shape_coordinates_art.shape)
    for point_id in range(len(mode_shape_coordinates_art)):
        mode_shape_coordinates_art_rot[point_id][0] = mode_shape_coordinates_art[point_id][0]
        mode_shape_coordinates_art_rot[point_id][1] = mode_shape_coordinates_art[point_id][1]
        mode_shape_coordinates_art_rot[point_id][2] = mode_shape_coordinates_art[point_id][2] + rotation_angle_rads

    mode_shape_coordinates_xyz_rot = get_xyz(mode_shape_coordinates_art_rot)

    point_cloud_rot = pv.PolyData(mode_shape_coordinates_xyz_rot)
    mode_shape = mode_shape_real * np.cos((blade_id - 1) * harmonic_index * sector_angle) - mode_shape_imag * np.sin((blade_id - 1) * harmonic_index * sector_angle)
    point_cloud_rot['fi'] = mode_shape

    pl.add_mesh(point_cloud_rot.copy(), scalars='fi')

# pl.show()


stpyvista(pl, key="pv_cube")