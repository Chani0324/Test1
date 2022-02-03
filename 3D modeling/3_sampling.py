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
grey_im180 = im180.convert("L")




## 삼각형으로 평면 만들어서 intensity 표현
max_size = (500, 500)
max_height = 20
min_height = 0

grey_im180.thumbnail(max_size)
print("resize : {0}".format(grey_im180.size))
imageNp = np.asarray(grey_im180)

# pixel intensity boundry
maxPix = imageNp.max()
minPix = imageNp.min()

# 평면 설정
(ncols, nrows) = grey_im180.size
vertices = np.zeros((nrows, ncols, 3))

for x in range(0, ncols):
    for y in range(0, nrows):
        z = (imageNp[y][x] * max_height) / maxPix
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
