import numpy as np
import cv2
import random 

from convex_collide import collide


def get_tri(size =50):
    return (np.random.randint(size,size=(3,2))).astype(np.int32)



def colr():
    return (np.random.randn(3)*256).astype(np.uint8).tolist()




image = np.zeros((768,1366,3),dtype=np.uint8)


triangles = []

for i in range(10000):

    tri = get_tri()

    tri[:,0]+= random.randint(0,1316) 
    tri[:,1]+= random.randint(0,718)

    flag = False

    for tri2 in triangles:

        if collide(tri,tri2):
            flag = True
            break

    if flag:
        continue
    
    triangles.append(tri)
    cv2.polylines(image,[tri],True,colr(),thickness=1)


cv2.imwrite('triangles.png',image)


print(len(triangles))


