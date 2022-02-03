# import numpy
# from stl import mesh

# # Using an existing stl file:
# your_mesh = mesh.Mesh.from_file('some_file.stl')

# # Or creating a new mesh (make sure not to overwrite the `mesh` import by
# # naming it `mesh`):
# VERTICE_COUNT = 100
# data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
# your_mesh = mesh.Mesh(data, remove_empty_areas=False)

# # The mesh normals (calculated automatically)
# your_mesh.normals
# # The mesh vectors
# your_mesh.v0, your_mesh.v1, your_mesh.v2
# # Accessing individual points (concatenation of v0, v1 and v2 in triplets)
# assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
# assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
# assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
# assert (your_mesh.points[1][0:3] == your_mesh.v0[1]).all()

# your_mesh.save('new_stl_file.stl')






##################
# from stl import mesh
# import math
# import numpy

# # Create 3 faces of a cube
# data = numpy.zeros(6, dtype=mesh.Mesh.dtype)

# # Top of the cube
# data['vectors'][0] = numpy.array([[0, 1, 1],
#                                   [1, 0, 1],
#                                   [0, 0, 1]])
# data['vectors'][1] = numpy.array([[1, 0, 1],
#                                   [0, 1, 1],
#                                   [1, 1, 1]])
# # Front face
# data['vectors'][2] = numpy.array([[1, 0, 0],
#                                   [1, 0, 1],
#                                   [1, 1, 0]])
# data['vectors'][3] = numpy.array([[1, 1, 1],
#                                   [1, 0, 1],
#                                   [1, 1, 0]])
# # Left face
# data['vectors'][4] = numpy.array([[0, 0, 0],
#                                   [1, 0, 0],
#                                   [1, 0, 1]])
# data['vectors'][5] = numpy.array([[0, 0, 0],
#                                   [0, 0, 1],
#                                   [1, 0, 1]])

# # Since the cube faces are from 0 to 1 we can move it to the middle by
# # substracting .5
# data['vectors'] -= .5

# # Generate 4 different meshes so we can rotate them later
# meshes = [mesh.Mesh(data.copy()) for _ in range(4)]

# # Rotate 90 degrees over the Y axis
# meshes[0].rotate([0.0, 0.5, 0.0], math.radians(90))

# # Translate 2 points over the X axis
# meshes[1].x += 2

# # Rotate 90 degrees over the X axis
# meshes[2].rotate([0.5, 0.0, 0.0], math.radians(90))
# # Translate 2 points over the X and Y points
# meshes[2].x += 2
# meshes[2].y += 2

# # Rotate 90 degrees over the X and Y axis
# meshes[3].rotate([0.5, 0.0, 0.0], math.radians(90))
# meshes[3].rotate([0.0, 0.5, 0.0], math.radians(90))
# # Translate 2 points over the Y axis
# meshes[3].y += 2


# # Optionally render the rotated cube faces
# from matplotlib import pyplot
# from mpl_toolkits import mplot3d

# # Create a new plot
# figure = pyplot.figure()
# axes = mplot3d.Axes3D(figure)

# # Render the cube faces
# for m in meshes:
#     axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))

# # Auto scale to the mesh size
# scale = numpy.concatenate([m.points for m in meshes]).flatten()
# axes.auto_scale_xyz(scale, scale, scale)

# # Show the plot to the screen
# pyplot.show()




#####################################
#creat simple cube using triangle vertices
import numpy as np
from stl import mesh

# Define the 8 vertices of the cube
vertices = np.array([\
    [-1, -1, -1],
    [+1, -1, -1],
    [+1, +1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
    [+1, -1, +1],
    [+1, +1, +1],
    [-1, +1, +1]])
# Define the 12 triangles composing the cube / vertices position
faces = np.array([\
    [0,3,1],
    [1,3,2],
    [0,4,7],
    [0,7,3],
    [4,5,6],
    [4,6,7],
    [5,1,2],
    [5,2,6],
    [2,3,6],
    [3,7,6],
    [0,1,5],
    [0,5,4]])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]

# Write the mesh to file "cube.stl"
cube.save('cube.stl')