from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from stl import mesh

# 이미지 불러오기
im = Image.open("C:/Users/YSJ/Desktop/PythonWorkspace/3D modeling/images/sample.jpg")
im180 = im.rotate(180)
# plt.imshow(im180)
# plt.show()

# grey scale로 변환
grey_im180 = im180.convert("LA")
# plt.imshow(grey_im180)
# plt.show()
# print(grey_im180.size)




## 2개 삼각형으로 한 평면 만들기
#creat simple cube using triangle vertices
# import numpy as np
# from stl import mesh

# # Define the 8 vertices of the cube
# vertices = np.array([\
#     [-1, -1, -1],
#     [+1, -1, -1],
#     [+1, +1, -1],
#     [-1, +1, -1]])

# # Define the 12 triangles composing the cube / vertices position
# faces = np.array([\
#     [0,1,2],
#     [3,2,0]])

# # Create the mesh
# cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
# for i, f in enumerate(faces):
#     for j in range(3):
#         cube.vectors[i][j] = vertices[f[j],:]

# # Write the mesh to file "cube.stl"
# cube.save('surface.stl')







## 1000x5000개의 삼각형으로 평면 만들기
nrows = 10
ncols = 50
vertices = np.zeros((nrows, ncols, 3))

for x in range(0, ncols):
    for y in range(0, nrows):
        z = 0
        vertices[y][x] = (x,y,z)

faces = []

for x in range(0, ncols - 1):
    for y in range(0, nrows - 1):
        z = 0
        vertices1 = vertices[y][x]
        vertices2 = vertices[y+1][x]
        vertices3 = vertices[y][x+1]
        face1 = (vertices1, vertices2, vertices3)
        faces.append(face1)

        vertices4 = vertices[y+1][x+1]
        face2 = (vertices4, vertices2, vertices3)
        faces.append(face2)

facesNp = np.array(faces)

# Create the mesh
surface = mesh.Mesh(np.zeros(facesNp.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        surface.vectors[i][j] = facesNp[i][j]

surface.save('surface.stl')
